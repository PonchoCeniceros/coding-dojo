# Guía de tono — *Rust*

Destilada de `A01`–`B02` (las páginas supervisadas), depurada de lo personal y
apretada. Aplica a las 22 páginas existentes y a las nuevas del reordenamiento.

**Registro objetivo:** manual técnico. Tercera persona, frase corta, una idea por
frase. Explica y no convence: si la diapositiva demostró algo, no lo remata.

---

## Las 10 reglas

### R1 · Sin raya larga como bisagra

Es el tic dominante: **35 casos** en el deck, siempre con la misma figura —
*afirmación · raya · reformulación que la vende*. Tus páginas A01–B02 tienen **cero**.

Sustituto: punto si son dos ideas; dos puntos si la segunda explica la primera.
Si la reformulación no agrega información, se borra.

| ❌ Actual | ✅ Objetivo |
|---|---|
| `.get(i)` devuelve `Option<&T>` en vez de arriesgar un *panic* — de nuevo, `Option` modelando la posible ausencia. | `.get(i)` devuelve `Option<&T>` en lugar de provocar un *panic*. |
| Un **adaptador** transforma un iterador en otro, pero **no ejecuta nada todavía** — solo describe qué hacer. | Un adaptador transforma un iterador en otro. No recorre nada: describe la operación y la difiere. |
| `Rc<T>` por sí solo **no permite mutar** el valor compartido — todas las referencias son de solo lectura. | `Rc<T>` no permite mutar el valor compartido: todas sus referencias son de solo lectura. |
| Un slice `&[T]` es una referencia a una porción contigua de un `Vec`, sin tomar su propiedad — es *borrowing* aplicado a colecciones. | Un slice `&[T]` es una referencia a una porción contigua de un `Vec`, sin tomar su propiedad. Es el préstamo de §2.3 aplicado a colecciones. |

La raya larga se conserva solo donde es puntuación real: inciso entre comas fuertes,
o separador en una celda de tabla.

### R2 · Títulos en mayúscula inicial

Español, no inglés. **40 de 92 títulos** están en Title Case; el pico es `Z02` (8 de 9)
y `D06`/`F01` (5 de 8).

```
❌ ## Tres Formas de Iterar          ✅ ## Tres formas de iterar
❌ ## Un Patrón que Reaparece        ✅ ## Dónde reaparece este patrón
❌ ## Result Estaba a la Vista       ✅ ## Result en código ya escrito
❌ ## Mutabilidad en Tiempo de Ejecución  ✅ ## Mutabilidad en tiempo de ejecución
```

### R3 · Tercera persona

Sin `tú` ni imperativos dirigidos al lector. El sujeto es el lenguaje, el compilador
o el código, no la persona que lee.

| ❌ | ✅ |
|---|---|
| para eso **ya viste** `if let` y `while let` | `if let` y `while let` (§1.6) cubren ese caso |
| **Puedes tener** infinitas lecturas, pero si **creas** una referencia mutable… | Se admiten múltiples referencias de lectura. Al crear una referencia mutable… |
| **De ahí que un tipo requiera** `Hash + Eq` para ser llave | `HashMap` exige `Hash + Eq` en su llave |

### R4 · El eco se declara, no se insinúa

**28 apariciones** de *"de nuevo / el mismo / ya visto / igual que"*. Reconectar
secciones es lo mejor que hace el deck; la muletilla es lo peor de cómo lo hace.

La conexión deja de ser prosa y pasa a ser un elemento fijo al pie de la diapositiva:

```markdown
<div class="cp-ver-tambien">
Ver también · §2.2 Ownership · §3.3 Option
</div>
```

Dentro del texto, referencia explícita en lugar de guiño:

| ❌ | ✅ |
|---|---|
| Es el mismo `Option` de la sección anterior — el compilador obliga a considerar el caso vacío. | `pop()` devuelve `Option<T>` (§3.3): el caso vacío es obligatorio de manejar. |
| es exactamente la distinción de *ownership* y *borrowing* ya vista | es la distinción de §2.2 y §2.3 aplicada a colecciones |

### R5 · Sin cierres que venden

Si la diapositiva ya lo demostró, el remate sobra. Cerrar con dato, regla o ejemplo.

| ❌ | ✅ |
|---|---|
| La elección no es estética: refleja cuántos dueños tiene realmente el dato y si necesita cambiar después de compartirse. | Criterio: número de dueños y necesidad de mutación tras compartir. |
| Y el patrón se repite: `Option` y `Result` son enums con dos variantes — la misma "cebolla" que se pela con `match`, `if let` o `?`. | `Option` y `Result` son enums de dos variantes. Se abren con `match`, `if let` o `?`. |
| El patrón real: encadenar adaptadores perezosos y cerrar con un consumidor. | El uso habitual encadena adaptadores y cierra con un consumidor. |
| **Conclusión:** Rust traslada la seguridad de la memoria al tiempo de compilación. | Rust verifica estas garantías en tiempo de compilación. |

