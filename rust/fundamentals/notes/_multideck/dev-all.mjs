#!/usr/bin/env node
// Levanta todos los decks a la vez, cada uno en su puerto.
// El índice queda en 3031 y sus enlaces apuntan a los demás.
import { spawn } from 'node:child_process'
import { DECKS } from './decks.mjs'

console.log('\nDecks:')
for (const d of DECKS) console.log(`  http://localhost:${d.puerto}/  ${d.slug || '(índice)'}`)
console.log('\nCtrl-C para detener todos.\n')

const hijos = DECKS.map(d =>
  spawn('npx', ['slidev', d.file, '--port', String(d.puerto)], { stdio: 'inherit', shell: false })
)
const matar = () => { for (const h of hijos) h.kill('SIGINT'); process.exit(0) }
process.on('SIGINT', matar)
process.on('SIGTERM', matar)
