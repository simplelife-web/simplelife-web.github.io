# -*- coding: utf-8 -*-
# Términos del glosario (parte 9): séptima tanda. Mezcla términos del
# Glosario del BCRP (campo "bcrp" con su nombre exacto) y conceptos básicos
# de los cursos de economía. Todo está redactado con palabras propias.

T = []

# --- Microeconomía ---------------------------------------------------------

T.append(dict(
slug="utilidad-marginal", t="Utilidad marginal", cat="mercados", ic="🍰",
alias="utilidad marginal decreciente satisfacción consumidor",
corto="Es la satisfacción extra que te da consumir una unidad más de algo.",
simple=[
r"La primera porción de torta te encanta; la tercera, ya no tanto. La <strong>utilidad marginal</strong> mide ese placer adicional de cada nueva unidad.",
r"Casi siempre es <strong>decreciente</strong>: cada unidad extra satisface menos que la anterior. Por eso estamos dispuestos a pagar menos por las unidades adicionales, y por eso la <a href='oferta-y-demanda.html'>curva de demanda</a> tiene pendiente negativa.",
],
formula=dict(
tex=r"UMg=\frac{\Delta U}{\Delta Q}",
donde=[(r"\Delta U", "cambio en la utilidad total"), (r"\Delta Q", "cambio en la cantidad consumida")],
calculo=[r"\frac{18-15}{3-2}=3"],
),
ejemplo=[
r"Si con dos vasos de chicha tu satisfacción es 15 y con tres es 18, la utilidad marginal del tercer vaso es 3.",
],
rel=["oferta-y-demanda", "excedente-del-consumidor-y-del-productor", "costo-marginal", "elasticidad-precio"],
))

T.append(dict(
slug="costo-marginal", t="Costo marginal", cat="mercados", ic="➕",
alias="costo marginal CMg costo de una unidad adicional",
corto="Es lo que cuesta producir una unidad más.",
simple=[
r"Si una panadería hace 100 panes y quiere hacer el pan 101, el <strong>costo marginal</strong> es lo que le añade ese pan extra en harina, gas y trabajo.",
r"Una empresa gana lo máximo cuando produce hasta el punto en que el costo marginal iguala al ingreso por la última unidad vendida. Si producir una unidad más cuesta más de lo que se cobra por ella, no conviene hacerla.",
],
formula=dict(
tex=r"CMg=\frac{\Delta CT}{\Delta Q}",
donde=[(r"\Delta CT", "cambio en el costo total"), (r"\Delta Q", "cambio en la cantidad producida")],
calculo=[r"\frac{530-500}{110-100}=3\ \text{soles}"],
),
ejemplo=[
r"Si producir 100 panes cuesta S/ 500 y producir 110 cuesta S/ 530, cada pan adicional cuesta en promedio S/ 3.",
],
rel=["costos-fijos-y-variables", "utilidad-marginal", "competencia-perfecta", "economias-de-escala"],
))

T.append(dict(
slug="costos-fijos-y-variables", t="Costos fijos y costos variables", cat="mercados", ic="🧾",
alias="costo fijo costo variable costo total costo medio",
corto="Los costos fijos se pagan igual aunque produzcas poco o mucho; los variables suben cuando produces más.",
simple=[
r"El alquiler del local es un <strong>costo fijo</strong>: lo pagas aunque ese mes no vendas nada. Los insumos son un <strong>costo variable</strong>: si haces más productos, gastas más en ellos.",
r"La suma de ambos es el costo total. Dividirlo entre la cantidad producida da el <strong>costo medio</strong>, que suele bajar al producir más porque el costo fijo se reparte entre más unidades.",
],
formula=dict(
tex=r"CT=CF+CV,\qquad CMe=\frac{CT}{Q}",
calculo=[r"CT=2000+5\times500=4500;\quad CMe=\frac{4500}{500}=9"],
),
ejemplo=[
r"Una juguería paga S/ 2000 de alquiler y gasta S/ 5 en fruta por jugo. Si vende 500 jugos al mes, su costo total es S/ 4500 y cada jugo le cuesta en promedio S/ 9.",
],
rel=["punto-de-equilibrio", "costo-marginal", "economias-de-escala", "costo-hundido"],
))

T.append(dict(
slug="costo-hundido", t="Costo hundido", cat="mercados", ic="⚓",
alias="costo hundido sunk cost falacia del costo hundido",
corto="Es un gasto que ya se hizo y que no se puede recuperar; por eso no debería influir en las decisiones futuras.",
simple=[
r"Si ya pagaste la entrada del cine y la película es mala, ese dinero no vuelve te quedes o te vayas. Es un <strong>costo hundido</strong>.",
r"La «falacia del costo hundido» es seguir en algo solo porque ya invertiste mucho. Una buena decisión compara solo los costos y beneficios <strong>que todavía vienen</strong>.",
],
ejemplo=[
r"Una empresa gastó S/ 1 millón en un proyecto que ya no es rentable. Si terminarlo cuesta S/ 500 mil más y solo generará S/ 300 mil, lo mejor es detenerlo, aunque se «pierda» lo ya gastado.",
],
rel=["costo-de-oportunidad", "costos-fijos-y-variables", "van", "expectativas"],
))

T.append(dict(
slug="economias-de-escala", t="Economías de escala", cat="mercados", ic="🏭",
alias="economías de escala deseconomías de escala producción a gran escala",
corto="Ocurren cuando producir más hace que cada unidad salga más barata.",
simple=[
r"Una fábrica grande puede comprar insumos al por mayor, usar maquinaria más eficiente y repartir sus costos fijos entre muchas unidades. Por eso su costo medio baja al crecer: tiene <strong>economías de escala</strong>.",
r"Pero si crece demasiado puede volverse difícil de coordinar y los costos vuelven a subir: son las <strong>deseconomías de escala</strong>.",
],
ejemplo=[
r"Una gran cadena de supermercados consigue mejores precios de sus proveedores que una bodega, porque compra en cantidades enormes.",
],
rel=["costos-fijos-y-variables", "monopolio", "productividad", "rendimientos-decrecientes"],
))

T.append(dict(
slug="rendimientos-decrecientes", t="Rendimientos decrecientes", cat="mercados", ic="📉",
alias="ley de rendimientos decrecientes producto marginal decreciente",
corto="Si agregas cada vez más de un insumo y mantienes fijos los demás, llega un punto en que cada unidad extra aporta menos.",
simple=[
r"En una chacra de tamaño fijo, el primer trabajador aumenta mucho la cosecha; el décimo, mucho menos, porque ya no hay tanto espacio ni herramientas para todos.",
r"Esta ley explica por qué no basta con añadir más de un solo factor para crecer sin límite; también es la idea central del <a href='modelo-de-solow.html'>modelo de Solow</a>.",
],
ejemplo=[
r"Con 1 trabajador, un taller produce 10 sillas; con 2, 18; con 3, 24. Cada nuevo trabajador suma menos: 10, 8 y 6 sillas.",
],
rel=["productividad", "modelo-de-solow", "economias-de-escala", "costo-marginal"],
))

T.append(dict(
slug="frontera-de-posibilidades-de-produccion", t="Frontera de posibilidades de producción", cat="mercados", ic="🌈",
alias="FPP curva de transformación escasez eficiencia",
corto="Es la curva que muestra las combinaciones máximas de dos bienes que una economía puede producir con sus recursos y tecnología.",
simple=[
r"Si un país solo produce papas y computadoras, la <strong>frontera de posibilidades de producción</strong> muestra cuántas de cada una puede hacer usando todos sus recursos. Producir más de una obliga a producir menos de la otra: ese sacrificio es el <a href='costo-de-oportunidad.html'>costo de oportunidad</a>.",
r"Un punto dentro de la curva indica recursos ociosos (por ejemplo, desempleo). La curva se desplaza hacia afuera cuando hay más recursos o mejor tecnología, es decir, cuando hay <a href='crecimiento-economico.html'>crecimiento</a>.",
],
ejemplo=[
r"Si para fabricar 10 computadoras más el país debe dejar de producir 50 toneladas de papa, el costo de oportunidad de cada computadora es 5 toneladas de papa.",
],
rel=["costo-de-oportunidad", "crecimiento-economico", "ventaja-comparativa", "productividad"],
))

