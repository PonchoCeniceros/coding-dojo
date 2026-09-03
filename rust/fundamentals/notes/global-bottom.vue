<!--
  Folio: número de lámina con el mismo pececito de las portadas.
  Se oculta en las láminas a sangre (portadas, portadillas, contraportada),
  que son las de `layout: intro-image`.
-->
<template>
  <div
    v-if="$slidev.nav.currentSlideRoute?.meta?.slide?.frontmatter?.layout !== 'intro-image'"
    class="cp-folio"
  >
    <svg class="cp-folio-pez" viewBox="-10 0 112 50" aria-hidden="true">
      <path d="M 14,25 C 32,7 74,7 98,25 C 74,43 32,43 14,25 Z" />
      <path d="M 14,25 L -8,11 L -1,25 L -8,39 Z" />
    </svg>
    <span>{{ $slidev.nav.currentPage }}</span>
  </div>
</template>
