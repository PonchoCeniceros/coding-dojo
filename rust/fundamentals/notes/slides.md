---
theme: apple-basic
title: Rust · Cuaderno de campo
layout: intro-image
fonts:
  sans: Work Sans
  local: Work Sans
  mono: JetBrains Mono
---

<div class="absolute inset-0 cp-lamina cp-lamina-portada"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Rust</h1>
  <p class="cp-cover-text">Cuaderno de campo</p>
  <p class="cp-cover-text" style="opacity:0.6; font-size:0.8rem; margin-top:0.2rem">Segunda edición</p>
</div>

<div class="absolute top-10 z-2">
  <span class="font-700 cp-cover-text">
    Giovanny Alfonso Chávez Ceniceros
    <span style="opacity:0.65; font-weight:400"> · con Claude</span>
  </span>
</div>

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-naranja"></div>

<div class="absolute top-10 z-2">
  <span class="font-700 cp-cover-text">
    Giovanny Alfonso Chávez Ceniceros
    <span style="opacity:0.65; font-weight:400"> · con Claude</span>
  </span>
</div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Rust</h1>
  <p class="cp-cover-text">Cuaderno de campo</p>
  <p class="cp-cover-text" style="opacity:0.6; font-size:0.8rem; margin-top:0.2rem">Segunda edición</p>
</div>

---
layout: center
---

# Contenido

<div class="grid grid-cols-2 gap-x-10 gap-y-4 mt-5 text-left text-sm">

  <div>
    <a href="/6" data-sec="1"><b class="cp-toc-title">1 · Fundamentos</b></a>
    <div class="cp-muted">tokens · tipos escalares · variables · expresiones · funciones · control de flujo</div>
  </div>

  <div>
    <a href="/45" data-sec="2"><b class="cp-toc-title">2 · Tipos compuestos</b></a>
    <div class="cp-muted">tuplas y arreglos · structs · enums · patrones</div>
  </div>

  <div>
    <a href="/67" data-sec="3"><b class="cp-toc-title">3 · Memoria</b></a>
    <div class="cp-muted">stack y heap · ownership · borrowing · strings · impl y métodos · lifetimes</div>
  </div>

  <div>
    <a href="/132" data-sec="4"><b class="cp-toc-title">4 · Abstracciones de costo cero</b></a>
    <div class="cp-muted">traits · generics · closures · traits de la stdlib · operadores</div>
  </div>

  <div>
    <a href="/166" data-sec="5"><b class="cp-toc-title">5 · Vocabulario de la stdlib</b></a>
    <div class="cp-muted">Option · Result · Vec · HashMap · otras colecciones · iteradores</div>
  </div>

  <div>
    <a href="/216" data-sec="6"><b class="cp-toc-title">6 · Indirección</b></a>
    <div class="cp-muted">Box y listas · Rc, RefCell y árboles · despacho dinámico · el mapa de la sección</div>
  </div>

  <div>
    <a href="/252" data-sec="7"><b class="cp-toc-title">7 · Proyectos</b></a>
    <div class="cp-muted">módulos · crates y Cargo · tests · errores idiomáticos</div>
  </div>

  <div>
    <div class="cp-muted">hoja de referencia · tabla de diagnóstico</div>
  </div>

  <div>
    <a href="/292" data-sec="8"><b class="cp-toc-title">8 · Concurrencia</b></a>
    <div class="cp-muted">la sección 6 entre hilos · hilos · Send y Sync · Arc y Mutex</div>
  </div>

  <div>
    <a href="/309" data-sec="9"><b class="cp-toc-title">9 · Async</b></a>
    <div class="cp-muted">async y await · Future · el runtime · Send en las tareas · un servidor mínimo</div>
  </div>

</div>

<div class="cp-ver-tambien">Ejercicios: deck aparte (<code>pnpm export:sections ej</code>)

</div>

---
src: ./pages/0-como-leer.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">1 · Fundamentos</h1>
</div>

---
src: ./pages/1.1-tokens.md
---
---
src: ./pages/1.2-tipos-escalares.md
---
---
src: ./pages/1.3-variables.md
---
---
src: ./pages/1.4-expresiones.md
---
---
src: ./pages/1.5-funciones.md
---
---
src: ./pages/1.6-control-flujo.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">2 · Tipos compuestos</h1>
</div>

---
src: ./pages/2.1-tuplas-arreglos.md
---
---
src: ./pages/2.2-structs.md
---
---
src: ./pages/2.3-enums.md
---
---
src: ./pages/2.4-patrones.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">3 · Memoria</h1>
</div>