### R6 · Una metáfora por concepto, nombrada una sola vez

**18 apariciones** (cebolla, tarjeta, dedo, puntero láser, columna vertebral, corrida
mental). Se conservan las que tienen una tabla o un diagrama que las sostenga —la
cebolla de `Z01` funciona porque la acompaña la tabla de envolturas—. Las decorativas
se van: *"solo el 'dedo' que lo señala"*, *"la 'tarjeta/puntero'"*, *"la columna
vertebral de la sintaxis"*.

### R7 · Sin superlativos ni absolutos no verificables

| ❌ | ✅ |
|---|---|
| El Stack es una estructura de acceso **ultra rápido** | El acceso al stack es de orden constante: mover el puntero de pila |
| duplicar datos pequeños en el Stack es **sumamente barato** | copiar un valor `Copy` es una copia de bits de tamaño conocido |
| Si tu código compila, es **matemáticamente seguro** en memoria | Si compila sin `unsafe`, el código está libre de accesos inválidos a memoria |

> La última está en `B02`, una de tus páginas, y además **es falsa**: un ciclo de `Rc`
> filtra memoria y sigue siendo código seguro; `unsafe` sigue existiendo. Es el
> ejemplo de por qué la regla no es cosmética.

### R8 · Una negrita por viñeta, y solo la primera vez

Densidad actual: `C01` 6.0 negritas por 100 palabras, `D02` 5.7, `D03` 5.1, `E01` 4.7.
Tus páginas: `A02` 0.4, `A05` 0.8. Cuando todo resalta, nada resalta.

Regla: negrita solo en la **primera** aparición de un término que la página define.
Nunca en frases completas. El código va en `código`, no en negrita.

### R9 · Esqueleto fijo por página

Esto es lo que vuelve el tono reproducible sin depender de la inspiración del día.
Toda página explicativa sigue el mismo orden:

```
## Título (mayúscula inicial)

1. Problema      · 1–2 frases: qué no se puede hacer sin esto
2. Mecanismo     · qué es y cómo funciona
3. Ejemplo       · el mínimo que compila
4. Regla         · cuándo usarlo / cuándo no
5. Ver también   · §referencias
```

Las páginas C–F ya lo hacen de facto (abren con *"El Problema:"*). Volverlo explícito
y aplicarlo también a A y B.

### R10 · Frase corta

Promedio actual: `A02` 9.7 palabras por frase, `C02` 17.1, `B02` 16.6.
**Objetivo: 12–15.** Una idea por frase. Si lleva dos verbos principales y una
subordinada, se parte.

### R11 · Una diapositiva, un elemento principal

La densidad es parte del tono. Una diapositiva sostiene **un** elemento pesado
(una tabla **o** un bloque de código **o** una rejilla de dos bloques cortos), más
como mucho una entradilla de dos líneas y un callout breve.

Cuando aparecen tabla **y** código en la misma diapositiva, se parte en dos: el
concepto con su tabla, y el ejemplo con su nota. Sale más barato pasar dos
diapositivas que leer una saturada.

| Señal de saturación | Qué hacer |
| :--- | :--- |
| tabla + bloque de código | partir en dos diapositivas |
| dos callouts | dejar uno; el otro es texto normal o se va |
| callout de más de tres viñetas | sacar la última como frase suelta |
| bloque de código de más de ~15 líneas | recortar al mínimo que compile |
| más de un `##` por diapositiva | ya son dos diapositivas |

Preferir muchas diapositivas ligeras a pocas densas. En un deck de estudio, el
costo de avanzar es cero.

---

## Lista de verificación

Antes de dar una página por terminada:

- [ ] ¿Alguna raya larga que sea bisagra retórica y no puntuación?
- [ ] ¿Títulos en mayúscula inicial?
- [ ] ¿Aparece `tú`, `ya viste`, `puedes`, `vas a ver`?
- [ ] ¿Hay *"de nuevo / el mismo / ya visto"* en vez de un `§`?
- [ ] ¿La última frase cierra con dato o con eslogan?
- [ ] ¿Más de una negrita por viñeta?
- [ ] ¿Algún superlativo (`ultra`, `sumamente`, `matemáticamente`, `por completo`)?
- [ ] ¿Alguna frase de más de 20 palabras?
- [ ] ¿Está el bloque "Ver también"?
- [ ] ¿La diapositiva carga más de un elemento pesado (R11)?

---

## Orden de aplicación sugerido

1. **Automatizable** (un script, revisión visual): R2 títulos, R1 rayas largas, R3 segunda persona.
2. **Página por página**: R4 ecos → `§`, R5 cierres, R8 negritas.
3. **Al escribir las páginas nuevas**: R9 esqueleto desde el principio.

Las páginas `A01`–`B02` necesitan poco: R2 en 7 títulos, R7 en cuatro superlativos,
y el "Ver también". El grueso del trabajo está en `C01`–`Z02`.