T.append(dict(
slug="competencia-perfecta", t="Competencia perfecta", cat="mercados", ic="🏁",
alias="competencia perfecta precio aceptante mercado competitivo",
corto="Es un mercado ideal con muchísimos vendedores y compradores de un producto idéntico, donde nadie puede fijar el precio por sí solo.",
simple=[
r"En <strong>competencia perfecta</strong> hay muchas empresas pequeñas, el producto es igual en todas, la información es completa y es fácil entrar o salir del mercado. Cada empresa es «tomadora de precios»: si cobra más que el resto, nadie le compra.",
r"Es un modelo de referencia: pocos mercados lo cumplen del todo, pero sirve para comparar con el <a href='monopolio.html'>monopolio</a> y el <a href='oligopolio.html'>oligopolio</a>.",
],
ejemplo=[
r"Un mercado mayorista de papa se parece bastante: hay muchos productores, la papa de una variedad es casi igual y el precio lo fija el mercado.",
],
rel=["monopolio", "oligopolio", "competencia-monopolistica", "libre-competencia"],
))

T.append(dict(
slug="oligopolio", t="Oligopolio", cat="mercados", ic="🎩",
alias="oligopolio pocas empresas colusión cártel",
corto="Es un mercado dominado por pocas empresas grandes, donde cada una tiene en cuenta lo que hacen las demás.",
simple=[
r"En un <strong>oligopolio</strong>, unas pocas empresas concentran la mayor parte de las ventas. Si una baja precios, las otras suelen responder, así que sus decisiones están entrelazadas.",
r"El riesgo es que se pongan de acuerdo para subir precios (un <strong>cártel</strong>), algo prohibido por las normas de <a href='libre-competencia.html'>libre competencia</a> y que en el Perú vigila el Indecopi.",
],
ejemplo=[
r"Los mercados de telefonía móvil o de cerveza en muchos países están en manos de pocas empresas: son ejemplos típicos de oligopolio.",
],
rel=["monopolio", "competencia-perfecta", "libre-competencia", "equilibrio-de-nash"],
))

T.append(dict(
slug="competencia-monopolistica", t="Competencia monopolística", cat="mercados", ic="🍔",
alias="competencia monopolística diferenciación de producto marca",
corto="Es un mercado con muchas empresas que venden productos parecidos pero no iguales, y por eso cada una tiene algo de poder sobre su precio.",
simple=[
r"Hay muchos restaurantes de pollo a la brasa, pero cada uno tiene su sazón, su local y su marca. Esa <strong>diferenciación</strong> permite cobrar un poco más que la competencia sin perder a todos los clientes.",
r"Como es fácil abrir un nuevo local, las ganancias extraordinarias tienden a desaparecer a largo plazo.",
],
ejemplo=[
r"Una cafetería con buena decoración puede cobrar S/ 1 más por un café que otra cercana y aun así tener clientes fieles.",
],
rel=["competencia-perfecta", "monopolio", "oligopolio", "elasticidad-precio"],
))

T.append(dict(
slug="excedente-del-consumidor-y-del-productor", t="Excedente del consumidor y del productor", cat="mercados", ic="🎁",
alias="excedente del consumidor excedente del productor bienestar total",
corto="El excedente del consumidor es lo que te «ahorras» al pagar menos de lo que estabas dispuesto a pagar; el del productor, lo que gana el vendedor por encima de lo mínimo que aceptaría.",
simple=[
r"Si estabas dispuesto a pagar S/ 50 por unas zapatillas y las compras a S/ 35, tu <strong>excedente del consumidor</strong> es S/ 15.",
r"Si el vendedor las habría vendido hasta en S/ 25, su <strong>excedente del productor</strong> es S/ 10. La suma de ambos mide el bienestar que genera el mercado; impuestos, precios controlados o monopolios suelen reducirla.",
],
formula=dict(
tex=r"EC=\text{Disposición a pagar}-P,\qquad EP=P-\text{Precio mínimo aceptado}",
calculo=[r"EC=50-35=15;\quad EP=35-25=10"],
),
ejemplo=[
r"En ese ejemplo, el intercambio crea S/ 25 de bienestar: S/ 15 para el comprador y S/ 10 para el vendedor.",
],
rel=["oferta-y-demanda", "utilidad-marginal", "precio-maximo-y-minimo", "monopolio"],
))

T.append(dict(
slug="elasticidad-ingreso", t="Elasticidad ingreso", cat="mercados", ic="🪢",
alias="elasticidad ingreso de la demanda bienes de lujo bienes necesarios",
corto="Mide cuánto cambia la cantidad que compras de algo cuando cambia tu ingreso.",
simple=[
r"Si tu sueldo sube 10 % y compras 20 % más viajes, la elasticidad ingreso de los viajes es 2: son un bien de <strong>lujo</strong>. Si compras solo 3 % más arroz, su elasticidad es 0.3: es un bien <strong>necesario</strong>.",
r"Si la elasticidad es negativa, el bien es <a href='bienes-normales-e-inferiores.html'>inferior</a>: lo compras menos cuando ganas más.",
],
formula=dict(
tex=r"E_I=\frac{\%\Delta Q}{\%\Delta I}",
calculo=[r"\frac{20\,\%}{10\,\%}=2"],
),
ejemplo=[
r"Cuando la economía crece, las ventas de restaurantes y viajes suelen subir más rápido que las de alimentos básicos, porque su elasticidad ingreso es mayor.",
],
rel=["elasticidad-precio", "bienes-normales-e-inferiores", "bienes-sustitutos-y-complementarios", "consumo"],
))

T.append(dict(
slug="bienes-normales-e-inferiores", t="Bienes normales e inferiores", cat="mercados", ic="🔼",
alias="bien normal bien inferior bien de Giffen",
corto="Un bien normal se compra más cuando sube el ingreso; uno inferior se compra menos, porque la gente lo reemplaza por algo mejor.",
simple=[
r"La mayoría de bienes son <strong>normales</strong>: con más ingreso compramos más ropa, más carne o más servicios.",
r"Un bien <strong>inferior</strong> es el que se deja cuando se puede pagar algo mejor: por ejemplo, pasar de viajar en combi a usar taxi cuando el ingreso sube.",
],
ejemplo=[
r"Si a una familia le aumenta el sueldo y compra menos fideos baratos y más carne, para ella los fideos baratos se comportan como un bien inferior.",
],
rel=["elasticidad-ingreso", "bienes-sustitutos-y-complementarios", "oferta-y-demanda", "canasta-de-consumo"],
))

T.append(dict(
slug="bienes-sustitutos-y-complementarios", t="Bienes sustitutos y complementarios", cat="mercados", ic="☕",
alias="bienes sustitutos bienes complementarios elasticidad cruzada",
corto="Los sustitutos se pueden reemplazar entre sí (té o café); los complementarios se usan juntos (auto y gasolina).",
simple=[
r"Si sube el precio del café, mucha gente toma más té: son <strong>sustitutos</strong>. La demanda de uno sube cuando el otro se encarece.",
r"Si sube el precio de la gasolina, la gente compra menos autos: son <strong>complementarios</strong>. La demanda de uno cae cuando el otro se encarece. La <strong>elasticidad cruzada</strong> mide esa relación: es positiva entre sustitutos y negativa entre complementarios.",
],
formula=dict(
tex=r"E_{xy}=\frac{\%\Delta Q_x}{\%\Delta P_y}",
calculo=[r"\frac{6\,\%}{10\,\%}=0.6\ \text{(sustitutos)}"],
),
ejemplo=[
r"Si el pollo sube 10 % y la venta de pescado aumenta 6 %, la elasticidad cruzada es 0.6: para los consumidores son sustitutos.",
],
rel=["elasticidad-precio", "elasticidad-ingreso", "oferta-y-demanda", "bienes-normales-e-inferiores"],
))

