---
theme: apple-basic
layout: intro
fonts:
  sans: Work Sans
  local: Work Sans
  mono: JetBrains Mono
---

# Rust Fundamentos
Notas de estudio

<div class="absolute bottom-10">
  <span class="font-700">
    Giovanny Alfonso Chávez Ceniceros
  </span>
</div>

---
layout: intro-image
---

<div class="absolute inset-0 cp-cover"></div>

<div class="absolute top-10 z-2">
  <span class="font-700 cp-cover-text">
    Giovanny Alfonso Chávez Ceniceros
  </span>
</div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Rust Fundamentos</h1>
  <p class="cp-cover-text">Notas de estudio</p>
</div>

---
layout: center
---

# Contenido

<div class="grid grid-cols-3 gap-x-10 mt-6 text-left">

  <div>
    <h2 class="text-xl cp-toc-title">
      1. Sintaxis y Semántica
    </h2>
    <ul class="space-y-3 list-none pl-0 text-sm">
      <li><span class="cp-muted font-mono">1.1</span> Tokens</li>
      <li><span class="cp-muted font-mono">1.2</span> Tipos de Dato</li>
      <li><span class="cp-muted font-mono">1.3</span> Estructuras de Control</li>
      <li><span class="cp-muted font-mono">1.4</span> Tipos de Memoria</li>
      <li><span class="cp-muted font-mono">1.5</span> Funciones</li>
    </ul>
  </div>

  <div>
    <h2 class="text-xl cp-toc-title">
      2. Memory Safety
    </h2>
    <ul class="space-y-3 list-none pl-0 text-sm">
      <li><span class="cp-muted font-mono">2.1</span> Ownership</li>
      <li><span class="cp-muted font-mono">2.2</span> Borrowing y Lifetimes</li>
    </ul>
  </div>

  <div>
    <h2 class="text-xl cp-toc-title">
      3. Enums, Option y Result
    </h2>
    <ul class="space-y-3 list-none pl-0 text-sm">
      <li><span class="cp-muted font-mono">3.1</span> Enums</li>
      <li><span class="cp-muted font-mono">3.2</span> Option</li>
      <li><span class="cp-muted font-mono">3.3</span> Result</li>
    </ul>
  </div>

</div>

---
layout: center
---

# Contenido (cont.)

<div class="grid grid-cols-3 gap-x-10 mt-6 text-left">

  <div>
    <h2 class="text-xl cp-toc-title">
      4. Estructuras de Datos
    </h2>
    <ul class="space-y-3 list-none pl-0 text-sm">
      <li><span class="cp-muted font-mono">4.1</span> Vec</li>
      <li><span class="cp-muted font-mono">4.2</span> Iteradores</li>
      <li><span class="cp-muted font-mono">4.3</span> HashMap y HashSet</li>
      <li><span class="cp-muted font-mono">4.4</span> Structs</li>
      <li><span class="cp-muted font-mono">4.5</span> Listas Enlazadas</li>
      <li><span class="cp-muted font-mono">4.6</span> Árboles</li>
      <li><span class="cp-muted font-mono">4.7</span> Big-O (resumen)</li>
    </ul>
  </div>

  <div>
    <h2 class="text-xl cp-toc-title">
      5. Traits y Generics
    </h2>
    <ul class="space-y-3 list-none pl-0 text-sm">
      <li><span class="cp-muted font-mono">5.1</span> Traits</li>
      <li><span class="cp-muted font-mono">5.2</span> Generics</li>
    </ul>
  </div>

</div>

<div class="mt-6 pt-3 border-t cp-divider text-sm cp-muted max-w-5xl mx-auto text-left">
  <span class="cp-group-title">Apéndices</span>
  &nbsp;&nbsp; <span class="font-mono cp-faint">A</span> Cheatsheet
  &nbsp;·&nbsp; <span class="font-mono cp-faint">B</span> Aplicación
</div>

---
layout: intro-image
---

<div class="absolute inset-0 cp-cover"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Sintaxis y Semántica</h1>
</div>

---
src: ./pages/A01-tokens.md
---
---
src: ./pages/A02-tipos-dato.md
---
---
src: ./pages/A03-estructuras-control.md
---
---
src: ./pages/A04-tipos-memoria.md
---
---
src: ./pages/A05-funciones.md
---
---
layout: intro-image
---

<div class="absolute inset-0 cp-cover"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Memory Safety</h1>
</div>

---
src: ./pages/B01-ownership.md
---
---
src: ./pages/B02-borrowing-lifetimes.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-cover"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Enums, Option y Result</h1>
</div>

---
src: ./pages/C01-enums.md
---
---
src: ./pages/C02-option.md
---
---
src: ./pages/C03-result.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-cover"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Estructuras de Datos</h1>
</div>

---
src: ./pages/D01-vec.md
---
---
src: ./pages/D02-iteradores.md
---
---
src: ./pages/D03-hashmap-hashset.md
---
---
src: ./pages/D04-structs.md
---
---
src: ./pages/D05-listas-enlazadas.md
---
---
src: ./pages/D06-arboles.md
---
---
src: ./pages/D07-big-o.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-cover"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Traits y Generics</h1>
</div>

---
src: ./pages/E01-traits.md
---
---
src: ./pages/E02-generics.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-cover"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Apéndices</h1>
</div>

---
src: ./pages/Z01-cheatsheet.md
---
---
src: ./pages/Z02-aplicacion.md
---

