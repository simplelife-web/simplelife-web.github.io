// Trabajador en segundo plano: carga Whisper y transcribe, uno por uno, los tramos de audio
// que le envía la página. Corre aparte para que la página no se congele.
// Transformers.js 4.3.1 (el mismo archivo publicado en npm), servido por jsDelivr.
import { pipeline, env } from 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.3.1/dist/transformers.min.js';

const LIB = new URL('./lib/', import.meta.url).href;
const ua = self.navigator.userAgent;
const isOldSafari = /^((?!chrome|android).)*safari/i.test(ua) && !self.navigator.gpu;

env.allowLocalModels = false;
if (!isOldSafari) {
  env.backends.onnx.wasm.wasmPaths = {
    mjs: LIB + 'ort-wasm-simd-threaded.asyncify.mjs',
    wasm: LIB + 'ort-wasm-simd-threaded.asyncify.wasm',
  };
}

let transcriber = null;
let loadedKey = '';
let loading = null;
let opts = { task: 'transcribe', return_timestamps: false };
const queue = [];
let ended = false;
let running = false;

async function detectGPU() {
  try {
    if (!self.navigator.gpu) return { webgpu: false, f16: false };
    const adapter = await self.navigator.gpu.requestAdapter();
    if (!adapter) return { webgpu: false, f16: false };
    return { webgpu: true, f16: adapter.features.has('shader-f16') };
  } catch {
    return { webgpu: false, f16: false };
  }
}

function dtypeFor(model, gpu) {
  if (!gpu.webgpu) return 'q8';
  if (model.includes('large')) {
    return { encoder_model: gpu.f16 ? 'fp16' : 'fp32', decoder_model_merged: 'q4' };
  }
  return { encoder_model: 'fp32', decoder_model_merged: 'q4' };
}

async function load(model) {
  const gpu = await detectGPU();
  const device = gpu.webgpu ? 'webgpu' : 'wasm';
  const key = model + '|' + device;
  if (transcriber && loadedKey === key) return device;
  if (transcriber) {
    try { await transcriber.dispose(); } catch {}
    transcriber = null;
  }
  const files = new Map();
  transcriber = await pipeline('automatic-speech-recognition', model, {
    device,
    dtype: dtypeFor(model, gpu),
    progress_callback: (p) => {
      if (p.status === 'progress' && p.total) {
        files.set(p.file, { loaded: p.loaded, total: p.total });
        let loaded = 0, total = 0;
        for (const f of files.values()) { loaded += f.loaded; total += f.total; }
        self.postMessage({ type: 'download', loaded, total });
      }
    },
  });
  loadedKey = key;
  return device;
}

function rms(a) {
  let s = 0;
  for (let i = 0; i < a.length; i++) s += a[i] * a[i];
  return Math.sqrt(s / Math.max(1, a.length));
}

// Frases que Whisper suele inventar cuando un tramo casi no tiene voz.
const HALLUCINATIONS = [
  /subt[ií]tulos (realizados|hechos) por/i,
  /amara\.org/i,
  /^\s*(gracias por ver( el video)?|suscr[ií]bete)[.!¡ ]*$/i,
];

async function processQueue() {
  if (running) return;
  running = true;
  try {
    await loading;
    while (queue.length) {
      const p = queue.shift();
      let text = '';
      const level = rms(p.audio);
      if (level > 0.004) {
        const out = await transcriber(p.audio, opts);
        text = (Array.isArray(out) ? out[0].text : out.text || '').trim();
        if (HALLUCINATIONS.some((r) => r.test(text)) && level < 0.02) text = '';
      }
      self.postMessage({ type: 'piece', index: p.index, start: p.start, end: p.end, text });
    }
    if (ended) self.postMessage({ type: 'done' });
  } catch (err) {
    self.postMessage({ type: 'error', message: String(err && err.message ? err.message : err) });
  } finally {
    running = false;
  }
}

self.onmessage = async (e) => {
  const m = e.data;
  if (m.type === 'gpu') {
    self.postMessage({ type: 'gpu', ...(await detectGPU()) });
  } else if (m.type === 'init') {
    queue.length = 0;
    ended = false;
    opts = { task: 'transcribe', return_timestamps: false };
    if (m.language && m.language !== 'auto') opts.language = m.language;
    loading = load(m.model).then((device) => self.postMessage({ type: 'ready', device }));
    loading.catch((err) => self.postMessage({ type: 'error', message: String(err && err.message ? err.message : err) }));
  } else if (m.type === 'piece') {
    queue.push(m);
    processQueue();
  } else if (m.type === 'end') {
    ended = true;
    processQueue();
  }
};
