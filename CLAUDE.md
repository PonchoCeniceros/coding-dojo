# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

**Academia Jedi** is a personal competitive programming and language-learning training ground. Solutions exist in two languages: Python and Rust. Each problem is called a "Trial" and is identified by its LeetCode problem ID. The repository uses automation scripts called "Holocrons" to scaffold, test, and organize work.

The repo is organized **language-first**. Within Rust there are two tracks: `fundamentals/` (mastering the language via algorithms) and `building/` (applied projects — APIs, data analysis).

## Repository Structure

```
rust/
├── fundamentals/           # Mastering the language
│   ├── notes/              # "Rust · Cuaderno de campo" — Slidev, ONE deck.
│   │   ├── slides.md       # Entry point; includes pages/ via `src:`
│   │   ├── export-sections.py  # One PDF per section (splits the deck) + standalone decks
│   │   ├── sync-indice.py  # Re-syncs the TOC's slide numbers. RUN AFTER EDITING pages/
│   │   ├── ejercicios.md   # Standalone deck: 56 exercises (its own PDF, not in slides.md)
│   │   ├── GUIA-DE-TONO.md # Writing/tone rules for the deck — READ BEFORE EDITING
│   │   ├── _multideck/     # Abandoned per-section entry files. Safe to delete.
│   │   └── pages/          # Numbered by section (topological order, see below):
│   │                       # 1.1-tokens.md … 7.4-errores-idiomaticos.md,
│   │                       # ap0-cheatsheet.md, ap2-aplicacion.md, ejercicios.md
│   └── trials/             # Cargo package "katas" (LeetCode in Rust)
│       ├── Cargo.toml
│       ├── holocron.sh     # Scaffolds/tests/runs trials
│       └── src/
│           ├── lib.rs      # `mod macros;`
│           ├── macros.rs   # exports the `s!` macro
│           └── bin/{ID}_{name}.rs   # one binary per trial (34)
└── building/               # Applied Cargo projects — planned. No separate
                             # slide deck; concepts live in fundamentals/notes
                             # (prefix F) — only per-project crate details
                             # belong here, in that project's own README
python/
├── trials/                 # Python solutions (pytest-based, 21)
│   ├── {ID}.py             # Solution file with tests
│   └── {ID}/main.py        # (Optional) Multi-file trials
├── utils/                  # log.py — logging helper used in tests
└── holocron.sh             # Scaffolds/tests Python trials
docs/whiteboards/           # Cross-language sketches
roadmap.csv                 # Problem metadata + progress (spans both languages)
pytest.ini                  # Stays at root — see "Python Setup"
```

## Development Workflow

Both holocrons resolve their own location, so they work from the repo root **or** from their own directory.

### Python Path (pytest)

**Create a new trial:**
```bash
python/holocron.sh -m "9. Palindrome Number"
```
Creates `python/trials/9.py` with test scaffold.

**Run tests for a trial:**
```bash
python/holocron.sh -t 9
```
Or directly:
```bash
pytest python/trials/9.py -v
```

**List all completed trials:**
```bash
python/holocron.sh -l
```

**Run all Python tests:**
```bash
pytest
```

### Rust Path (cargo)

**Create a new trial:**
```bash
rust/fundamentals/trials/holocron.sh -m "1. Two Sum"
```
Creates `rust/fundamentals/trials/src/bin/1_two_sum.rs` with test scaffold.

**Run tests for a trial:**
```bash
rust/fundamentals/trials/holocron.sh -t 1
```
Or directly:
```bash
cargo test --manifest-path rust/fundamentals/trials/Cargo.toml --bin 1_two_sum
```

**Execute trial main function:**
```bash
rust/fundamentals/trials/holocron.sh -r 1
```

**Run all Rust tests:**
```bash
cargo test --manifest-path rust/fundamentals/trials/Cargo.toml
```

**List all completed trials:**
```bash
rust/fundamentals/trials/holocron.sh -l
```

### Study deck (Slidev)

