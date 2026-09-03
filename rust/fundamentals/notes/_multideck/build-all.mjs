#!/usr/bin/env node
// Compila cada deck a dist/<slug>/. El índice va en la raíz de dist/.
// El índice se compila primero porque `slidev build` limpia su directorio de salida.
import { execSync } from 'node:child_process'
import { DECKS } from './decks.mjs'

const soloEste = process.argv[2]
const objetivo = soloEste ? DECKS.filter(d => d.slug === soloEste || d.file === soloEste) : DECKS
if (!objetivo.length) {
  console.error(`No hay ningún deck con slug "${soloEste}". Opciones: ${DECKS.map(d => d.slug || '(índice)').join(', ')}`)
  process.exit(1)
}

for (const { file, slug } of objetivo) {
  const base = slug ? `/${slug}/` : '/'
  const out = slug ? `dist/${slug}` : 'dist'
  console.log(`\n▸ ${file} → ${out} (base ${base})`)
  execSync(`npx slidev build ${file} --base ${base} --out ${out}`, { stdio: 'inherit' })
}
