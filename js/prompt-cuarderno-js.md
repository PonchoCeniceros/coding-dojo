# Cuaderno de campo de JS — nota de diseño
 
**Estado:** no construido. Esto es la decisión de arquitectura, tomada antes de
escribir la primera lámina, para que el día que empiece no se repita el análisis.
**Escrito:** 2 de septiembre de 2026, a partir de la experiencia de
*Rust · Cuaderno de campo* (`rust/fundamentals/notes/`, 321 láminas).
**Referencia del método:** `claude/rust-notes-estado.md`.
 
---
 
## 1 · El problema: el método de Rust no se copia tal cual
 
Lo que se hizo con el cuaderno de Rust fue **ordenar, no simplificar**. No hay en él
ninguna versión reducida del lenguaje: hay dos deudas declaradas (los literales de
texto y `String`) y son referencias hacia adelante, no medias verdades. Eso fue
posible porque las reglas de Rust no son opcionales: el compilador las cobra desde
la primera línea, y no existe un subconjunto que ignore ownership.
 
JS no admite ese trato, por dos razones distintas.
 
**No hay orden topológico.** Las partes difíciles son mutuamente recursivas. `this`
depende de cómo se llama la función, que depende de las arrow, que dependen de
closures y scope léxico. `class` es azúcar sobre prototipos, pero es lo primero que
todo el mundo escribe. `async` no se entiende sin el event loop, y el event loop no
es del lenguaje sino del runtime, así que no hay nada anterior donde ponerlo.
 
**No hay compilador que rechace.** La mitad del motor pedagógico del cuaderno de
Rust es citar un E0382 real y decir *esto no pasa*. En JS nada se rechaza: devuelve
`NaN`, `undefined` o `[object Object]` y sigue corriendo. El esqueleto
problema → mecanismo → ejemplo sobrevive, pero el problema pasa de ser un error de
compilación a ser un resultado incorrecto en ejecución. Eso se escribe con más
ejemplos, no con menos.
 
---
 
## 2 · La solución: tres capas
 
El desorden de JS es histórico, no estructural. Si se elige un subconjunto, lo que
queda **sí** se ordena.
 
### Capa 1 · El JS que escribes
 
El subconjunto. `const` y `let`, funciones y arrow, objetos y arreglos literales,
desestructuración, módulos ESM, `===` siempre, encadenamiento opcional,
`async`/`await`, `for..of`. Topológico estricto, sin deudas.
 
### Capa 2 · El JS que corre
 
No agrega funciones: **explica las reglas de la capa 1**. Por qué `===` era la regla
(coerción). Qué es `this` de verdad y por qué las arrow lo esquivan. En qué se
convierte una `class`. Qué hace el event loop detrás de un `await`, con microtareas.
Por qué `undefined` y `null` son dos cosas. Esta capa también es topológica, porque
la capa 1 ya dio todo el vocabulario para nombrarla.
 
### Capa 3 · El JS que lees
 
`var` y hoisting, IIFE, `module.exports`, prototipos escritos a mano, `==`,
`function` con `this` dinámico. No se ordena y no se aprende: se consulta. Es hoja de
referencia, no capítulo. La misma separación cuaderno/cheatsheet que ya existe en el
proyecto de Rust.
 
### La metáfora que sostiene la estructura
 
La capa 1 es el **mapa del metro**: topológicamente correcto, te lleva a donde vas,
callado sobre las distancias. La capa 2 es el mapa de la calle, y explica por qué
ese transbordo que en el diagrama es un puntito toma diez minutos.
 
Lo importante es que no son perspectivas simétricas. La capa 2 es estrictamente más
verdadera, pero el mapa del metro **sigue siendo el que se usa a diario**, incluso
después de conocer la geografía. Un programador competente escribe en la capa 1 y
baja a la 2 solo cuando algo se rompe.
 
La variante para explicar por qué la capa 2 no es opcional: manejar estándar. Al
principio el embrague es un procedimiento a ciegas. Después entiendes que son dos
discos igualando velocidades, y se explican cosas que ya te habían pasado: por qué
te apagas en una subida, por qué se quema el clutch. Los movimientos son idénticos
antes y después; lo que cambia es que dejas de temerle a las fallas y empiezas a
predecirlas. El que nunca lo aprende quema el clutch.
 