T.append(dict(
slug="precio-maximo-y-minimo", t="Precio máximo y precio mínimo", cat="mercados", ic="🚧",
alias="control de precios precio tope precio piso escasez excedente",
corto="Son límites que fija el Estado: un precio máximo impide cobrar más de cierto monto; uno mínimo impide pagar menos.",
simple=[
r"Un <strong>precio máximo</strong> por debajo del equilibrio hace que la gente quiera comprar más de lo que se ofrece: aparecen <strong>escasez</strong>, colas y mercados negros.",
r"Un <strong>precio mínimo</strong> por encima del equilibrio hace que se ofrezca más de lo que se compra: aparece un <strong>excedente</strong>. El salario mínimo es un precio mínimo del trabajo.",
],
ejemplo=[
r"En el Perú de los años ochenta hubo controles de precios en muchos productos básicos, y fueron comunes las colas y la escasez en las tiendas.",
],
rel=["oferta-y-demanda", "excedente-del-consumidor-y-del-productor", "remuneracion-minima-vital", "subsidio"],
))

T.append(dict(
slug="externalidad", t="Externalidad", cat="bienestar", ic="🏭",
alias="externalidad negativa externalidad positiva contaminación impuesto pigouviano",
corto="Es un efecto, bueno o malo, que una actividad causa a terceros que no participan en ella y que no se paga ni se cobra.",
simple=[
r"Una fábrica que contamina un río perjudica a los pescadores sin pagarles: es una <strong>externalidad negativa</strong>. Quien se vacuna protege también a los demás: es una <strong>externalidad positiva</strong>.",
r"Como el mercado no cobra esos efectos, produce demasiado de lo dañino y muy poco de lo beneficioso. El Estado puede corregirlo con impuestos (llamados pigouvianos), normas o subsidios.",
],
ejemplo=[
r"El impuesto selectivo al consumo sobre cigarrillos y bebidas alcohólicas busca, en parte, que el precio refleje los daños a la salud que su consumo causa.",
],
rel=["bienes-publicos", "subsidio", "impuesto-directo-e-indirecto", "libre-competencia"],
))

T.append(dict(
slug="bienes-publicos", t="Bienes públicos", cat="bienestar", ic="🚦",
alias="bien público no rival no excluible polizón free rider",
corto="Son bienes que, una vez producidos, pueden usar todos a la vez y de los que es muy difícil excluir a alguien, como el alumbrado público.",
simple=[
r"Un bien público es <strong>no rival</strong> (que lo use yo no impide que lo uses tú) y <strong>no excluible</strong> (no se puede impedir que alguien lo aproveche).",
r"Por eso aparece el problema del <strong>polizón</strong>: cada uno espera que paguen los demás. Así, el mercado privado produce muy poco de estos bienes y suele proveerlos el Estado, financiados con impuestos.",
],
ejemplo=[
r"La defensa nacional, el alumbrado de las calles o un sistema de alerta de tsunamis protegen a todos, hayan pagado o no.",
],
rel=["externalidad", "presupuesto-publico", "tributo", "inversion-publica"],
))

T.append(dict(
slug="informacion-asimetrica", t="Información asimétrica", cat="mercados", ic="🙈",
alias="información asimétrica mercado de limones Akerlof",
corto="Ocurre cuando una de las partes de un trato sabe mucho más que la otra sobre lo que se negocia.",
simple=[
r"El vendedor de un auto usado conoce sus fallas; el comprador, no. Esa <strong>información asimétrica</strong> hace que el comprador desconfíe y ofrezca menos, y que los dueños de autos buenos prefieran no venderlos.",
r"De ella nacen dos problemas famosos: la <a href='seleccion-adversa.html'>selección adversa</a> (antes del trato) y el <a href='riesgo-moral.html'>riesgo moral</a> (después del trato). Garantías, centrales de riesgo y certificaciones ayudan a reducirla.",
],
ejemplo=[
r"Un banco no sabe con certeza si quien pide un préstamo pagará. Por eso revisa la <a href='central-de-riesgos.html'>central de riesgos</a> y pide garantías.",
],
rel=["seleccion-adversa", "riesgo-moral", "central-de-riesgos", "garantia"],
))

T.append(dict(
slug="seleccion-adversa", t="Selección adversa", cat="mercados", ic="🍋",
alias="selección adversa información oculta seguros",
corto="Es cuando, por falta de información, terminan entrando a un trato justo las personas o productos más riesgosos.",
simple=[
r"Si un seguro de salud cobra lo mismo a todos, lo compran sobre todo quienes saben que se enfermarán más. La aseguradora pierde, sube el precio y los más sanos se retiran. Eso es <strong>selección adversa</strong>.",
r"Ocurre <strong>antes</strong> de firmar el contrato, por información oculta. Exámenes médicos, historiales de crédito o periodos de carencia buscan reducirla.",
],
ejemplo=[
r"Si un prestamista cobra tasas muy altas, puede atraer justamente a los deudores más dispuestos a arriesgar, que son los que menos pagan.",
],
rel=["informacion-asimetrica", "riesgo-moral", "compania-de-seguros", "riesgo-de-credito"],
))

T.append(dict(
slug="riesgo-moral", t="Riesgo moral", cat="mercados", ic="🎲",
alias="riesgo moral moral hazard acción oculta rescate",
corto="Es cuando alguien protegido contra un riesgo se comporta de forma más descuidada, porque las consecuencias las pagará otro.",
simple=[
r"Quien tiene su auto asegurado contra robo puede volverse menos cuidadoso al estacionarlo. Eso es <strong>riesgo moral</strong>: ocurre <strong>después</strong> del contrato, porque la otra parte no puede vigilar todo lo que haces.",
r"En finanzas, si los bancos creen que el Estado siempre los rescatará, pueden tomar demasiados riesgos. Deducibles, copagos y supervisión ayudan a limitarlo.",
],
ejemplo=[
r"Los seguros suelen tener un deducible: como pagas una parte del daño, sigues teniendo motivos para cuidarte.",
],
rel=["informacion-asimetrica", "seleccion-adversa", "compania-de-seguros", "quiebra-bancaria"],
))

T.append(dict(
slug="equilibrio-de-nash", t="Equilibrio de Nash", cat="mercados", ic="♟️",
alias="equilibrio de Nash teoría de juegos estrategia óptima",
corto="Es una situación en la que cada participante hace lo mejor que puede dado lo que hacen los demás, y nadie gana cambiando solo su decisión.",
simple=[
r"La <strong>teoría de juegos</strong> estudia decisiones en las que el resultado de cada uno depende de lo que hagan los otros. En un <strong>equilibrio de Nash</strong>, nadie quiere cambiar de estrategia por su cuenta.",
r"Ese equilibrio no siempre es el mejor para el grupo, como muestra el <a href='dilema-del-prisionero.html'>dilema del prisionero</a>.",
],
ejemplo=[
r"Dos grifos vecinos fijan el precio del combustible. Si ninguno puede ganar más subiendo o bajando su precio mientras el otro mantiene el suyo, están en un equilibrio de Nash.",
],
rel=["dilema-del-prisionero", "oligopolio", "expectativas-racionales", "competencia-perfecta"],
))

