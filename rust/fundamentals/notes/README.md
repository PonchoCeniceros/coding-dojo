# Rust · Cuaderno de campo

Apuntes del lenguaje Rust, hechos con [Slidev](https://github.com/slidevjs/slidev).
**~300 láminas · 9 secciones · 56 ejercicios.**

Un cuaderno de campo se escribe mientras se trabaja y se consulta en el campo: esto
sirve para aprender en orden y para buscar algo a media tarea.

Por **Giovanny Alfonso Chávez Ceniceros**, con **Claude**. Las páginas de ownership,
borrowing y lifetimes son suyas de origen, y de ahí salió la guía de tono con la que
está escrito el resto; el orden topológico, la partición en secciones y las decisiones
de contenido se discutieron a cuatro manos.

## Cómo está ordenado

Las secciones siguen un **orden topológico**: nada se usa antes de explicarse. Es la
restricción que decide dónde vive cada tema, y tiene tres consecuencias que conviene
saber antes de editar.

- `impl` y los métodos están **separados** de `struct` (datos en 2.2, métodos en 3.4),
  porque `&self` es un préstamo.
- **Traits van antes que generics**, porque los *trait bounds* son traits.
- `Option` y `Result` viven en la sección 5, después de enums y de genéricos, que es
  lo que necesitan para explicarse.

Solo hay **dos referencias hacia adelante**, y están declaradas en 1.2: los literales
de texto (`&str`) y `String`. No se pueden evitar sin volver irreales los ejemplos.

| | Sección | Páginas |
| :--- | :--- | :--- |
| **1** | Fundamentos | tokens · tipos escalares · variables · todo es una expresión · funciones · control de flujo |
| **2** | Tipos compuestos | tuplas y arreglos · structs · enums · patrones |
| **3** | Memoria | stack y heap · ownership · borrowing · strings · impl y métodos · lifetimes · mapa de la sección |
| **4** | Abstracciones de costo cero | traits · generics · closures · traits de la stdlib |
| **5** | Vocabulario de la stdlib | Option · Result y `?` · Vec · HashMap y HashSet · otras colecciones · iteradores · iteradores a fondo |
| **6** | Indirección | Box y listas enlazadas · Rc, RefCell y árboles · despacho dinámico |
| **7** | Proyectos | módulos · crates y Cargo · tests · errores idiomáticos · entrada y salida · macros y atributos |
| **8** | Concurrencia | hilos · Send y Sync · Arc y Mutex · canales · paralelismo de datos |
| **9** | Async | el problema · async, await y Future · el runtime · Send en las tareas · async o hilos |

El **cheatsheet** y los **apéndices** (aplicación a los trials de LeetCode) están
comentados al final de `slides.md`. Para reactivarlos hay que quitar el comentario y
devolver los separadores `---` a la columna 0.

Las secciones **8 y 9** cierran los fundamentos de cara al desarrollo aplicado: son
el prerrequisito de APIs web, bases de datos y Polars. Async se cubre a nivel de
lenguaje —`async`, `.await`, `Future`, `Send`—; el runtime (`tokio`) y los
frameworks van en `rust/building/`.

Los **56 ejercicios** con respuesta son un deck aparte (`ejercicios.md`) y se exportan
a su propio PDF. Cubren las secciones 1 y 3; el resto todavía no tiene ejercicios.

## Correr

```bash
pnpm install
pnpm dev          # http://localhost:3031
```

## Comandos

| | |
| :--- | :--- |
| `pnpm dev` | servidor de desarrollo con recarga en caliente |
| `pnpm build` | sitio estático en `dist/` |
| `pnpm export` | el deck completo en un PDF |
| `pnpm export:sections` | **un PDF por sección** en `exports/` |
| `pnpm indice` | resincroniza los números de diapositiva del índice |
| `pnpm densidad` | lista las diapositivas saturadas (regla R11) |

`pnpm export:sections 3 5` exporta solo las secciones pedidas.

## Antes de editar

1. **Lee `GUIA-DE-TONO.md`.** Son once reglas destiladas de estas mismas páginas:
   sin raya larga como bisagra retórica, títulos en mayúscula inicial, tercera
   persona, una negrita por viñeta, y una diapositiva por elemento pesado.
2. **Respeta el orden topológico.** Si una página nueva usa algo que se explica
   después, o se mueve la página, o se marca la referencia explícitamente.
3. **Corre `pnpm indice`** después de agregar, quitar o reordenar cualquier página:
   los enlaces del índice apuntan a números de diapositiva y se desfasan solos.
4. **Corre `pnpm densidad`** antes de dar una página por terminada.

## Estructura

```
notes/
├── slides.md              punto de entrada; incluye pages/ vía `src:`
├── ejercicios.md          deck aparte, con su propio PDF
├── pages/                 una página por tema, numerada por sección
├── style.css              tema y componentes (cp-*)
├── GUIA-DE-TONO.md        reglas de escritura
├── export-sections.py     parte el PDF exportado en uno por sección
├── sync-indice.py         resincroniza los enlaces del índice
└── revisar-densidad.py    detector de diapositivas saturadas
```

Los archivos que empiezan con `_` están retirados y los scripts los ignoran.

## Notas técnicas

- `slidev export --range` genera PDFs en blanco en esta versión (bug de Playwright).
  `export-sections.py` lo esquiva exportando el deck completo una vez y partiéndolo
  con `pypdf`, verificando que las páginas traigan texto antes de darlas por buenas.
  Requiere `pip install --user pypdf`.
- Las cercas de código dentro de un `<div>` deben abrir y cerrar con la **misma
  indentación**. Si no, Slidev no cierra el bloque y se come las diapositivas
  siguientes, sin error visible.
- Los bloques de código de las páginas se verifican compilándolos con `rustc`. Los
  que fallan a propósito traen su código `E0xxx` en la nota de al lado.
- Los ejemplos de las secciones 8 y 9 que usan `rayon` o `tokio` se verificaron en un
  proyecto cargo aparte con esos crates instalados, no solo a ojo.
