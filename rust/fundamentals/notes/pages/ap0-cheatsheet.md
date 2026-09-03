---
layout: section
---

# Cheatsheet
Hoja de referencia para la corrida mental

---
layout: center
---

## Ownership — ¿se copia o se mueve?

<div class="flex flex-col gap-3 mt-3 max-w-5xl mx-auto text-left text-xs">

<div class="cp-card">
  <div class="grid gap-x-4 gap-y-2" style="grid-template-columns:1.7fr 0.8fr 1.3fr 0.9fr">
    <div class="opacity-50">Tipo de dato</div><div class="opacity-50">Dónde vive</div><div class="opacity-50">Al asignar / pasar / retornar</div><div class="opacity-50">¿Sigue usable?</div>
    <div class="font-mono">i32, u8, f64, bool, char</div><div>Stack</div><div><b>Copia</b> (Copy)</div><div>✅ Sí</div>
    <div class="font-mono">&amp;T <span class="opacity-60">(compartida)</span></div><div>Stack</div><div><b>Copia</b> el puntero (es <code>Copy</code>)</div><div>✅ Sí *</div>
    <div class="font-mono">&amp;mut T <span class="opacity-60">(exclusiva)</span></div><div>Stack</div><div><b>Movimiento</b> (no es <code>Copy</code>)</div><div>❌ No ***</div>
    <div class="font-mono">String, Vec&lt;T&gt;, Box&lt;T&gt;</div><div>Heap</div><div><b>Movimiento</b> (Move)</div><div>❌ No **</div>
  </div>
</div>

<div class="cp-card space-y-1.5">
  <div class="font-bold cp-brand mb-1">Las 3 reglas del ownership</div>
  <div>① Cada valor tiene un dueño (<i>owner</i>).</div>
  <div>② Solo un dueño a la vez.</div>
  <div>③ Cuando el dueño sale de scope, el valor se destruye (<i>drop</i>).</div>
  <div class="mt-2 opacity-90"><b>Gatillan transferencia:</b> <code>let y = x;</code> · <code>foo(x)</code> · <code>return x;</code></div>
</div>

<div class="opacity-60" style="font-size:0.6rem">* según las reglas de borrowing &nbsp;·&nbsp; ** salvo <code>.clone()</code> &nbsp;·&nbsp; *** al pasarla a una función el compilador hace un <i>reborrow</i> implícito (<code>&amp;mut *r</code>), por eso parece copiarse</div>

</div>

---
layout: center
---

## Borrowing y lifetimes — ¿es válida esta referencia?

<div class="flex flex-col gap-3 mt-3 max-w-5xl mx-auto text-left text-xs">

<div class="cp-card">
  <div class="grid gap-x-4 gap-y-2" style="grid-template-columns:1fr 1.1fr 1.7fr">
    <div class="opacity-50">Referencia</div><div class="opacity-50">Permite</div><div class="opacity-50">¿Cuántas a la vez?</div>
    <div class="font-mono">&amp;T <span class="opacity-60">(compartida)</span></div><div>leer</div><div>✅ muchas simultáneas</div>
    <div class="font-mono">&amp;mut T <span class="opacity-60">(exclusiva)</span></div><div>leer y escribir</div><div>⚠️ una sola, y sin <code>&amp;</code> activas</div>
  </div>
</div>

<div class="cp-callout">
  <b>Regla del borrow checker:</b> en un mismo instante puede existir <b>una sola</b> <code class="cp-code-inline">&amp;mut T</code> <b>o bien cualquier cantidad de</b> <code class="cp-code-inline">&amp;T</code>, <b>nunca las dos a la vez</b>. Además, toda referencia debe ser siempre válida (sin <i>dangling</i>).
</div>

<div class="cp-card space-y-2">

<div class="font-bold cp-brand">Lifetimes</div>

**Ecuación:** $'a = \min\left(L(\text{entradas})\right)$; válido si $\max\left(L(r)\right) \le\ 'a$. La referencia nunca vive más que su dueño.

</div>

</div>

---
layout: center
---

## Pelar la cebolla — leer un tipo envuelto

<div class="flex flex-col gap-3 mt-3 max-w-5xl mx-auto text-left text-xs">