T.append(dict(
slug="dilema-del-prisionero", t="Dilema del prisionero", cat="mercados", ic="🔒",
alias="dilema del prisionero teoría de juegos cooperación",
corto="Es un ejemplo de teoría de juegos en el que dos personas, buscando cada una su mejor opción, terminan peor que si hubieran cooperado.",
simple=[
r"Dos detenidos son interrogados por separado. Si ninguno confiesa, ambos reciben 1 año. Si uno confiesa y el otro no, el que confiesa sale libre y el otro recibe 10 años. Si ambos confiesan, reciben 5 años cada uno.",
r"Confesar es lo mejor para cada uno haga lo que haga el otro, así que ambos confiesan y pasan 5 años presos, aunque callar les habría dado solo 1. Explica por qué es difícil cooperar, por ejemplo, entre empresas de un <a href='oligopolio.html'>oligopolio</a> o entre países que deben reducir su contaminación.",
],
ejemplo=[
r"Dos empresas preferirían no gastar en publicidad, pero cada una teme que la otra sí lo haga. Al final ambas gastan y ninguna gana clientes.",
],
rel=["equilibrio-de-nash", "oligopolio", "externalidad", "libre-competencia"],
))

T.append(dict(
slug="concentracion-de-mercado", t="Concentración de mercado (índice Herfindahl-Hirschman)", cat="mercados", ic="🥧",
alias="índice Herfindahl Hirschman IHH HHI concentración participación de mercado",
corto="Mide si un mercado está repartido entre muchas empresas o concentrado en pocas; el índice más usado es el de Herfindahl-Hirschman.",
simple=[
r"El índice de <strong>Herfindahl-Hirschman</strong> (IHH) se calcula elevando al cuadrado la participación de mercado de cada empresa, en porcentaje, y sumando los resultados.",
r"Va desde casi 0 (muchísimas empresas pequeñas) hasta 10 000 (un monopolio). Las autoridades de competencia lo usan para evaluar fusiones: si una fusión concentra mucho el mercado, la revisan con más cuidado.",
],
formula=dict(
tex=r"IHH=\sum_{i=1}^{n} s_i^{2}",
donde=[(r"s_i", "participación de mercado de la empresa i, en porcentaje")],
calculo=[r"50^2+30^2+20^2=2500+900+400=3800"],
),
ejemplo=[
r"Un mercado con tres empresas que tienen 50 %, 30 % y 20 % de las ventas tiene un IHH de 3800: está muy concentrado.",
],
rel=["monopolio", "oligopolio", "fusion-y-adquisicion", "libre-competencia"],
))

# --- Macroeconomía ---------------------------------------------------------

T.append(dict(
slug="curva-de-phillips", t="Curva de Phillips", cat="trabajo", ic="🔀",
alias="curva de Phillips inflación desempleo trade-off",
corto="Es la relación que muestra que, en el corto plazo, menos desempleo suele venir con más inflación, y viceversa.",
simple=[
r"Cuando la economía está muy activa y hay poco desempleo, las empresas compiten por trabajadores y suben sueldos y precios: la inflación sube. Cuando hay mucho desempleo, pasa lo contrario.",
r"Esa relación no es estable a largo plazo: si la gente espera más inflación, la curva se desplaza. Por eso se habla de la curva de Phillips «aumentada con expectativas» y de una <a href='tasa-natural-de-desempleo.html'>tasa natural de desempleo</a>.",
],
formula=dict(
tex=r"\pi=\pi^{e}-\beta\,(u-u_n)",
donde=[(r"\pi", "inflación"), (r"\pi^{e}", "inflación esperada"), (r"u", "tasa de desempleo"), (r"u_n", "tasa natural de desempleo"), (r"\beta", "sensibilidad de la inflación al desempleo")],
calculo=[r"2-0.5\times(5-6)=2.5\,\%"],
),
ejemplo=[
r"Si la inflación esperada es 2 %, el desempleo natural 6 % y el desempleo cae a 5 %, con \(\beta=0.5\) la inflación sube a 2.5 %.",
],
rel=["tasa-natural-de-desempleo", "inflacion", "tasa-de-desempleo", "expectativas-adaptativas"],
))

T.append(dict(
slug="tasa-natural-de-desempleo", t="Tasa natural de desempleo", cat="trabajo", ic="🌿",
alias="tasa natural de desempleo NAIRU desempleo de equilibrio",
corto="Es el nivel de desempleo que existe incluso cuando la economía funciona normalmente, sin presionar la inflación al alza ni a la baja.",
simple=[
r"Aun en buenos tiempos hay gente cambiando de empleo o cuyas habilidades no coinciden con lo que piden las empresas. Ese desempleo «de fondo» es la <strong>tasa natural</strong>; también se le llama NAIRU.",
r"Si el desempleo baja de ese nivel, la inflación tiende a subir; si sube por encima, tiende a bajar. Mejores sistemas de búsqueda de empleo y capacitación pueden reducirla.",
],
ejemplo=[
r"Si la tasa natural de un país es 6 % y el desempleo llega a 4 % en un auge, probablemente los sueldos y los precios empiecen a subir más rápido.",
],
rel=["tipos-de-desempleo", "curva-de-phillips", "tasa-de-desempleo", "brecha-del-producto"],
))

T.append(dict(
slug="tipos-de-desempleo", t="Tipos de desempleo", cat="trabajo", ic="🧩",
bcrp="Desempleo", alias="desempleo friccional desempleo estructural desempleo cíclico desempleo estacional",
corto="El desempleo puede ser friccional (cambio de empleo), estructural (habilidades que ya no se piden), cíclico (por una recesión) o estacional.",
simple=[
r"<strong>Friccional</strong>: personas que dejaron un trabajo y buscan otro. <strong>Estructural</strong>: habilidades que ya no se demandan, por ejemplo por un cambio tecnológico. <strong>Estacional</strong>: trabajos que solo existen en ciertas épocas, como las cosechas.",
r"<strong>Cíclico</strong>: el que aparece cuando la economía entra en <a href='recesion.html'>recesión</a> y las empresas despiden. Es el que la política económica intenta reducir con medidas <a href='politica-anticiclica.html'>anticíclicas</a>.",
],
ejemplo=[
r"Una recién egresada que busca su primer empleo está en desempleo friccional; un operario reemplazado por una máquina, en desempleo estructural.",
],
rel=["tasa-de-desempleo", "tasa-natural-de-desempleo", "subempleo", "ciclo-economico"],
))

T.append(dict(
slug="ley-de-okun", t="Ley de Okun", cat="produccion", ic="⚖️",
alias="ley de Okun crecimiento y desempleo brecha del producto",
corto="Es una regla empírica que relaciona el crecimiento de la economía con el desempleo: si se crece poco, el desempleo sube.",
simple=[
r"Arthur Okun observó en Estados Unidos que, cuando el PBI crece por debajo de su ritmo normal, el desempleo aumenta. En su versión clásica, cada punto de producción por debajo del potencial se asocia con medio punto más de desempleo, aunque la cifra cambia según el país y la época.",
r"No es una ley exacta, sino una relación promedio útil para estimar el costo de una desaceleración en empleos.",
],
formula=dict(
tex=r"u-u_n=-\beta\,\frac{Y-Y^{*}}{Y^{*}}\times100",
donde=[(r"Y", "PBI observado"), (r"Y^{*}", "PBI potencial"), (r"\beta", "coeficiente de Okun")],
calculo=[r"-0.5\times(-2)=+1\ \text{punto de desempleo}"],
),
ejemplo=[
r"Si el PBI está 2 % por debajo de su potencial y el coeficiente es 0.5, el desempleo estaría 1 punto por encima de su tasa natural.",
],
rel=["brecha-del-producto", "tasa-natural-de-desempleo", "crecimiento-potencial", "recesion"],
))