---
src: ./pages/3.1-stack-heap.md
---
---
src: ./pages/3.2-ownership.md
---
---
src: ./pages/3.3-borrowing.md
---
---
src: ./pages/3.4-strings.md
---
---
src: ./pages/3.5-impl-metodos.md
---
---
src: ./pages/3.6-lifetimes.md
---
---
src: ./pages/3.7-mapa-seccion.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">4 · Abstracciones de costo cero</h1>
</div>

---
src: ./pages/4.0-costo-cero.md
---
---
src: ./pages/4.1-traits.md
---
---
src: ./pages/4.2-generics.md
---
---
src: ./pages/4.3-closures.md
---
---
src: ./pages/4.4-traits-stdlib.md
---
---
src: ./pages/4.5-operadores.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">5 · Vocabulario de la stdlib</h1>
</div>

---
src: ./pages/5.1-option.md
---
---
src: ./pages/5.2-result.md
---
---
src: ./pages/5.3-vec.md
---
---
src: ./pages/5.4-hashmap-hashset.md
---
---
src: ./pages/5.5-otras-colecciones.md
---
---
src: ./pages/5.6-iteradores.md
---
---
src: ./pages/5.7-iteradores-a-fondo.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">6 · Indirección</h1>
</div>

---
src: ./pages/6.1-box-listas.md
---
---
src: ./pages/6.2-rc-refcell-arboles.md
---
---
src: ./pages/6.3-dyn.md
---
---
src: ./pages/6.4-mapa-seccion.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">7 · Proyectos</h1>
</div>

---
src: ./pages/7.1-modulos.md
---
---
src: ./pages/7.2-crates-cargo.md
---
---
src: ./pages/7.3-tests.md
---
---
src: ./pages/7.4-errores-idiomaticos.md
---
---
src: ./pages/7.5-entrada-salida.md
---
---
src: ./pages/7.6-macros-atributos.md
---


---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">8 · Concurrencia</h1>
</div>

---
src: ./pages/8.0-la-6-entre-hilos.md
---
---
src: ./pages/8.1-hilos.md
---
---
src: ./pages/8.2-send-sync.md
---
---
src: ./pages/8.3-estado-compartido.md
---
<!-- Diferidos a un capítulo futuro de Cómputo paralelo (ver claude/rust-notes-estado.md).
Para reactivarlos: quitar este comentario, devolver los separadores a la columna 0 y
quitarles el `_` a los archivos.

src: ./pages/_8.4-canales.md

src: ./pages/_8.5-paralelismo.md
-->

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">9 · Async</h1>
</div>

---
src: ./pages/9.1-el-problema.md
---
---
src: ./pages/9.2-async-await.md
---
---
src: ./pages/9.3-runtime.md
---
---
src: ./pages/9.4-send-en-tareas.md
---
---
src: ./pages/9.5-async-o-hilos.md
---
---
src: ./pages/9.6-un-servidor-minimo.md
---

---
layout: intro-image
---

<div class="absolute inset-0 cp-lamina cp-lamina-contraportada"></div>

<div class="absolute top-10 z-2">
  <span class="font-700 cp-cover-text">
    Giovanny Alfonso Chávez Ceniceros
    <span style="opacity:0.65; font-weight:400"> · con Claude</span>
  </span>
</div>

<div class="absolute bottom-10 z-2 cp-colofon">
  <p class="cp-cover-text"><b>Rust · Cuaderno de campo</b></p>
  <p class="cp-cover-text">Segunda edición · septiembre de 2026</p>
  <p class="cp-cover-text">332 láminas · 9 secciones · 80 ejercicios</p>
  <p class="cp-cover-text">Todos los bloques de código se compilaron con rustc 1.95.</p>
  <p class="cp-cover-text">Orden topológico: ningún símbolo aparece antes de explicarse.</p>
</div>


<!--
SECCIONES RETIRADAS (comentadas, no borradas).
Para reactivarlas, quitar este comentario y devolver los separadores a la columna 0.

  ---
layout: intro-image
  ---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Cheatsheet</h1>
</div>

  ---
src: ./pages/ap0-cheatsheet.md
  ---

  ---
layout: intro-image
  ---

<div class="absolute inset-0 cp-lamina cp-lamina-seccion"></div>

<div class="absolute bottom-10 z-2">
  <h1 class="cp-cover-text">Apéndices</h1>
</div>

  ---
src: ./pages/ap2-aplicacion.md
  ---
-->