<div class="cp-card">
  <div class="grid gap-x-4 gap-y-2" style="grid-template-columns:1.2fr 1.3fr 1.6fr 1.3fr;font-size:0.66rem">
    <div class="opacity-50">Envoltura</div><div class="opacity-50">Qué representa</div><div class="opacity-50">Cómo la abres</div><div class="opacity-50">Qué obtienes</div>
    <div class="font-mono">&amp;T / &amp;mut T</div><div>préstamo</div><div>deref <code>*</code> (casi siempre auto)</div><div>acceso sin mover</div>
    <div class="font-mono">Box&lt;T&gt;</div><div>dueño único (heap)</div><div>auto-deref <code>*</code></div><div>el <code>T</code> interior</div>
    <div class="font-mono">Option&lt;T&gt;</div><div>¿hay valor?</div><div><code>if let Some</code> / <code>match</code> / <code>?</code></div><div>el <code>T</code> (o nada)</div>
    <div class="font-mono">Result&lt;T,E&gt;</div><div>¿éxito o error?</div><div><code>match</code> / <code>?</code></div><div>el <code>T</code> (o <code>E</code>)</div>
    <div class="font-mono">Rc&lt;T&gt; / Arc&lt;T&gt;</div><div>propiedad compartida</div><div>auto-deref → <code>&amp;T</code>; <code>.clone()</code></div><div>solo lectura; comparte dueño</div>
    <div class="font-mono">RefCell&lt;T&gt;</div><div>mutabilidad interior</div><div><code>.borrow()</code> / <code>.borrow_mut()</code></div><div><code>Ref</code> / <code>RefMut</code> (runtime)</div>
    <div class="font-mono">Vec&lt;T&gt;</div><div>secuencia</div><div><code>.iter()</code> / <code>.into_iter()</code> / <code>[i]</code></div><div><code>&amp;T</code> / <code>T</code> / elemento</div>
  </div>
</div>

<div class="grid grid-cols-2 gap-3">

  <div class="cp-card space-y-1.5">
    <div class="font-bold cp-brand mb-1">El método · 3 pasos</div>
    <div><b>①</b> Leer el tipo de <b>afuera → adentro</b>.</div>
    <div><b>②</b> Abrir cada capa con su operación y determinar qué entrega: <b>dueño</b> (move), <b>préstamo</b> (<code>&amp;</code>) o <b>valor Copy</b>.</div>
    <div><b>③</b> Repetir hasta llegar al dato buscado.</div>
    <div class="mt-1 opacity-70">Iteradores = el mismo patrón: <code>.iter()</code> presta, <code>.into_iter()</code> consume.</div>
  </div>

  <div class="cp-callout">
    <div class="font-bold mb-1">Ejemplo · el nodo del árbol</div>
    <div class="font-mono" style="font-size:0.66rem;line-height:1.9">
      Option&lt;Rc&lt;RefCell&lt;TreeNode&gt;&gt;&gt;<br>
      → <code class="cp-code-inline">if let Some(rc)</code> → &amp;Rc&lt;..&gt;<br>
      → (Rc se desreferencia solo)<br>
      → <code class="cp-code-inline">.borrow()</code> → Ref&lt;TreeNode&gt;<br>
      → <code class="cp-code-inline">.val</code> ✅
    </div>
  </div>

</div>

</div>

---
layout: center
---

## Diagnóstico — el compilador se queja

<div class="flex flex-col gap-3 mt-3 max-w-5xl mx-auto text-left text-xs">

<div class="cp-card">
  <div class="grid gap-x-4 gap-y-2" style="grid-template-columns:1.6fr 1.4fr 1.4fr;font-size:0.68rem">
    <div class="opacity-50">Error del compilador</div><div class="opacity-50">Qué regla violaste</div><div class="opacity-50">Fix típico</div>
    <div class="font-mono">use of moved value</div><div>usaste un valor del heap <b>después</b> de moverlo</div><div><code>.clone()</code>, o pasar <code>&amp;x</code> en vez de <code>x</code></div>
    <div class="font-mono">cannot borrow as mutable … also borrowed as immutable</div><div>pediste <code>&amp;mut</code> con una <code>&amp;</code> todavía viva</div><div>termina de usar la ref inmutable antes</div>
    <div class="font-mono">cannot borrow as mutable more than once</div><div>dos <code>&amp;mut</code> al mismo tiempo</div><div>separa los scopes de cada préstamo</div>
    <div class="font-mono">x does not live long enough</div><div>la referencia sobrevive a su dueño</div><div>el dato debe vivir al menos tanto como la ref</div>
    <div class="font-mono">missing lifetime specifier</div><div>retornas <code>&amp;T</code> sin decir de cuál entrada</div><div>anota <code>'a</code> en firma y retorno</div>
  </div>
</div>

<div class="cp-card space-y-1.5">
  <div class="font-bold cp-brand mb-1">Corrida mental — tres preguntas en orden</div>
  <div><b>①</b> ¿El dato vive en Heap? → asignarlo o pasarlo lo <b>mueve</b> (el original queda inutilizable). ¿En Stack? → se <b>copia</b>, ambos siguen vivos.</div>
  <div><b>②</b> ¿Hay una <code>&amp;mut</code> y una <code>&amp;</code> vivas a la vez sobre el mismo dato? → prohibido: equivale a escribir mientras alguien lee.</div>
  <div><b>③</b> ¿La referencia devuelta o guardada vive más que su dueño? → <i>dangling</i>, prohibido.</div>
</div>

<div class="cp-callout">
  En corto, casi todo error de memoria es uno de tres: <b>un valor movido y vuelto a usar</b> · <b>lectura y escritura mezcladas</b> · <b>una referencia que vive más que su dueño</b>
</div>

</div>

<div class="cp-ver-tambien">

Ver también · 3.2 Ownership · 3.3 Borrowing · 3.6 Lifetimes · Aplicación

</div>