T.append(dict(
slug="propension-marginal-a-consumir", t="Propensión marginal a consumir", cat="produccion", ic="🛒",
alias="propensión marginal a consumir PMgC propensión marginal a ahorrar PMgS",
corto="Es la parte de cada sol adicional de ingreso que una persona gasta en consumo; el resto lo ahorra.",
simple=[
r"Si te dan S/ 100 extra y gastas S/ 80, tu <strong>propensión marginal a consumir</strong> es 0.8, y tu propensión marginal a ahorrar es 0.2. Ambas suman 1.",
r"Las familias de menores ingresos suelen tener una propensión a consumir más alta, porque necesitan gastar casi todo lo que reciben. Este dato es clave para calcular el <a href='multiplicador-keynesiano.html'>multiplicador</a> del gasto.",
],
formula=dict(
tex=r"PMgC=\frac{\Delta C}{\Delta Y},\qquad PMgC+PMgS=1",
calculo=[r"\frac{80}{100}=0.8"],
),
ejemplo=[
r"Si un bono de S/ 100 se gasta en S/ 80 y se ahorran S/ 20, la propensión marginal a consumir es 0.8.",
],
rel=["multiplicador-keynesiano", "consumo", "ahorro", "demanda-agregada"],
))

T.append(dict(
slug="multiplicador-keynesiano", t="Multiplicador keynesiano", cat="produccion", ic="✖️",
alias="multiplicador del gasto multiplicador fiscal Keynes",
corto="Indica cuánto aumenta la producción total por cada sol adicional de gasto, porque ese gasto se convierte en ingreso de otros que también gastan.",
simple=[
r"Si el Estado gasta S/ 100 en una obra, los trabajadores reciben ese dinero y gastan una parte; quienes les venden también gastan una parte, y así sucesivamente. Al final, la producción sube más de S/ 100.",
r"Cuanto mayor es la <a href='propension-marginal-a-consumir.html'>propensión marginal a consumir</a>, mayor es el multiplicador. En la práctica es menor que en el modelo simple, porque parte del gasto se va en importaciones e impuestos.",
],
formula=dict(
tex=r"k=\frac{1}{1-PMgC}",
calculo=[r"\frac{1}{1-0.8}=5"],
),
ejemplo=[
r"Con una propensión a consumir de 0.8, el multiplicador simple es 5: S/ 100 de gasto nuevo elevarían la producción en S/ 500. Con importaciones e impuestos, el efecto real sería bastante menor.",
],
rel=["propension-marginal-a-consumir", "impulso-fiscal", "politica-fiscal", "demanda-agregada"],
))

T.append(dict(
slug="trampa-de-liquidez", t="Trampa de liquidez", cat="dinero", ic="🕳️",
alias="trampa de liquidez tasa cero límite inferior política monetaria",
corto="Es una situación en la que las tasas de interés ya están cerca de cero y el banco central ya no puede estimular la economía bajándolas más.",
simple=[
r"Normalmente, bajar la tasa de interés anima el crédito y el gasto. Pero si ya está casi en cero, y la gente prefiere guardar efectivo por miedo, la política monetaria pierde fuerza: es una <strong>trampa de liquidez</strong>.",
r"En esos casos, los bancos centrales recurren a herramientas no convencionales, como comprar bonos a gran escala, y cobra más importancia la <a href='politica-fiscal.html'>política fiscal</a>.",
],
ejemplo=[
r"Japón pasó años con tasas cercanas a cero y poca inflación; muchos economistas lo citan como ejemplo de trampa de liquidez.",
],
rel=["politica-monetaria", "tasa-de-referencia", "deflacion", "politica-fiscal"],
))

T.append(dict(
slug="teoria-cuantitativa-del-dinero", t="Teoría cuantitativa del dinero", cat="dinero", ic="🧮",
alias="teoría cuantitativa ecuación de cambio MV=PY Fisher monetarismo",
corto="Sostiene que, a largo plazo, si la cantidad de dinero crece más rápido que la producción, el resultado es inflación.",
simple=[
r"Se resume en la <strong>ecuación de cambio</strong>: el dinero por las veces que circula es igual a los precios por la producción. Si la <a href='velocidad-del-dinero.html'>velocidad</a> es estable y la producción no cambia mucho, más dinero termina subiendo los precios.",
r"La <a href='hiperinflacion.html'>hiperinflación</a> peruana de fines de los ochenta, cuando se imprimía dinero para financiar el déficit, es un ejemplo extremo de esta idea.",
],
formula=dict(
tex=r"M\cdot V=P\cdot Y",
donde=[(r"M", "cantidad de dinero"), (r"V", "velocidad de circulación"), (r"P", "nivel de precios"), (r"Y", "producción real")],
calculo=[r"\%\Delta P\approx\%\Delta M+\%\Delta V-\%\Delta Y=10+0-3=7\,\%"],
),
ejemplo=[
r"Si el dinero crece 10 % al año, la velocidad no cambia y la producción crece 3 %, la inflación tendería a ser cerca de 7 %.",
],
rel=["velocidad-del-dinero", "agregados-monetarios", "inflacion", "senoreaje"],
))

T.append(dict(
slug="modelo-is-lm", t="Modelo IS-LM", cat="produccion", ic="✂️",
alias="IS-LM Hicks curva IS curva LM equilibrio macroeconómico",
corto="Es un modelo de corto plazo que muestra cómo se determinan juntos la producción y la tasa de interés, uniendo el mercado de bienes y el de dinero.",
simple=[
r"La curva <strong>IS</strong> reúne las combinaciones de tasa de interés y producción en que el gasto iguala a la producción: a menor tasa, más inversión y más producción. La curva <strong>LM</strong> reúne las combinaciones en que la demanda de dinero iguala a la oferta: a más producción, más demanda de dinero y mayor tasa.",
r"Donde se cruzan está el equilibrio. Una expansión fiscal desplaza la IS a la derecha; una expansión monetaria desplaza la LM. Es una herramienta clásica de los cursos de macroeconomía.",
],
ejemplo=[
r"Si el Estado aumenta su gasto, la IS se mueve a la derecha: sube la producción, pero también la tasa de interés, lo que frena en parte la inversión privada (el <a href='efecto-desplazamiento.html'>efecto desplazamiento</a>).",
],
rel=["efecto-desplazamiento", "politica-fiscal", "politica-monetaria", "demanda-de-dinero"],
))

T.append(dict(
slug="efecto-desplazamiento", t="Efecto desplazamiento (crowding out)", cat="estado", ic="🫸",
alias="crowding out efecto expulsión desplazamiento de la inversión privada",
corto="Es cuando un mayor gasto o endeudamiento del Estado reduce la inversión privada, porque sube la tasa de interés o se queda con el ahorro disponible.",
simple=[
r"Si el Estado pide mucho dinero prestado, compite con las empresas por el ahorro del país. Eso puede subir las tasas de interés y hacer que algunas empresas dejen de invertir.",
r"El tamaño del efecto depende de la situación: en una recesión con tasas bajas suele ser pequeño; en una economía a plena capacidad puede ser grande.",
],
ejemplo=[
r"Si el Gobierno coloca muchos bonos y los bancos prefieren comprarlos antes que prestar a empresas, parte de la inversión privada se desplaza.",
],
rel=["modelo-is-lm", "deficit-fiscal", "deuda-publica", "multiplicador-keynesiano"],
))

T.append(dict(
slug="curva-de-laffer", t="Curva de Laffer", cat="impuestos", ic="⛰️",
alias="curva de Laffer tasa impositiva recaudación óptima",
corto="Muestra que subir la tasa de un impuesto no siempre aumenta la recaudación: si la tasa es demasiado alta, la gente trabaja, invierte o declara menos.",
simple=[
r"Con una tasa de 0 % no se recauda nada, y con una de 100 % tampoco, porque nadie tendría motivos para generar ingresos declarados. Entre ambos extremos hay un punto que maximiza la recaudación.",
r"El debate real es dónde está ese punto para cada impuesto y país; no se puede asumir que bajar impuestos siempre aumenta lo recaudado.",
],
ejemplo=[
r"Si un impuesto es muy alto, puede crecer la <a href='evasion-y-elusion-tributaria.html'>evasión</a> y la informalidad, y la recaudación termina siendo menor que con una tasa moderada.",
],
rel=["tasa-impositiva-marginal", "presion-tributaria", "evasion-y-elusion-tributaria", "ingresos-tributarios"],
))

