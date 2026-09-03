#!/usr/bin/env node
// Exporta cada deck a su propio PDF en exports/.
// Reemplaza a export-sections.py: al ser decks independientes ya no hace falta
// exportar el deck completo y partirlo con pypdf para esquivar el bug de --range.
import { execSync } from 'node:child_process'
import { mkdirSync } from 'node:fs'
import { DECKS } from './decks.mjs'

mkdirSync('exports', { recursive: true })
const soloEste = process.argv[2]
const objetivo = soloEste ? DECKS.filter(d => d.slug === soloEste || d.file === soloEste) : DECKS

for (const { file, nombre } of objetivo) {
  console.log(`\n▸ ${file} → exports/${nombre}.pdf`)
  execSync(`npx slidev export ${file} --output exports/${nombre}.pdf`, { stdio: 'inherit' })
}