```bash
pnpm --dir rust/fundamentals/notes run dev
```
One deck, ~296 slides (called *láminas* in the deck's own language), served whole on port 3031, plus a standalone `ejercicios.md`
(114 slides) that is exported separately. The split into sections happens only at
PDF export time: `pnpm export:sections` produces one PDF per section in `exports/`.
The deck's TOC links to slide numbers, so **run `python3 sync-indice.py` after
adding, removing or reordering any page** or the links go stale. Also available as the `rust-notes` config in `.claude/launch.json`.

### Learning line (topological)

Sections are ordered so that nothing is used before it is explained:
`1 Fundamentos` (tokens, escalares, variables, expresiones, funciones, control de
flujo) · `2 Tipos compuestos` (tuplas/arreglos, structs *sin métodos*, enums,
patrones) · `3 Memoria` (stack/heap, ownership, borrowing, impl y métodos,
lifetimes) · `4 Abstracciones de costo cero` (traits, generics, closures) · `5 Vocabulario
stdlib` (Option, Result, Vec, HashMap, otras colecciones, iteradores) ·
`6 Indirección` (Box, Rc/RefCell, dyn) · `7 Proyectos` (módulos, Cargo, tests,
errores, I/O, macros) · `8 Concurrencia` (hilos, Send/Sync, Arc/Mutex, canales,
rayon) · `9 Async` (async/await, Future, runtime, Send en tareas).

Sections 8 and 9 close the fundamentals for the applied tracks the user is heading
into: web APIs, databases, Polars, parallel compute. Async is taught at the language
level only — the runtime (tokio) and frameworks belong in `rust/building/`.

Consequences worth knowing before editing: **`impl`/methods are split from `struct`**
(datos in 2.2, métodos in 3.4, because `&self` is a borrow); **traits come before
generics** (bounds are traits); and the two "ya lo viste" tables in 4.1/4.2 are now
**forward maps** ("dónde vas a encontrarlos"). Two forward references are declared
explicitly in 1.2 and allowed everywhere: string literals (`&str`) and `String`.
Adding a page? Check nothing it uses is introduced later.

A per-section multi-deck layout was tried and reverted: reading the notes wants one
continuous deck, and only the PDFs need to be separate. The abandoned entry files
are in `_multideck/`.

## Key Technical Details

### Python Setup
- Uses **pytest** for testing with parametrize decorators
- Tests in same file as solution (at bottom of `{ID}.py`)
- Imports `utils.log.Log` for standardized logging (optional but available)
- `python/` is on `PYTHONPATH` (via `pythonpath = python` in `pytest.ini`), which is what makes `from utils.log import Log` resolve
- **`pytest.ini` deliberately stays at the repo root.** If moved into `python/`, running `pytest` from the root would let the root `pyproject.toml` win as rootdir and silently discard all config. At the root it behaves identically from either directory.
- venv at `.venv/` (pyright configured to use it)

### Rust Setup
- Single Cargo **package** (`katas`, not a workspace) in `rust/fundamentals/trials/` with edition `2024`
- Each solution is a separate binary: `cargo run --bin {ID}_{name}`
- Dependencies available: `regex`, `colored`
- Tests embedded in binary via `#[cfg(test)]` modules
- Common utilities imported via `use katas::s;` (internal crate reference)

### Test Conventions
- **Python**: Use `@pytest.mark.parametrize` with tuples of (input, expected)
- **Rust**: Use `#[test]` fn with loop over test cases, `assert_eq!` macro, print errors with `.red().italic().underline()`

## Common Commands

| Task | Command |
|------|---------|
| Create Python trial | `python/holocron.sh -m "{ID}. Problem Name"` |
| Create Rust trial | `rust/fundamentals/trials/holocron.sh -m "{ID}. Problem Name"` |
| Test Python solution | `python/holocron.sh -t {ID}` or `pytest python/trials/{ID}.py -v` |
| Test Rust solution | `rust/fundamentals/trials/holocron.sh -t {ID}` |
| Run Rust binary | `rust/fundamentals/trials/holocron.sh -r {ID}` |
| Test all Python | `pytest` |
| Test all Rust | `cargo test --manifest-path rust/fundamentals/trials/Cargo.toml` |
| Serve study deck | `pnpm --dir rust/fundamentals/notes run dev` |
| One PDF per section | `pnpm --dir rust/fundamentals/notes run export:sections` |

## Code Philosophy

Per the README philosophy:
1. **Clarity over cleverness** — solutions must be readable
2. **Continuous refinement** — a trial is only "mastered" when no further simplification is possible
3. **Process-driven** — each failed test is a lesson; solutions should flow naturally when mastered

## Important Files
- `python/holocron.sh` — scaffolds and runs Python trials
- `rust/fundamentals/trials/holocron.sh` — scaffolds and runs Rust trials
- `roadmap.csv` — tracks problem metadata and progress (spans both languages, hence at root)
- `pytest.ini` — pytest configuration (testpaths, pythonpath, logging)
- `rust/fundamentals/trials/Cargo.toml` — Rust package config
- `rust/fundamentals/notes/slides.md` — study deck entry point (the only one)
- `rust/fundamentals/notes/GUIA-DE-TONO.md` — tone rules for the decks; read it before writing or editing any page

## Notes for Future Sessions
- Both language paths run independently; no requirement to do both
- LeetCode problem IDs are used consistently across both paths
- Rust edition 2024 is explicitly set in Cargo.toml (non-standard; verify compatibility when upgrading)
- Test scaffold filenames follow the pattern: Python uses `test_{function_name}`, Rust uses `test_{package_name}`
- The Slidev deck's images use root-absolute paths (`/images/...`) served from `notes/public`; its page includes use `./pages/...`. Both are internal, so the deck can be moved as a unit.
- In Slidev pages, sibling `<div>`s containing markdown need blank lines around them, or the build fails with `Element is missing end tag`.
- `rust/building/notes` (a separate "Rust Aplicado" deck) was merged into `rust/fundamentals/notes` as the `F0X` pages (Módulos, Crates y Cargo) — there is now a single Slidev deck for all of Rust. `rust/building/` keeps only future Cargo projects.
- `slidev export --range "X-Y"` silently produces blank-page PDFs/PNGs in this Slidev version (Playwright rendering bug). `export-sections.py` works around it by exporting the full deck once and splitting the result with `pypdf`, verifying each PDF's content streams aren't suspiciously small before trusting the output. It was updated for the new numbering: sections are keyed `0`–`7`, `cheat`, `ap`, `ej` (see `section_key()`).
- The deck was split and reordered on 2026-08-31: `A01`…`Z02` became `1.1`…`7.4` plus appendices, `B02` was split into `2.3-borrowing.md` and `2.4-lifetimes.md`, and nine placeholder pages were created for content that does not exist yet (`1.1`, `1.3`, `1.6`, `2.5`, `4.4`, `5.3`, `7.3`, `7.4`, `0-por-que-rust`). Originals kept as `pages/_B02-original.md.bak` and `pages/_Z01-original.md.bak`.

## Failing tests (pre-existing; unrelated to the language-first refactor)

`cargo test` is **fail-fast**: a single failing target stops the run, so use
`--no-fail-fast` to see the whole picture. Four targets fail today:

| Trial | Symptom | Likely cause |
|---|---|---|
| 241 Different Ways to Add Parentheses | `[]` vs `[11]` | real bug: single-number input returns nothing |
| 347 Top K Frequent Elements | `[2, 1]` vs `[1, 2]` | **order only** — the answer is right; the test asserts an exact order that LeetCode doesn't require |
| 49 Group Anagrams | groups right, order differs | **order only** — same as above, at both the group and element level |
| 48 Rotate Image | panics at `48_rotate_image.rs:86` | needs a look (no left/right in the assert output) |

All four are marked `ya_en_rust=Si` in `roadmap.csv`. They stayed invisible for a
while because a compile error in 241 aborted the suite before reaching them.

`python/trials/888.py` also has one failing parametrized case
(`test_fairCandySwap[...expected1]`).

## Environment gotcha

The `.venv/bin/*` console scripts have a dead shebang pointing at
`/Users/giovannychavez/developments/...` (plural) while the repo lives at
`.../development/...` — the venv was built before the repo moved. So invoking
bare `pytest` fails even with the venv activated. Use `.venv/bin/python -m
pytest` (which is what `python/holocron.sh` does), or recreate the venv from
`requeriments.txt`.