T.append(dict(
slug="deficits-gemelos", t="Déficits gemelos", cat="estado", ic="👯",
alias="déficit gemelos déficit fiscal y déficit en cuenta corriente",
corto="Es la idea de que un déficit fiscal grande suele ir acompañado de un déficit en la cuenta corriente con el exterior.",
simple=[
r"Si el Estado gasta más de lo que recauda y el sector privado no ahorra más para compensarlo, el país en conjunto necesita financiarse con ahorro externo. Eso se refleja en un déficit en <a href='balanza-en-cuenta-corriente.html'>cuenta corriente</a>.",
r"La relación no es automática: depende de cómo reaccionen el ahorro y la inversión privados.",
],
formula=dict(
tex=r"CC=(S_p-I)+(T-G)",
donde=[(r"CC", "saldo en cuenta corriente"), (r"S_p-I", "ahorro privado menos inversión"), (r"T-G", "saldo fiscal")],
calculo=[r"(1-0)+(-4)=-3\ \%\ \text{del PBI}"],
),
ejemplo=[
r"Si el saldo privado es +1 % del PBI y el déficit fiscal es 4 % del PBI, la cuenta corriente tendría un déficit de 3 % del PBI.",
],
rel=["deficit-fiscal", "balanza-en-cuenta-corriente", "brecha-ahorro-inversion", "efecto-desplazamiento"],
))

T.append(dict(
slug="modelo-de-solow", t="Modelo de Solow", cat="produccion", ic="🌱",
alias="modelo de Solow-Swan crecimiento exógeno estado estacionario progreso técnico",
corto="Es el modelo básico de crecimiento económico: explica que acumular capital ayuda a crecer, pero que a largo plazo lo que sostiene el crecimiento es el progreso técnico.",
simple=[
r"Robert Solow mostró que, por los <a href='rendimientos-decrecientes.html'>rendimientos decrecientes</a>, cada máquina adicional aporta menos. Por eso un país no puede crecer para siempre solo ahorrando e invirtiendo más: llega a un <strong>estado estacionario</strong>.",
r"Lo que permite seguir creciendo es la mejora de la tecnología y la <a href='productividad.html'>productividad</a>. El modelo también predice que los países pobres podrían crecer más rápido que los ricos (convergencia), si tienen condiciones parecidas.",
],
formula=dict(
tex=r"\Delta k=s\,f(k)-(n+\delta)\,k",
donde=[(r"k", "capital por trabajador"), (r"s", "tasa de ahorro"), (r"f(k)", "producción por trabajador"), (r"n", "crecimiento de la población"), (r"\delta", "depreciación")],
calculo=[r"0.2\times10-(0.01+0.05)\times30=2-1.8=0.2"],
),
ejemplo=[
r"Si cada trabajador produce 10, se ahorra 20 %, hay 30 de capital por trabajador, la población crece 1 % y el capital se deprecia 5 %, el capital por trabajador todavía aumenta en 0.2: la economía aún no llega a su estado estacionario.",
],
rel=["rendimientos-decrecientes", "productividad", "fuentes-de-crecimiento", "crecimiento-economico"],
))

T.append(dict(
slug="enfermedad-holandesa", t="Enfermedad holandesa", cat="comercio", ic="🌷",
alias="enfermedad holandesa auge de materias primas apreciación desindustrialización",
corto="Es cuando un auge de exportaciones de recursos naturales aprecia la moneda y perjudica a otros sectores exportadores, como la industria o la agricultura.",
simple=[
r"El nombre viene de los Países Bajos, que en los años sesenta descubrieron gas natural. Al entrar muchos dólares, la moneda local se fortalece y los demás productos del país se vuelven caros para el resto del mundo.",
r"El riesgo para países mineros como el Perú es depender demasiado de las <a href='materias-primas.html'>materias primas</a>. Ahorrar parte de los ingresos extraordinarios, por ejemplo en un <a href='fondo-de-estabilizacion-fiscal.html'>fondo de estabilización</a>, ayuda a evitarlo.",
],
ejemplo=[
r"Si un boom del cobre trae muchos dólares y el sol se aprecia, una empresa que exporta confecciones recibe menos soles por cada dólar que vende y pierde competitividad.",
],
rel=["materias-primas", "tipo-de-cambio-real", "terminos-de-intercambio", "fondo-de-estabilizacion-fiscal"],
))

T.append(dict(
slug="trilema-de-la-economia-abierta", t="Trilema de la economía abierta", cat="dinero", ic="🔺",
alias="trinidad imposible trilema Mundell tipo de cambio fijo libre movilidad de capitales política monetaria independiente",
corto="Dice que un país no puede tener a la vez tipo de cambio fijo, libre movimiento de capitales y política monetaria independiente: solo dos de las tres.",
simple=[
r"Si un país fija su tipo de cambio y deja que el capital entre y salga libremente, debe tener las mismas tasas de interés que el país al que se ata; pierde su política monetaria.",
r"Si quiere política monetaria propia y libre movimiento de capitales, debe dejar flotar su moneda, que es básicamente la opción del Perú, con intervenciones para suavizar la volatilidad. La tercera combinación exige controlar los capitales.",
],
ejemplo=[
r"Un país que ata su moneda al dólar y permite el libre movimiento de capitales tiene que subir o bajar sus tasas al ritmo de la Reserva Federal, aunque su economía necesite otra cosa.",
],
rel=["regimen-cambiario", "politica-monetaria", "control-cambiario", "paridad-de-tasas-de-interes"],
))

T.append(dict(
slug="paridad-de-tasas-de-interes", t="Paridad de tasas de interés", cat="mercados", ic="🟰",
alias="paridad cubierta paridad descubierta de tasas de interés arbitraje",
corto="Dice que la diferencia de tasas de interés entre dos monedas debería compensarse con lo que se espera que cambie el tipo de cambio.",
simple=[
r"Si en soles se gana 5 % y en dólares 3 %, ¿por qué no todos ahorran en soles? Porque podría esperarse que el sol se deprecie cerca de 2 %, lo que borraría la ventaja.",
r"Cuando se usa un forward para cubrirse del riesgo cambiario, se habla de paridad <strong>cubierta</strong>; cuando se usa la expectativa, de paridad <strong>descubierta</strong>.",
],
formula=dict(
tex=r"i\approx i^{*}+\frac{E^{e}-E}{E}",
donde=[(r"i", "tasa en moneda local"), (r"i^{*}", "tasa en moneda extranjera"), (r"E", "tipo de cambio actual"), (r"E^{e}", "tipo de cambio esperado")],
calculo=[r"3\,\%+\frac{3.774-3.70}{3.70}=3\,\%+2\,\%=5\,\%"],
),
ejemplo=[
r"Si en dólares se gana 3 % y se espera que el dólar pase de S/ 3.70 a S/ 3.774 (2 % más), solo convendría ahorrar en soles si la tasa en soles supera el 5 %.",
],
rel=["tipo-de-cambio", "contrato-forward", "trilema-de-la-economia-abierta", "diferencial-cambiario"],
))

