// Registro único de los decks del proyecto. Lo consumen build-all.mjs y export-all.mjs.
export const DECKS = [
  { file: 'slides.md',          slug: '',            nombre: 'indice', puerto: 3031 },
  { file: 's1-sintaxis.md',     slug: 's1',          nombre: '1-sintaxis-y-semantica', puerto: 3041 },
  { file: 's2-memoria.md',      slug: 's2',          nombre: '2-memoria-y-ownership', puerto: 3042 },
  { file: 's3-tipos.md',        slug: 's3',          nombre: '3-tipos-propios', puerto: 3043 },
  { file: 's4-colecciones.md',  slug: 's4',          nombre: '4-colecciones-e-iteradores', puerto: 3044 },
  { file: 's5-abstraccion.md',  slug: 's5',          nombre: '5-abstraccion', puerto: 3045 },
  { file: 's6-indireccion.md',  slug: 's6',          nombre: '6-indireccion', puerto: 3046 },
  { file: 's7-proyectos.md',    slug: 's7',          nombre: '7-proyectos', puerto: 3047 },
  { file: 'cheatsheet.md',      slug: 'cheatsheet',  nombre: 'cheatsheet', puerto: 3048 },
  { file: 'apendices.md',       slug: 'apendices',   nombre: 'apendices', puerto: 3049 },
  { file: 'ejercicios.md',      slug: 'ejercicios',  nombre: 'ejercicios', puerto: 3050 },
]