---
 
## 3 · La regla de oro
 
> **La capa 1 puede omitir. No puede mentir.**
> Ninguna afirmación de la capa 1 puede ser contradicha por la capa 2.
 
Es la diferencia entre el mapa del metro y Santa Claus. Santa Claus es una mentira
que hay que **retractar**: cuando llega la verdad, la primera versión se borra y
nada de lo aprendido se aprovecha. El mapa del metro se **refina**.
 
"Usa siempre `===`" es una omisión legítima. "`==` no existe" sería Santa Claus, y
cobra intereses en la capa 2.
 
### Las tentaciones concretas de JS
 
| Frase cómoda | Por qué es Santa Claus | Cómo se dice bien desde el principio |
| :--- | :--- | :--- |
| "`class` es cómo se hacen objetos" | es azúcar sobre prototipos | "`class` es la forma moderna de declarar un tipo; lo que hace por debajo va en la capa 2" |
| "las arrow son funciones más cortas" | la diferencia real es `this` | "las arrow no traen su propio `this`, y por eso son las que sirven de callback" |
| "`await` pausa la ejecución" | cede el control al event loop | "`await` entrega el control hasta que la promesa se resuelva" |
 
Las tres versiones de la derecha son ciertas a las dos resoluciones y no obligan a
desdecirse después.
 
**Nota reflexiva:** ni siquiera "`class` es azúcar sobre prototipos" es exacto, y la
capa 2 tiene que decirlo. Verificado en Node 22: los campos privados (`#x`) no se
expresan con prototipos, y `Caja()` sin `new` lanza `TypeError`. Hay azúcar, pero
también semántica propia.
 
---
 
## 4 · Qué gana el subconjunto (medido, no supuesto)
 
Todo esto corrió en Node v22.22.2:
 
- **El bug clásico del closure en un `for` desaparece.** Con `var`, los tres closures
  devuelven `[3, 3, 3]`; con `let`, `[0, 1, 2]`, porque cada iteración crea un enlace
  nuevo. La capa 1 elimina esa clase entera de errores por construcción, y es el
  mejor argumento a favor del subconjunto.
- **`await` dentro de `forEach` sobrevive al subconjunto y sigue mordiendo.**
  `forEach` ignora la promesa que devuelve su callback: el arreglo sale vacío
  (`[]`), mientras que el mismo bucle con `for..of` da `[1, 2, 3]`. Este sí es
  material de capa 2, y es de los buenos: falla en silencio.
- **Un método de `class` pasado suelto pierde su `this`.** `c.leer()` da `7`;
  `const suelto = c.leer; suelto()` da `undefined`. La capa 1 puede prevenirlo con
  una regla ("pasa `() => c.leer()`, no `c.leer`"), y la capa 2 la explica.
- `typeof null === 'object'`, `null == undefined` es `true`, `null === undefined` es
  `false`. Puro material de capa 2 y de capa 3.
---
 
## 5 · Verificación: la cuarta herramienta
 
El cuaderno de Rust tiene tres verificadores (`pnpm indice`, `pnpm refs`,
`pnpm densidad`) y la regla de que todo bloque se compila con `rustc`. Aquí el
equivalente es doble, y es mejor:
 
1. **Un `eslint.config.js` que *sea* el subconjunto.** `no-var`, `eqeqeq`,
   `prefer-const`, `no-restricted-syntax` para `this` fuera de clases, `no-iterator`.
   Todo bloque de la capa 1 pasa ese lint o no entra a la lámina. Es la cuarta
   herramienta, hermana de las tres que ya existen.
2. **Cada bloque se ejecuta y se muestra su salida real.** Y aquí el medio permite
   algo que Rust no: los bloques pueden correr **en la propia lámina**, en el
   navegador, con la salida al lado. Es una mejora pedagógica real.
Los tres verificadores actuales se reutilizan tal cual: son agnósticos del lenguaje.
 
---
 