T.append(dict(
slug="curva-de-lorenz", t="Curva de Lorenz", cat="bienestar", ic="🌀",
alias="curva de Lorenz desigualdad distribución del ingreso Gini",
corto="Es un gráfico que muestra qué porcentaje del ingreso total recibe cada porcentaje de la población, ordenada de menor a mayor ingreso.",
simple=[
r"Si todos ganaran lo mismo, el 20 % de la población tendría el 20 % del ingreso, y la curva sería una línea recta (la línea de igualdad). Cuanto más se aleja la curva de esa línea, más desigualdad hay.",
r"El <a href='coeficiente-de-gini.html'>coeficiente de Gini</a> se calcula a partir de la curva de Lorenz: compara el área entre la curva y la línea de igualdad con el área total bajo esa línea.",
],
ejemplo=[
r"Si el 50 % más pobre recibe solo el 20 % del ingreso, el punto (50 %, 20 %) de la curva queda muy por debajo de la línea de igualdad.",
],
rel=["coeficiente-de-gini", "distribucion-del-ingreso", "pobreza-monetaria", "indice-de-desarrollo-humano"],
))

# --- Finanzas --------------------------------------------------------------

T.append(dict(
slug="diversificacion", t="Diversificación", cat="finanzas", ic="🧺",
alias="diversificar no poner todos los huevos en una canasta riesgo no sistemático",
corto="Es repartir tu dinero entre varias inversiones distintas para que, si a una le va mal, no pierdas todo.",
simple=[
r"Si inviertes todo en una sola empresa y quiebra, lo pierdes todo. Si repartes entre muchas empresas, sectores y tipos de activos, las caídas de unas se compensan con las subidas de otras.",
r"La diversificación reduce el riesgo propio de cada inversión, pero no elimina el riesgo de todo el mercado (por ejemplo, una crisis mundial), que se mide con la <a href='beta-y-capm.html'>beta</a>.",
],
ejemplo=[
r"Un <a href='fondo-mutuo.html'>fondo mutuo</a> o un <a href='etf.html'>ETF</a> te permite diversificar con poco dinero, porque reúne muchas acciones o bonos en un solo producto.",
],
rel=["portafolio", "fondo-mutuo", "etf", "beta-y-capm"],
))

T.append(dict(
slug="beta-y-capm", t="Beta y modelo CAPM", cat="finanzas", ic="β",
alias="beta CAPM modelo de valoración de activos de capital rentabilidad esperada prima de mercado",
corto="La beta mide cuánto se mueve una acción cuando se mueve el mercado; el CAPM usa la beta para calcular qué rentabilidad debería exigirse a esa inversión.",
simple=[
r"Una acción con <strong>beta</strong> 1 se mueve igual que el mercado; con beta 1.5, se mueve 50 % más (sube y baja más); con beta 0.5, la mitad.",
r"El <strong>CAPM</strong> dice que la rentabilidad exigida es la tasa sin riesgo más una prima proporcional a la beta. Se usa para estimar el costo del capital propio de una empresa.",
],
formula=dict(
tex=r"E(R_i)=R_f+\beta_i\,\big(E(R_m)-R_f\big)",
donde=[(r"R_f", "tasa libre de riesgo"), (r"\beta_i", "beta de la acción"), (r"E(R_m)", "rentabilidad esperada del mercado")],
calculo=[r"4\,\%+1.2\times(10\,\%-4\,\%)=11.2\,\%"],
),
ejemplo=[
r"Con una tasa sin riesgo de 4 %, una rentabilidad esperada del mercado de 10 % y una beta de 1.2, la acción debería ofrecer al menos 11.2 % anual.",
],
rel=["diversificacion", "wacc", "prima-de-riesgo", "rentabilidad"],
))

T.append(dict(
slug="wacc", t="Costo promedio ponderado de capital (WACC)", cat="finanzas", ic="🏗️",
alias="WACC costo de capital costo promedio ponderado tasa de descuento de proyectos",
corto="Es el costo promedio que paga una empresa por su financiamiento, combinando lo que le cuesta su deuda y lo que exigen sus accionistas.",
simple=[
r"Una empresa se financia con deuda (bancos, bonos) y con capital propio (accionistas). Cada fuente tiene su costo; el <strong>WACC</strong> los promedia según cuánto pesa cada una.",
r"Como los intereses reducen el impuesto a la renta, el costo de la deuda se toma después de impuestos. El WACC se usa como <a href='tasa-de-descuento.html'>tasa de descuento</a> para calcular el <a href='van.html'>VAN</a> de proyectos.",
],
formula=dict(
tex=r"WACC=\frac{E}{V}\,k_e+\frac{D}{V}\,k_d\,(1-t)",
donde=[(r"E", "capital propio"), (r"D", "deuda"), (r"V", "E + D"), (r"k_e", "costo del capital propio"), (r"k_d", "costo de la deuda"), (r"t", "tasa del impuesto a la renta")],
calculo=[r"0.6\times12\,\%+0.4\times8\,\%\times(1-0.295)\approx9.46\,\%"],
),
ejemplo=[
r"Una empresa con 60 % de capital propio que cuesta 12 %, 40 % de deuda que cuesta 8 % y una tasa de impuesto de 29.5 % tiene un WACC cercano a 9.5 %.",
],
rel=["beta-y-capm", "van", "tir", "tasa-de-descuento"],
))

T.append(dict(
slug="flujo-de-caja", t="Flujo de caja", cat="finanzas", ic="🌊",
alias="flujo de caja cash flow flujo de efectivo flujo de caja libre",
corto="Es el registro del dinero que realmente entra y sale de una empresa o persona en un periodo.",
simple=[
r"Una empresa puede tener utilidades en el <a href='estado-de-resultados.html'>estado de resultados</a> y, aun así, quedarse sin efectivo si sus clientes le pagan tarde. El <strong>flujo de caja</strong> muestra el dinero que de verdad se mueve.",
r"Para evaluar proyectos se proyectan los flujos de caja futuros y se traen a valor presente para calcular el <a href='van.html'>VAN</a> y la <a href='tir.html'>TIR</a>.",
],
formula=dict(
tex=r"\text{Flujo de caja neto}=\text{Entradas de efectivo}-\text{Salidas de efectivo}",
calculo=[r"25\,000-21\,500=3500\ \text{soles}"],
),
ejemplo=[
r"Si en un mes una bodega cobra S/ 25 000 y paga S/ 21 500 entre mercadería, alquiler y sueldos, su flujo de caja neto es S/ 3500.",
],
rel=["van", "tir", "capital-de-trabajo", "estado-de-resultados"],
))

T.append(dict(
slug="ratio-de-liquidez", t="Ratio de liquidez", cat="finanzas", ic="🚰",
bcrp="Coeficiente de liquidez", alias="ratio de liquidez coeficiente de liquidez razón corriente prueba ácida",
corto="Mide si una empresa o un banco tiene suficientes activos líquidos para pagar sus obligaciones de corto plazo.",
simple=[
r"En una empresa, la <strong>razón corriente</strong> divide los activos corrientes (caja, cuentas por cobrar, inventarios) entre los pasivos corrientes. Si es mayor que 1, en principio puede pagar sus deudas de corto plazo.",
r"En los bancos, la <a href='sbs.html'>SBS</a> exige mantener ratios mínimos de liquidez para que puedan atender retiros sin problemas.",
],
formula=dict(
tex=r"\text{Razón corriente}=\frac{\text{Activo corriente}}{\text{Pasivo corriente}}",
calculo=[r"\frac{150}{100}=1.5"],
),
ejemplo=[
r"Una empresa con S/ 150 mil en activos corrientes y S/ 100 mil en deudas de corto plazo tiene una razón corriente de 1.5.",
],
rel=["liquidez", "riesgo-de-liquidez", "balance-general", "capital-de-trabajo"],
))

# --- Términos del BCRP -----------------------------------------------------

