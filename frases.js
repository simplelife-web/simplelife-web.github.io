/* Base de frases célebres de la portada de Simplelife.
   Cada línea: [ámbito, frase, autor, quién fue, obra o lugar, año, foto de Wikimedia Commons (o "")].
   Solo frases verificadas en la obra, carta o discurso que se cita. Las que no son del español van con traducción propia.
   Las fotos son de dominio público o con licencia libre; si una no carga, se muestran las iniciales.
   Para sumar una frase: copia una línea, cambia sus datos y deja la coma al final. */
window.FRASES = [
  // Ciencia
  ["Ciencia", "La imaginación es más importante que el conocimiento.", "Albert Einstein", "físico, Premio Nobel", "entrevista en The Saturday Evening Post", "1929", "Albert_Einstein_Head.jpg"],
  ["Ciencia", "Si he visto más lejos, es porque estoy sobre hombros de gigantes.", "Isaac Newton", "físico y matemático", "carta a Robert Hooke", "1676", "GodfreyKneller-IsaacNewton-1689.jpg"],
  ["Ciencia", "La vida no es fácil para ninguno de nosotros. Pero ¿qué importa? Hay que tener perseverancia y, sobre todo, confianza en uno mismo.", "Marie Curie", "científica, dos veces Premio Nobel", "carta citada por su hija Eve Curie en Madame Curie", "1937", "Marie_Curie_c1920.jpg"],
  ["Ciencia", "El universo está escrito en lengua matemática.", "Galileo Galilei", "astrónomo y físico", "El ensayador", "1623", "Justus_Sustermans_-_Portrait_of_Galileo_Galilei,_1636.jpg"],
  ["Ciencia", "Hay grandeza en esta concepción de la vida.", "Charles Darwin", "naturalista", "El origen de las especies", "1859", "Charles_Darwin_seated_crop.jpg"],
  ["Ciencia", "En el campo de la observación, el azar solo favorece a la mente preparada.", "Louis Pasteur", "químico y microbiólogo", "discurso en la Universidad de Lille", "1854", ""],
  ["Ciencia", "Todo hombre puede ser, si se lo propone, escultor de su propio cerebro.", "Santiago Ramón y Cajal", "médico, Premio Nobel", "Reglas y consejos sobre investigación científica", "1897", ""],
  ["Ciencia", "Somos una manera de que el cosmos se conozca a sí mismo.", "Carl Sagan", "astrónomo y divulgador", "serie Cosmos, capítulo 1", "1980", ""],
  ["Ciencia", "El primer principio es que no debes engañarte a ti mismo, y tú eres la persona más fácil de engañar.", "Richard Feynman", "físico, Premio Nobel", "discurso en Caltech «Cargo Cult Science»", "1974", ""],
  ["Ciencia", "Recuerda mirar hacia las estrellas y no hacia tus pies.", "Stephen Hawking", "físico teórico", "entrevista en la cadena ABC", "2010", ""],
  ["Ciencia", "La ciencia y la vida cotidiana no pueden ni deben separarse.", "Rosalind Franklin", "química, pionera del estudio del ADN", "carta a su padre", "c. 1940", ""],
  ["Ciencia", "Dadme un punto de apoyo y moveré el mundo.", "Arquímedes", "matemático e inventor griego", "según Papo de Alejandría, Colección matemática", "siglo III a. C.", ""],
  ["Tecnología", "La Máquina Analítica teje patrones algebraicos tal como el telar de Jacquard teje flores y hojas.", "Ada Lovelace", "matemática, pionera de la programación", "notas a la traducción del artículo de Menabrea", "1843", "Ada_Lovelace_portrait.jpg"],
  ["Tecnología", "Solo podemos ver un poco del futuro, pero lo suficiente para darnos cuenta de que hay mucho que hacer.", "Alan Turing", "matemático, padre de la informática", "Computing Machinery and Intelligence", "1950", ""],
  ["Tecnología", "El genio es un uno por ciento de inspiración y un noventa y nueve por ciento de transpiración.", "Thomas Edison", "inventor", "declaración recogida por la prensa", "c. 1903", ""],
  ["Tecnología", "Sigan hambrientos, sigan alocados.", "Steve Jobs", "cofundador de Apple", "discurso en la Universidad de Stanford", "2005", ""],
  ["Tecnología", "Esto es para todos.", "Tim Berners-Lee", "creador de la World Wide Web", "ceremonia de los Juegos Olímpicos de Londres", "2012", ""],

  // Perú
  ["Historia del Perú", "El Perú es desde este momento libre e independiente por la voluntad general de los pueblos y por la justicia de su causa que Dios defiende.", "José de San Martín", "libertador del Perú", "proclamación de la Independencia, Lima", "1821", "Portrait_of_General_José_de_San_Martín_(1818).jpg"],
  ["Historia del Perú", "Tengo deberes sagrados que cumplir y los cumpliré hasta quemar el último cartucho.", "Francisco Bolognesi", "héroe de la batalla de Arica", "respuesta al pedido de rendición, Arica", "1880", ""],
  ["Historia del Perú", "Los viejos a la tumba, los jóvenes a la obra.", "Manuel González Prada", "escritor y pensador peruano", "discurso en el teatro Politeama, Lima", "1888", ""],
  ["Literatura peruana", "Hay golpes en la vida, tan fuertes... ¡Yo no sé!", "César Vallejo", "poeta peruano", "Los heraldos negros", "1918", "Cesar_vallejo_1929.jpg"],
  ["Literatura peruana", "Aprendí a leer a los cinco años [...]. Es la cosa más importante que me ha pasado en la vida.", "Mario Vargas Llosa", "escritor peruano, Premio Nobel", "discurso del Nobel «Elogio de la lectura y la ficción»", "2010", "Mario_Vargas_Llosa_(crop_2).jpg"],
  ["Literatura peruana", "Yo no soy un aculturado; yo soy un peruano que orgullosamente, como un demonio feliz, habla en cristiano y en indio, en español y en quechua.", "José María Arguedas", "escritor y antropólogo peruano", "discurso «No soy un aculturado»", "1968", ""],

  // Literatura
  ["Literatura", "El que lee mucho y anda mucho, ve mucho y sabe mucho.", "Miguel de Cervantes", "escritor", "Don Quijote de la Mancha, segunda parte", "1615", "Cervantes_Jáuregui.jpg"],
  ["Literatura", "La libertad, Sancho, es uno de los más preciosos dones que a los hombres dieron los cielos.", "Miguel de Cervantes", "escritor", "Don Quijote de la Mancha, segunda parte", "1615", "Cervantes_Jáuregui.jpg"],
  ["Literatura", "Ser o no ser, esa es la cuestión.", "William Shakespeare", "dramaturgo y poeta", "Hamlet", "c. 1600", "Shakespeare.jpg"],
  ["Literatura", "La vida no es la que uno vivió, sino la que uno recuerda y cómo la recuerda para contarla.", "Gabriel García Márquez", "escritor colombiano, Premio Nobel", "Vivir para contarla", "2002", ""],
  ["Literatura", "Yo, que me figuraba el Paraíso bajo la especie de una biblioteca.", "Jorge Luis Borges", "escritor argentino", "Poema de los dones", "1960", ""],
  ["Literatura", "Caminante, no hay camino, se hace camino al andar.", "Antonio Machado", "poeta español", "Campos de Castilla", "1912", ""],
  ["Literatura", "Lo esencial es invisible a los ojos.", "Antoine de Saint-Exupéry", "escritor y aviador", "El principito", "1943", ""],
  ["Literatura", "Todas las familias felices se parecen; cada familia infeliz lo es a su manera.", "León Tolstói", "escritor ruso", "Ana Karénina", "1877", ""],
  ["Literatura", "Era el mejor de los tiempos, era el peor de los tiempos.", "Charles Dickens", "escritor inglés", "Historia de dos ciudades", "1859", ""],
  ["Literatura", "Juventud, divino tesoro, ¡ya te vas para no volver!", "Rubén Darío", "poeta nicaragüense", "Canción de otoño en primavera", "1905", ""],
  ["Literatura", "Puedo escribir los versos más tristes esta noche.", "Pablo Neruda", "poeta chileno, Premio Nobel", "Veinte poemas de amor y una canción desesperada", "1924", ""],
  ["Literatura", "Hombres necios que acusáis a la mujer sin razón, sin ver que sois la ocasión de lo mismo que culpáis.", "Sor Juana Inés de la Cruz", "poeta mexicana", "Redondillas", "1689", ""],
  ["Literatura", "El amor que mueve el sol y las demás estrellas.", "Dante Alighieri", "poeta italiano", "La Divina Comedia, Paraíso", "c. 1320", ""],

  // Filosofía
  ["Filosofía", "El ser humano es por naturaleza un animal político.", "Aristóteles", "filósofo griego", "Política, libro I", "siglo IV a. C.", "Aristotle_Altemps_Inv8575.jpg"],
  ["Filosofía", "Una vida sin examen no merece ser vivida.", "Sócrates", "filósofo griego", "según Platón, Apología de Sócrates", "siglo IV a. C.", ""],
  ["Filosofía", "No es posible bañarse dos veces en el mismo río.", "Heráclito", "filósofo griego", "fragmento citado por Plutarco", "siglo V a. C.", ""],
  ["Filosofía", "Aprender sin pensar es inútil; pensar sin aprender es peligroso.", "Confucio", "filósofo chino", "Analectas, libro II", "siglo V a. C.", ""],
  ["Filosofía", "Un viaje de mil li comienza con un paso.", "Lao-Tse", "filósofo chino", "Tao Te Ching, capítulo 64", "siglo IV a. C.", ""],
  ["Filosofía", "No es que tengamos poco tiempo, sino que perdemos mucho.", "Séneca", "filósofo romano", "Sobre la brevedad de la vida", "c. 49", ""],
  ["Filosofía", "Tal como sean tus pensamientos habituales, así será tu mente.", "Marco Aurelio", "emperador y filósofo romano", "Meditaciones, libro V", "siglo II", ""],
  ["Filosofía", "No nos perturban las cosas, sino las opiniones que tenemos de ellas.", "Epicteto", "filósofo estoico", "Enquiridión", "siglo II", ""],
  ["Filosofía", "Pienso, luego existo.", "René Descartes", "filósofo y matemático", "Discurso del método", "1637", "Frans_Hals_-_Portret_van_René_Descartes.jpg"],
  ["Filosofía", "El corazón tiene razones que la razón no conoce.", "Blaise Pascal", "filósofo y matemático", "Pensamientos", "1670", ""],
  ["Filosofía", "¡Ten el valor de servirte de tu propio entendimiento!", "Immanuel Kant", "filósofo", "¿Qué es la Ilustración?", "1784", "Immanuel_Kant_(painted_portrait).jpg"],
  ["Filosofía", "El hombre nace libre, y en todas partes está encadenado.", "Jean-Jacques Rousseau", "filósofo", "El contrato social", "1762", ""],
  ["Filosofía", "Hay que cultivar nuestro jardín.", "Voltaire", "escritor y filósofo", "Cándido", "1759", ""],
  ["Filosofía", "Quien tiene un porqué para vivir puede soportar casi cualquier cómo.", "Friedrich Nietzsche", "filósofo", "Crepúsculo de los ídolos", "1889", ""],
  ["Filosofía", "Yo soy yo y mi circunstancia.", "José Ortega y Gasset", "filósofo español", "Meditaciones del Quijote", "1914", ""],
  ["Filosofía", "No se nace mujer: se llega a serlo.", "Simone de Beauvoir", "filósofa y escritora", "El segundo sexo", "1949", ""],
  ["Filosofía", "El valor de un Estado, a la larga, es el valor de las personas que lo componen.", "John Stuart Mill", "filósofo y economista", "Sobre la libertad", "1859", "John_Stuart_Mill_by_London_Stereoscopic_Company,_c1870.jpg"],

  // Política e historia
  ["Política", "La educación es el arma más poderosa que puedes usar para cambiar el mundo.", "Nelson Mandela", "presidente de Sudáfrica, Premio Nobel de la Paz", "discurso en Johannesburgo", "2003", "Nelson_Mandela_1994.jpg"],
  ["Política", "Que el gobierno del pueblo, por el pueblo y para el pueblo no desaparezca de la Tierra.", "Abraham Lincoln", "presidente de Estados Unidos", "discurso de Gettysburg", "1863", "Abraham_Lincoln_O-77_matte_collodion_print.jpg"],
  ["Derechos civiles", "Tengo un sueño: que mis cuatro hijos pequeños vivirán un día en una nación donde no serán juzgados por el color de su piel, sino por su carácter.", "Martin Luther King Jr.", "líder de los derechos civiles, Premio Nobel de la Paz", "discurso «Tengo un sueño», Washington", "1963", "Martin_Luther_King,_Jr..jpg"],
  ["Derechos humanos", "Un niño, un maestro, un libro y una pluma pueden cambiar el mundo.", "Malala Yousafzai", "activista, Premio Nobel de la Paz", "discurso en las Naciones Unidas", "2013", ""],
  ["Política", "Entre los individuos, como entre las naciones, el respeto al derecho ajeno es la paz.", "Benito Juárez", "presidente de México", "manifiesto a la nación", "1867", ""],
  ["Política", "Moral y luces son nuestras primeras necesidades.", "Simón Bolívar", "libertador", "discurso de Angostura", "1819", ""],
  ["Política", "Nunca en el campo de los conflictos humanos tantos debieron tanto a tan pocos.", "Winston Churchill", "primer ministro británico", "discurso en la Cámara de los Comunes", "1940", ""],
  ["Política", "No preguntes qué puede hacer tu país por ti; pregunta qué puedes hacer tú por tu país.", "John F. Kennedy", "presidente de Estados Unidos", "discurso de investidura", "1961", ""],
  ["Política", "Lo único que debemos temer es al miedo mismo.", "Franklin D. Roosevelt", "presidente de Estados Unidos", "discurso de investidura", "1933", ""],

  // Arte y música
  ["Arte", "Pies, ¿para qué los quiero si tengo alas pa' volar?", "Frida Kahlo", "pintora mexicana", "su diario", "1953", "Frida_Kahlo,_by_Guillermo_Kahlo.jpg"],
  ["Arte", "¿Qué sería de la vida si no tuviéramos el valor de intentar algo?", "Vincent van Gogh", "pintor", "carta a su hermano Theo", "1881", ""],
  ["Cine", "Pensamos demasiado y sentimos muy poco.", "Charles Chaplin", "actor y director de cine", "discurso final de El gran dictador", "1940", ""],
  ["Música", "Gracias a la vida, que me ha dado tanto.", "Violeta Parra", "cantautora chilena", "canción «Gracias a la vida»", "1966", ""],
  ["Música", "La vida es lo que te pasa mientras estás ocupado haciendo otros planes.", "John Lennon", "músico, integrante de The Beatles", "canción «Beautiful Boy»", "1980", ""],

  // Deporte
  ["Deporte", "Flota como una mariposa, pica como una abeja.", "Muhammad Ali", "boxeador, campeón mundial", "antes de su pelea con Sonny Liston", "1964", "Muhammad_Ali_NYWTS.jpg"],
  ["Deporte", "He fallado una y otra vez en mi vida. Y por eso tengo éxito.", "Michael Jordan", "basquetbolista, seis veces campeón de la NBA", "comercial de Nike «Failure»", "1997", ""],
  ["Deporte", "Lo importante en la vida no es el triunfo, sino la lucha.", "Pierre de Coubertin", "fundador de los Juegos Olímpicos modernos", "discurso en Londres", "1908", ""],
  ["Deporte", "La presión es un privilegio.", "Billie Jean King", "tenista, campeona de Wimbledon", "libro Pressure Is a Privilege", "2008", ""],

  // Economía
  ["Economía", "Ninguna sociedad puede ser floreciente y feliz si la mayor parte de sus miembros son pobres y miserables.", "Adam Smith", "economista", "La riqueza de las naciones", "1776", "Adam_Smith_The_Muir_portrait.jpg"],
  ["Economía", "No es de la benevolencia del carnicero, del cervecero o del panadero de donde esperamos nuestra cena, sino de su propio interés.", "Adam Smith", "economista", "La riqueza de las naciones", "1776", "Adam_Smith_The_Muir_portrait.jpg"],
  ["Economía", "La economía es el estudio de la humanidad en los asuntos ordinarios de la vida.", "Alfred Marshall", "economista", "Principios de economía", "1890", "Alfred_Marshall.jpg"],
  ["Economía", "Recuerda que el tiempo es dinero.", "Benjamin Franklin", "inventor y político", "Consejos a un joven comerciante", "1748", "Joseph_Siffrein_Duplessis_-_Benjamin_Franklin_-_Google_Art_Project.jpg"],
  ["Economía", "A largo plazo, todos estaremos muertos.", "John Maynard Keynes", "economista", "Breve tratado sobre la reforma monetaria", "1923", ""],
  ["Economía", "La dificultad no está en las ideas nuevas, sino en escapar de las viejas.", "John Maynard Keynes", "economista", "Teoría general del empleo, el interés y el dinero", "1936", ""],
  ["Economía", "Este proceso de destrucción creativa es el hecho esencial del capitalismo.", "Joseph Schumpeter", "economista", "Capitalismo, socialismo y democracia", "1942", ""],
  ["Economía", "La inflación es siempre y en todas partes un fenómeno monetario.", "Milton Friedman", "economista, Premio Nobel", "Inflation: Causes and Consequences", "1963", ""],
  ["Economía", "El curioso cometido de la economía es demostrar a los hombres lo poco que saben sobre lo que imaginan que pueden diseñar.", "Friedrich Hayek", "economista, Premio Nobel", "La fatal arrogancia", "1988", ""],
  ["Economía", "El desarrollo puede concebirse como un proceso de expansión de las libertades reales de que disfrutan los individuos.", "Amartya Sen", "economista, Premio Nobel", "Desarrollo y libertad", "1999", ""],
  ["Economía", "Se puede ver la era de las computadoras en todas partes, menos en las estadísticas de productividad.", "Robert Solow", "economista, Premio Nobel", "reseña en The New York Times Book Review", "1987", ""],
  ["Economía", "El precio es lo que pagas; el valor es lo que obtienes.", "Warren Buffett", "inversionista", "carta a los accionistas de Berkshire Hathaway", "2008", ""]
];