## 6 · Decisiones pendientes, para el día que empiece
 
1. **¿JS o TypeScript?** Buena parte de lo que uno quiere de un cuaderno de JS es en
   realidad de TS, y ahí el análisis se invierte: el sistema de tipos de TS **sí** es
   un sistema de reglas con consecuencias profundas, y se ordena topológicamente casi
   tan bien como Rust. Además vuelve el compilador, con códigos de error
   (TS2322, TS2345) y `tsc --noEmit`, o sea que la metodología entera se transfiere
   intacta. Apuesta: el cuaderno útil es de TS, con las capas 1 y 2 de JS como sus
   dos primeros capítulos.
2. **¿Un deck o dos?** Las capas 1 y 2 pueden ser dos secciones de un mismo deck, o
   dos decks. A favor de uno solo: la capa 2 referencia constantemente la 1. A favor
   de dos: la capa 1 es material de primer año y la 2 no.
3. **Dónde queda el DOM.** Probablemente fuera, igual que tokio y los frameworks
   quedaron fuera del cuaderno de Rust. El navegador no es el lenguaje.
4. **Navegador o Node.** Afecta a los módulos, al I/O y a los ejemplos ejecutables.
5. **Orden dentro de la capa 2.** El candidato natural es: coerción → funciones y
   `this` → modelo de objetos → event loop. Hay que verificar que sea un DAG antes de
   comprometerse.
---
 
## 7 · Qué se reutiliza del proyecto de Rust
 
- **`GUIA-DE-TONO.md`**, las once reglas, tal cual. Son de escritura, no de Rust.
- **Los tres verificadores** (`sync-indice.py`, `revisar-refs.py`,
  `revisar-densidad.py`), agnósticos del lenguaje.
- **`export-sections.py`** y el truco de exportar el deck completo y partirlo con
  `pypdf`, porque `slidev export --range` genera páginas en blanco.
- **El CSS y las láminas de portada** (`public/images/lamina.py`): el dict
  `VARIANTES` genera las tres paletas, y las clases de rol
  (`.cp-lamina-portada` / `.cp-lamina-seccion`) siguen el tema.
- **El esqueleto de página R9**: problema → mecanismo → ejemplo → regla → ver también.
- **La estructura de deudas declaradas**, aquí más necesaria que allá.
---
 
## 8 · Estimación
 
| | Láminas | Ordenable |
| :--- | ---: | :--- |
| Capa 1 · el JS que escribes | 60–80 | topológico estricto |
| Capa 2 · el JS que corre | 70–90 | topológico, sobre el vocabulario de la capa 1 |
| Capa 3 · el JS que lees | glosario | no se ordena, se indexa |
 
Total aproximado: 150–200 láminas contra las 321 de Rust. El peso cambia por
completo. Aquí los capítulos gordos son memoria (57 láminas) y abstracciones; allá
serían funciones y `this`, el modelo de objetos, el event loop, y coerción.
 
---
 
## 9 · La regla general que salió de todo esto
 
**Se puede ordenar lo que es un sistema de reglas. Solo se puede indexar lo que es
una acumulación de convenciones.**
 
| Lenguaje | ¿Orden topológico? | Por qué |
| :--- | :--- | :--- |
| Rust | sí | la dificultad son reglas, y las reglas se ordenan |
| TypeScript (solo tipos) | sí, con JS como prerrequisito | mismo caso, más las válvulas de escape (`any`, aserciones) |
| Python | casi, con una deuda grande | el modelo de datos es circular: `len(x)` llama a `__len__` |
| JavaScript | no, sin subconjunto | la dificultad es superficie histórica, no reglas |
 
Y para lo segundo el formato correcto no es un cuaderno topológico sino una hoja de
referencia. Que es exactamente la separación que este proyecto ya hizo desde el
principio.
 
---
 
## Precedentes
 
- **How to Design Programs**, los *language levels* de Racket: dialectos que crecen
  capítulo a capítulo. Es el precedente serio de la capa 1.
- **JavaScript: The Good Parts**, Crockford. Escribió la capa 1 y nunca la 2, y por
  eso envejeció mal: dejó reglas sin justificación.