T.append(dict(
slug="sector-publico-no-financiero", t="Sector público no financiero", cat="estado", ic="🏛️",
bcrp="Sector público no financiero", alias="SPNF sector público gobierno general empresas públicas no financieras",
corto="Agrupa al gobierno central, los gobiernos regionales y locales y las empresas públicas que no son financieras; es la base de las cifras fiscales.",
simple=[
r"Cuando se habla del <a href='deficit-fiscal.html'>déficit fiscal</a> del Perú, normalmente se mide para el <strong>sector público no financiero</strong>. Incluye al <a href='gobierno-general.html'>gobierno general</a> (ministerios, regiones, municipios, seguridad social) y a empresas públicas como Petroperú.",
r"Deja fuera a las entidades financieras públicas, como el BCRP, el Banco de la Nación o Cofide, porque su lógica es distinta.",
],
ejemplo=[
r"Si un municipio gasta más de lo que recibe y Petroperú tiene pérdidas, ambos resultados se suman en las cuentas del sector público no financiero.",
],
rel=["gobierno-general", "deficit-fiscal", "empresa-publica", "gobiernos-regionales-y-locales"],
))

T.append(dict(
slug="gobiernos-regionales-y-locales", t="Gobiernos regionales y locales", cat="estado", ic="🗺️",
bcrp="Gobiernos regionales", alias="gobiernos regionales municipalidades descentralización gobiernos subnacionales",
corto="Son los niveles de gobierno de las regiones y de las municipalidades provinciales y distritales, que manejan parte del presupuesto público.",
simple=[
r"En el Perú, el Estado tiene tres niveles: nacional, regional y local. Los <strong>gobiernos regionales</strong> se encargan de temas como salud, educación e infraestructura regional; los <strong>locales</strong> (municipalidades), de limpieza, pistas, mercados y licencias.",
r"Se financian con transferencias del gobierno central, el <a href='canon.html'>canon</a>, el <a href='foncomun.html'>Foncomun</a> y sus propios <a href='impuestos-municipales.html'>impuestos</a>, como el predial.",
],
ejemplo=[
r"Cuando pagas el impuesto predial de tu casa, ese dinero va a tu municipalidad distrital, que lo usa en servicios locales.",
],
rel=["impuestos-municipales", "foncomun", "canon", "sector-publico-no-financiero"],
))

T.append(dict(
slug="preferencia-por-circulante", t="Preferencia por circulante", cat="dinero", ic="💵",
bcrp="Preferencia por circulante", alias="coeficiente de preferencia por circulante efectivo sobre depósitos",
corto="Mide cuánto dinero prefiere la gente tener en efectivo en lugar de depositarlo en el banco.",
simple=[
r"Se calcula como la proporción entre el efectivo en manos del público y sus depósitos. Si es alta, la gente confía poco en los bancos o usa mucho efectivo, por ejemplo por la <a href='informalidad.html'>informalidad</a>.",
r"Influye en el <a href='multiplicador-bancario.html'>multiplicador bancario</a>: cuanto más efectivo guarda la gente, menos pueden prestar los bancos y menor es la creación de dinero.",
],
formula=dict(
tex=r"c=\frac{\text{Circulante}}{\text{Depósitos}}",
calculo=[r"\frac{30}{120}=0.25"],
),
ejemplo=[
r"Si el público tiene S/ 30 mil millones en efectivo y S/ 120 mil millones en depósitos, la preferencia por circulante es 0.25.",
],
rel=["circulante", "multiplicador-bancario", "bancarizacion", "agregados-monetarios"],
))

T.append(dict(
slug="consumo-privado-y-publico", t="Consumo privado y consumo público", cat="produccion", ic="🛍️",
bcrp="Consumo privado", alias="consumo privado consumo público consumo del gobierno demanda interna",
corto="El consumo privado es lo que gastan las familias en bienes y servicios; el consumo público, lo que gasta el Estado en su funcionamiento diario.",
simple=[
r"El <strong>consumo privado</strong> es el componente más grande del <a href='pbi.html'>PBI</a> por el lado del gasto: comida, ropa, transporte, educación, salud, entretenimiento.",
r"El <strong>consumo público</strong> incluye sueldos de maestros, médicos y policías, y la compra de bienes y servicios del Estado. No incluye la <a href='inversion-publica.html'>inversión pública</a>, que se cuenta aparte.",
],
ejemplo=[
r"Cuando una familia paga el menú del día, suma al consumo privado; cuando el Estado paga el sueldo de una enfermera de un hospital público, suma al consumo público.",
],
rel=["consumo", "demanda-interna", "pbi", "inversion-publica"],
))

T.append(dict(
slug="exportaciones-e-importaciones", t="Exportaciones e importaciones", cat="comercio", ic="🚢",
bcrp="Exportación", alias="exportación importación comercio exterior FOB",
corto="Exportar es vender bienes y servicios a otros países; importar es comprarlos del exterior.",
simple=[
r"Las <strong>exportaciones</strong> traen divisas al país: en el Perú destacan el cobre, el oro, la pesca y la agroexportación. Las <strong>importaciones</strong> incluyen bienes de consumo, insumos y bienes de capital, como maquinaria.",
r"La diferencia entre ambas es la <a href='balanza-comercial.html'>balanza comercial</a>. En el cálculo del <a href='pbi.html'>PBI</a> por el lado del gasto, las exportaciones se suman y las importaciones se restan.",
],
formula=dict(
tex=r"\text{PBI}=C+I+G+(X-M)",
donde=[(r"X", "exportaciones"), (r"M", "importaciones")],
calculo=[r"X-M=80-70=10\ \text{mil millones de dólares}"],
),
ejemplo=[
r"Si el Perú exporta 80 mil millones de dólares y importa 70 mil millones en un año, su balanza comercial tiene un superávit de 10 mil millones.",
],
rel=["balanza-comercial", "exportaciones-tradicionales-y-no-tradicionales", "terminos-de-intercambio", "arancel"],
))

T.append(dict(
slug="indice-de-precios-de-exportacion", t="Índice de precios de exportación e importación", cat="comercio", ic="🏷️",
bcrp="Índice de Precios de Exportación", alias="índice de precios de exportación índice de precios de importación términos de intercambio",
corto="Miden cómo cambian, en promedio, los precios de lo que el país vende y compra al exterior.",
simple=[
r"El <strong>índice de precios de exportación</strong> sigue el precio promedio de lo que vendemos (cobre, oro, harina de pescado, uvas…). El de <strong>importación</strong> sigue el de lo que compramos (petróleo, maquinaria, alimentos…).",
r"Al dividir el primero entre el segundo se obtienen los <a href='terminos-de-intercambio.html'>términos de intercambio</a>. El BCRP publica estos índices de forma periódica.",
],
formula=dict(
tex=r"TI=\frac{\text{Índice de precios de exportación}}{\text{Índice de precios de importación}}\times100",
calculo=[r"\frac{110}{100}\times100=110"],
),
ejemplo=[
r"Si los precios de exportación suben 10 % y los de importación no cambian, los términos de intercambio mejoran 10 %: con lo que vendemos podemos comprar más.",
],
herramienta=("Ver precios de metales y alimentos", "../precios/"),
rel=["terminos-de-intercambio", "exportaciones-e-importaciones", "materias-primas", "inflacion-importada"],
))

T.append(dict(
slug="ley-de-say", t="Ley de Say", cat="produccion", ic="🔁",
alias="ley de Say la oferta crea su propia demanda economía clásica",
corto="Es la idea clásica de que «la oferta crea su propia demanda»: producir genera los ingresos con los que se compra lo producido.",
simple=[
r"Jean-Baptiste Say sostenía que no puede haber una sobreproducción general duradera, porque quien produce recibe ingresos y los gasta en otros bienes.",
r"Keynes la criticó en los años treinta: si la gente decide ahorrar en lugar de gastar, la demanda puede quedarse corta y aparecer el desempleo. Ese debate está en la base de la <a href='politica-anticiclica.html'>política anticíclica</a>.",
],
ejemplo=[
r"Según la ley de Say, si un agricultor cosecha más, usará el dinero de su venta para comprar otros productos; según Keynes, podría guardarlo por miedo y frenar la economía.",
],
rel=["demanda-agregada", "oferta-agregada", "multiplicador-keynesiano", "politica-anticiclica"],
))
