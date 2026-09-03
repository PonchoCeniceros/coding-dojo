---
layout: section
---

# Ejercicios propuestos

---
layout: default
---

## Ejercicio 1: La keyword perdida
<br/>

```rust
fn main() {
    x = 42;
    println!("x es: {}", x);
}
```

🤔 El código de arriba falta algo esencial. ¿Qué keyword de Rust necesitas para que `x` exista dentro del `main`?

---
layout: default
---

## Respuesta 1: La keyword perdida
<br/>

Rust exige declarar las variables con `let` antes de usarlas. Sin `let`, el compilador no sabe que `x` es una nueva variable.

```rust
fn main() {
    let x = 42;
    println!("x es: {}", x);
}
```

---
layout: default
---

## Ejercicio 2: El identificador rebelde
<br/>

```rust
fn main() {
    let miVariable = String::from("hola");
    let 2do_intento = "mundo";
    println!("{} {}", miVariable, 2do_intento);
}
```

❌ Este código tiene dos errores de convención y sintaxis. ¿Cuáles son las reglas de identificadores que está violando?

---
layout: default
---

## Respuesta 2: El identificador rebelde
<br/>

Dos problemas:
1. Rust usa **snake_case** para variables: `mi_variable`, no `miVariable` (camelCase).
2. Los identificadores **no pueden empezar con dígitos**: `2do_intento` es inválido.

```rust
fn main() {
    let mi_variable = String::from("hola");
    let segundo_intento = "mundo";
    println!("{} {}", mi_variable, segundo_intento);
}
```

---
layout: default
---

## Ejercicio 3: La prioridad oculta
<br/>

```rust
fn main() {
    let resultado = 2 + 3 * 4;
    let esperado = (2 + 3) * 4;
    println!("resultado: {}, esperado: {}", resultado, esperado);
}
```

🤔 ¿Son `resultado` y `esperado` iguales o diferentes? ¿Qué operador tiene mayor prioridad en Rust?

---
layout: default
---

## Respuesta 3: La prioridad oculta
<br/>

Son **diferentes**. `resultado` es `14` (3 * 4 = 12, + 2 = 14) porque `*` tiene prioridad sobre `+`. `esperado` es `20` porque los paréntesis `(2 + 3)` fuerzan la suma primero.

```rust
fn main() {
    let resultado = 2 + 3 * 4;   // 14
    let esperado = (2 + 3) * 4;  // 20
    println!("resultado: {}, esperado: {}", resultado, esperado);
}
```

---
layout: default
---

## Ejercicio 4: El camino incompleto
<br/>

```rust
fn main() {
    let numero = 7;
    if numero > 10 {
        println!("Grande");
    }
}
```

🤔 El código compila pero no imprime nada. ¿Qué estructura de control podrías agregar para manejar el caso contrario y mostrar "Pequeño"?

---
layout: default
---

## Respuesta 4: El camino incompleto
<br/>

Necesitas un `else` para cubrir el caso cuando la condición es falsa:

```rust
fn main() {
    let numero = 7;
    if numero > 10 {
        println!("Grande");
    } else {
        println!("Pequeño");
    }
}
```

---
layout: default
---

## Ejercicio 5: El match incompleto
<br/>

```rust
fn main() {
    let opcion = 3;
    match opcion {
        1 => println!("Uno"),
        2 => println!("Dos"),
    }
}
```

❌ Este código no compila. ¿Qué regla de `match` está violando y cómo se soluciona?

---
layout: default
---

## Respuesta 5: El match incompleto
<br/>

`match` en Rust debe ser **exhaustivo** (cubrir todos los valores posibles). Aquí solo se cubren `1` y `2`, pero `opcion` es `i32` y puede tener cualquier valor. Se soluciona con un brazo `_` (catch-all):

```rust
fn main() {
    let opcion = 3;
    match opcion {
        1 => println!("Uno"),
        2 => println!("Dos"),
        _ => println!("Otro"),
    }
}
```

---
layout: default
---

## Ejercicio 6: El bucle que no termina
<br/>

```rust
fn main() {
    let mut contador = 0;
    loop {
        contador += 1;
        if contador == 5 {
            // ¿Qué va aquí?
        }
    }
    println!("Contador final: {}", contador);
}
```

❌ El `loop` es infinito y nunca se llega al `println!`. ¿Qué palabra clave falta para romper el ciclo cuando `contador` llegue a 5?

---
layout: default
---

## Respuesta 6: El bucle que no termina
<br/>

La palabra clave `break` detiene el `loop`:

```rust
fn main() {
    let mut contador = 0;
    loop {
        contador += 1;
        if contador == 5 {
            break;
        }
    }
    println!("Contador final: {}", contador);
}
```

---
layout: default
---

## Ejercicio 7: El tipo invisible
<br/>

```rust
fn main() {
    let x = 42;
    let y = 3.14;
    let z = true;
}
```

🤔 ¿Qué tipos infiere Rust para `x`, `y` y `z`? ¿Cómo podrías verificarlo en código?

---
layout: default
---

## Respuesta 7: El tipo invisible
<br/>

Rust infiere:
- `x`: `i32` (entero por defecto)
- `y`: `f64` (flotante por defecto)
- `z`: `bool`

Puedes verificarlo pidiendo el tamaño con `std::mem::size_of_val` o viendo el error si forzas un tipo incompatible.

---
layout: default
---

## Ejercicio 8: El índice prohibido
<br/>

```rust
fn main() {
    let arr = [10, 20, 30, 40];
    let primero = arr[0];
    let ultimo = arr[3];
    let fuera = arr[10];
    println!("{} {}", primero, ultimo);
}
```

❌ ¿Qué línea causa un error y por qué? ¿El error ocurre en compilación o en ejecución?

---
layout: default
---

## Respuesta 8: El índice prohibido
<br/>

`arr[10]` causa un error en **ejecución** (panic) porque el arreglo tiene 4 elementos (índices 0..3) y se está accediendo al índice 10, que está fuera de los límites. El compilador no puede saber en tiempo de compilación qué índice se usará (si fuera una variable), así que la verificación ocurre en runtime.

```rust
fn main() {
    let arr = [10, 20, 30, 40];
    let primero = arr[0];
    let ultimo = arr[3];
    // let fuera = arr[10]; // 💥 panic en runtime
    println!("{} {}", primero, ultimo);
}
```

---
layout: default
---

## Ejercicio 9: La tupla desestructurada
<br/>

```rust
fn main() {
    let persona = ("Ana", 30, true);
    // Extrae el nombre y la edad en variables separadas
    // sin usar persona.0, persona.1
}
```

🤔 ¿Qué característica de Rust permite extraer los valores de una tupla en variables individuales en una sola línea?

---
layout: default
---

## Respuesta 9: La tupla desestructurada
<br/>

La **desestructuración (destructuring)** permite desempaquetar una tupla en una sola línea:

```rust
fn main() {
    let persona = ("Ana", 30, true);
    let (nombre, edad, activo) = persona;
    println!("{} tiene {} años", nombre, edad);
}
```

---
layout: default
---

## Ejercicio 10: ¿Stack o Heap?
<br/>

```rust
fn main() {
    let a = 100;
    let b = "hola";
    let c = String::from("mundo");
    let d = [1, 2, 3];
    let e = vec![1, 2, 3];
}
```

🤔 ¿Cuáles de estas variables viven completamente en el Stack y cuáles almacenan datos en el Heap?

---
layout: default
---

## Respuesta 10: ¿Stack o Heap?
<br/>

En el Stack: `a` (`i32`), `b` (`&str` — el string vive en el binario), `d` (`[i32; 3]` — arreglo de tamaño fijo).

En el Heap: `c` (`String`), `e` (`Vec<i32>`). El puntero al heap está en el Stack, pero los datos reales están en el Heap.

---
layout: default
---

## Ejercicio 11: Copiar vs Mover
<br/>

```rust
fn main() {
    let x = 42;
    let y = x;
    println!("x: {}, y: {}", x, y); // ✅

    let s1 = String::from("hola");
    let s2 = s1;
    println!("s1: {}, s2: {}", s1, s2); // ❌
}
```

🤔 ¿Por qué el primer `println!` funciona y el segundo no, si la estructura de las asignaciones es idéntica?

---
layout: default
---

## Respuesta 11: Copiar vs Mover
<br/>

`i32` implementa el trait `Copy`: al hacer `let y = x`, se duplica el valor en el Stack y ambas variables son independientes.

`String` **no** implementa `Copy` porque almacena datos en el Heap. `let s2 = s1` **mueve** la propiedad: `s1` queda inválida para evitar el doble free.

```rust
let x = 42;       // i32 es Copy
let y = x;        // se copia, ambos viven

let s1 = String::from("hola"); // String no es Copy
let s2 = s1;      // se mueve, s1 muere
```

---
layout: default
---

## Ejercicio 12: El bloque que todo lo borra
<br/>

```rust
fn main() {
    let x = 10;
    {
        let y = 20;
        println!("Dentro: x={}, y={}", x, y);
    }
    println!("Fuera: x={}", x);
    println!("Fuera: y={}", y); // ❌
}
```

¿Por qué falla el último `println!`? ¿Qué regla de los delimitadores `{}` y del Stack explica este comportamiento?

---
layout: default
---

## Respuesta 12: El bloque que todo lo borra
<br/>

Las llaves `{}` crean un **ámbito (scope)**. Todo lo declarado dentro de ellas vive solo allí. Al cerrarse el bloque (la llave `}`), `y` se elimina del Stack. Fuera del bloque, `y` ya no existe. Esto es fundamental para la gestión de memoria en Rust: los recursos se liberan automáticamente al salir de su ámbito.

```rust
fn main() {
    let x = 10;
    {
        let y = 20;
        println!("Dentro: x={}, y={}", x, y);
    } // y se destruye aquí
    println!("Fuera: x={}", x);
    // println!("Fuera: y={}", y); // Error: y no existe
}
```

---
layout: default
---

## Ejercicio 13: El clon olvidado
<br/>

```rust
fn main() {
    let s1 = String::from("hola");
    let s2 = s1; 
    println!("{}, mundo!", s1); // ❌ ¿Por qué falla? ¿Cómo lo arreglas sin borrar la línea 3?
}
```

---
layout: default
---

## Respuesta 13: El clon olvidado
<br/>

`s1` se **mueve** (move) a `s2`. Después de esa asignación, `s1` ya no es válido
porque Rust transfiere la propiedad del dato en el Heap. El compilador prohíbe
usarlo para evitar el problema de "doble free".

Corrección: clonar antes de transferir.
```rust
let s2 = s1.clone();
```

---
layout: default
---

## Ejercicio 14: El agujero negro de las funciones
<br/>

```rust
fn tomar_propiedad(texto: String) {
    println!("{}", texto);
}

fn main() {
    let frase = String::from("Rust es genial");
    tomar_propiedad(frase);
    println!("{}", frase); // ❌ ¿Por qué 'frase' ya no existe aquí?
}
```

---
layout: default
---

## Respuesta 14: El agujero negro de las funciones
<br/>

Al pasar `frase` a `tomar_propiedad(frase)`, la propiedad del String se transfiere
al parámetro `texto`. Cuando la función termina y `texto` sale de alcance, el
String se destruye. En `main`, `frase` ya apunta a memoria liberada, por eso el
compilador lo prohíbe.

Corrección: pasar una referencia `&frase` o devolver la propiedad con `-> String`.

---
layout: default
---

## Ejercicio 15: Tipos primitivos en el Stack
<br/>

```rust
fn procesar_numero(n: i32) {
    println!("{}", n);
}

fn main() {
    let x = 42;
    procesar_numero(x);
    println!("{}", x); // 🤔 ¿Por qué este SI compila y el Ejercicio 2 NO?
}
```

---
layout: default
---

## Respuesta 15: Tipos primitivos en el Stack
<br/>

`i32` implementa el trait `Copy`. Los tipos `Copy` se **copian** bit a bit en el
Stack en lugar de moverse. Por eso `x` sigue siendo válido después de la llamada:
nunca se transfirió la propiedad, solo se duplicó el valor.

---
layout: default
---

## Ejercicio 16: El ciclo de devoluciones
<br/>

```rust
fn cambiar_dueno(s: String) -> String {
    s
}

fn main() {
    let s1 = String::from("datos");
    let s2 = cambiar_dueno(s1);
    // ¿Quién es el dueño de los bytes "datos" en esta línea? ¿s1 o s2?
}
```

---
layout: default
---

## Respuesta 16: El ciclo de devoluciones
<br/>

Al finalizar la línea `let s2 = cambiar_dueno(s1)`:

- `s1` ya no es el dueño (movió su propiedad al parámetro `s`).
- La función devuelve `s`, y ese valor se asigna a `s2`.
- **`s2` es el único dueño** de los bytes "datos".

---
layout: default
---

## Ejercicio 17: Mutabilidad y transferencia
<br/>

```rust
fn main() {
    let s1 = String::from("original");
    let mut s2 = s1; // ¿Es válido transferir la propiedad de algo inmutable a algo mutable?
    s2.push_str(" modificado");
    println!("{}", s2);
}
```

---
layout: default
---

## Respuesta 17: Mutabilidad y transferencia
<br/>

Sí, es válido. La mutabilidad es una propiedad del **binding** (la variable),
no del dato. Al hacer `let mut s2 = s1`, simplemente se transfiere la propiedad
a un binding que permite modificaciones. El String en sí no cambia; lo que cambia
es quién lo tiene y con qué permisos.

---
layout: default
---

## Ejercicio 18: Ownership dentro de un bucle
<br/>

```rust
fn main() {
    let lista = vec![String::from("A"), String::from("B")];
    for elemento in lista {
        println!("{}", elemento);
    }
    // ❌ Si intentas usar 'lista' aquí, fallará. ¿A dónde se movió la lista completa?
}
```

---
layout: default
---

## Respuesta 18: Ownership dentro de un bucle
<br/>

`for elemento in lista` usa `IntoIterator`, que **consume** el vector completo.
La propiedad de `lista` se transfiere al iterador al inicio del `for`. Cada
iteración extrae y toma propiedad de un elemento. Al terminar el bucle, el vector
original ya fue descompuesto; no existe más.

Corrección: iterar por referencia con `for elemento in &lista`.

---
layout: default
---

## Ejercicio 19: Estructuras que reclaman propiedad
<br/>

```rust
struct Contenedor {
    contenido: String,
}

fn main() {
    let texto = String::from("Secreto");
    let c = Contenedor { contenido: texto };
    // 🤔 ¿Puedes seguir usando la variable 'texto' aquí abajo? ¿Por qué?
}
```

---
layout: default
---

## Respuesta 19: Estructuras que reclaman propiedad
<br/>

No. Cuando escribes `Contenedor { contenido: texto }`, el String que era de
`texto` se **mueve** dentro del struct. A partir de esa línea, `texto` ya no es
un binding válido. La propiedad vive ahora en `c.contenido`.

---
layout: default
---

## Ejercicio 20: El préstamo básico
<br/>

```rust
fn calcular_longitud(s: &String) -> usize {
    s.len()
}

fn main() {
    let s1 = String::from("puente");
    let len = calcular_longitud(&s1); // Creamos una referencia
    println!("La longitud de '{}' es {}.", s1, len); // ✅ ¿Por qué esto sí es válido?
}
```

---
layout: default
---

## Respuesta 20: El préstamo básico
<br/>

Porque `&s1` crea una **referencia inmutable**: `calcular_longitud` toma
prestado el String sin reclamar su propiedad. Cuando la función termina, el
préstamo expira, y `s1` sigue siendo el dueño legítimo, disponible en el
`println!`.

---
layout: default
---

## Ejercicio 21: El lector que intentó escribir
<br/>

```rust
fn modificar(s: &String) {
    s.push_str(" extra"); // ❌ ¿Qué le falta a la firma para permitir esto?
}

fn main() {
    let mut s = String::from("hola");
    modificar(&s);
}
```

---
layout: default
---

## Respuesta 21: El lector que intentó escribir
<br/>

La firma debe usar una **referencia mutable** para permitir modificar el valor:

```rust
fn modificar(s: &mut String) {
    s.push_str(" extra");
}

fn main() {
    let mut s = String::from("hola");
    modificar(&mut s);
}
```

Dos cambios: `&mut String` en la firma y `&mut s` en la llamada. Además `s`
debe declararse `mut`.

---
layout: default
---

## Ejercicio 22: El doble escritor (Aliasing Mutable)
<br/>

```rust
fn main() {
    let mut s = String::from("dinámico");
    let r1 = &mut s;
    let r2 = &mut s; // ❌ ¿Por qué Rust prohíbe tener dos referencias mutables al mismo tiempo?
    println!("{}, {}", r1, r2);
}
```

---
layout: default
---

## Respuesta 22: El doble escritor (Aliasing Mutable)
<br/>

Rust prohíbe dos referencias mutables simultáneas al mismo dato para eliminar
las **carreras de datos** (data races). Si `r1` y `r2` pudieran modificar `s` a
la vez, cualquier suposición sobre el estado de la memoria sería inválida. La
regla es: un solo escritor **o** múltiples lectores, nunca ambos.

---
layout: default
---

## Ejercicio 23: El escritor tímido
<br/>

```rust
fn main() {
    let mut s = String::from("datos");
    let r1 = &s; // Lector
    let r2 = &s; // Lector
    let r3 = &mut s; // ❌ Escritor. ¿Por qué esto colapsa el universo de Rust?
    println!("{}, {}, {}", r1, r2, r3);
}
```

---
layout: default
---

## Respuesta 23: El escritor tímido
<br/>

El compilador aplica la regla de exclusión mutua: no puedes tener una referencia
mutable (`r3`) activa al mismo tiempo que referencias inmutables (`r1`, `r2`)
al mismo dato. Aquí las tres se usan en el mismo `println!`, por lo que sus
vidas se solapan. Si se permitiera, `r3` podría mover o invalidar la memoria
que `r1`/`r2` están leyendo.

---
layout: default
---

## Ejercicio 24: El ciclo de vida de una mirada (NLL)
<br/>

```rust
fn main() {
    let mut s = String::from("hola");
    let r1 = &s; 
    println!("{}", r1); // El lector r1 se usa aquí por última vez
    
    let r2 = &mut s; // 🤔 ¿Por qué este código SÍ compila a pesar del Ejercicio 11?
    r2.push_str(" mundo");
}
```

---
layout: default
---

## Respuesta 24: El ciclo de vida de una mirada (NLL)
<br/>

Gracias a **Non-Lexical Lifetimes (NLL)**, el compilador moderno calcula el
alcance real de cada referencia basándose en su **último uso**, no en las llaves
del bloque. `r1` se usa por última vez en su `println!`; después de esa línea,
su préstamo termina. Cuando se crea `r2 = &mut s`, ya no hay ninguna referencia
activa que compita, por lo que el código es válido.

---
layout: default
---

## Ejercicio 25: Referencias a porciones (Slices)
<br/>

```rust
fn main() {
    let mut v = vec![1, 2, 3, 4, 5];
    let slice = &v[0..3]; // Tomamos prestada una parte (Lectura)
    v.push(6); // ❌ Intentamos modificar el vector original. ¿Por qué da error?
    println!("{:?}", slice);
}
```

---
layout: default
---

## Respuesta 25: Referencias a porciones (Slices)
<br/>

`slice = &v[0..3]` establece un **préstamo inmutable** del vector. Mientras
`slice` esté vivo, el vector está "bloqueado" para lecturas. `v.push(6)` exige
un préstamo mutable, lo que viola la regla: no puedes combinar préstamos
mutables con inmutables activos sobre el mismo dato.

---
layout: default
---

## Ejercicio 26: Desreferenciación (Entrar al Heap)
<br/>

```rust
fn main() {
    let mut x = 10;
    let r = &mut x;
    // Modifica el valor interno de x a través de 'r' para que valga 20.
    // Pista: Usa el operador asterisco (*).
}
```

---
layout: default
---

## Respuesta 26: Desreferenciación
<br/>

```rust
fn main() {
    let mut x = 10;
    let r = &mut x;
    *r = 20; // Entra al Heap/Stack a través del puntero y cambia el valor
    println!("{}", x); // Imprime 20
}
```

El operador `*` **desreferencia** el puntero, permitiendo leer o escribir
el valor al que apunta.

---
layout: default
---

## Ejercicio 27: La referencia que apunta a la nada
<br/>

```rust
fn main() {
    let r;
    {
        let x = 5;
        r = &x; 
    } // x muere aquí
    println!("r: {}", r); // ❌ ¿Cuál es el error conceptual de espacio-tiempo aquí?
}
```

---
layout: default
---

## Respuesta 27: La referencia que apunta a la nada
<br/>

Error conceptual: **dangling reference** (referencia colgante). `x` vive solo
dentro del bloque interno `{}`. Cuando ese bloque termina, `x` se destruye y su
memoria se libera. `r` apuntaría a una dirección de memoria inválida. Rust lo
detecta en tiempo de compilación y lo prohíbe.

---
layout: default
---

## Ejercicio 28: El dilema de la función simple
<br/>

```rust
// ❌ Arregla la firma de esta función usando anotaciones de lifetimes ('a)
fn devolver_uno(x: &str, y: &str) -> &str {
    x
}

fn main() {
    let a = "hola";
    let b = "mundo";
    let res = devolver_uno(a, b);
}
```

---
layout: default
---

## Respuesta 28: El dilema de la función simple
<br/>

El compilador no puede inferir de cuál parámetro proviene la referencia
devuelta. Debes anotarlo explícitamente:

```rust
fn devolver_uno<'a>(x: &'a str, y: &'a str) -> &'a str {
    x
}
```

Esto le dice al compilador: "la referencia que devuelvo vive al menos tanto
como el parámetro `x` (y `y`, dado que ambos usan `'a`)."

---
layout: default
---

## Ejercicio 29: El eslabón más débil
<br/>

```rust
fn elegir<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

fn main() {
    let s1 = String::from("cadena_larga");
    let res;
    {
        let s2 = String::from("corta");
        res = elegir(&s1, &s2);
    } // s2 muere aquí. 
    println!("{}", res); // ❌ ¿Por qué falla si el resultado claramente iba a ser s1?
}
```

---
layout: default
---

## Respuesta 29: El eslabón más débil
<br/>

El contrato `<'a>` le dice al compilador: "el resultado vive a lo sumo tanto
como **el más corto** de los dos parámetros". Aunque en tiempo de ejecución el
resultado siempre sería `s1`, el compilador no hace análisis de flujo de valores;
trabaja con el tipo y las anotaciones. Como `s2` muere antes de que `res` sea
usado, la garantía se rompe desde el punto de vista del sistema de tipos.

Solución: darle a `s2` el mismo o mayor alcance que `res`, o usar `'static`.

---
layout: default
---

## Ejercicio 30: Structs con pasajeros prestados
<br/>

```rust
// ❌ Corrige este struct para que acepte una referencia
struct Perfil {
    nombre: &str, 
}

fn main() {
    let nombre_usuario = String::from("Carlos");
    let p = Perfil { nombre: &nombre_usuario };
}
```

---
layout: default
---

## Respuesta 30: Structs con pasajeros prestados
<br/>

Un struct que contiene una referencia debe declarar un lifetime para que el
compilador sepa que el struct no puede sobrevivir al dato al que apunta:

```rust
struct Perfil<'a> {
    nombre: &'a str,
}
```

---
layout: default
---

## Ejercicio 31: Mezclando Lifetimes diferentes
<br/>

```rust
// Imagina que 'x' e 'y' no tienen nada que ver entre sí.
// Modifica la firma para que el retorno dependa ÚNICAMENTE de la vida de 'x'.
fn procesar_separados(x: &str, y: &str) -> &str {
    x
}
```

---
layout: default
---

## Respuesta 31: Mezclando Lifetimes diferentes
<br/>

Cuando el retorno solo depende de `x`, se usan dos parámetros de lifetime
distintos:

```rust
fn procesar_separados<'a, 'b>(x: &'a str, y: &'b str) -> &'a str {
    x
}
```

Así `y` puede tener cualquier vida sin afectar la garantía del resultado.

---
layout: default
---

## Ejercicio 32: El ciudadano eterno
<br/>

```rust
struct Mensaje<'a> {
    texto: &'a str,
}

fn main() {
    let m;
    {
        let literal = "Hola, soy estático"; // Vive en el binario (rodata)
        m = Mensaje { texto: literal };
    }
    println!("{}", m.texto); // 🤔 ¿Por qué esto SÍ compila perfectamente? ¿Qué lifetime tiene un literal?
}
```

---
layout: default
---

## Respuesta 32: El ciudadano eterno
<br/>

Los literales de cadena (`"..."`) tienen lifetime `'static`: están embebidos
directamente en el binario del programa (sección `.rodata`) y **viven durante
toda la ejecución**. Por eso el compilador acepta que `m.texto` sea válido
fuera del bloque interno; la memoria del literal nunca se libera.

---
layout: default
---

## Ejercicio 33: Métodos con Lifetimes
<br/>

```rust
struct Descriptor<'a> {
    info: &'a str,
}

// ❌ Completa la sintaxis de 'impl' para que el método pueda retornar la referencia interna
impl Descriptor {
    fn obtener_info(&self) -> &str {
        self.info
    }
}
```

---
layout: default
---

## Respuesta 33: Métodos con Lifetimes
<br/>

El bloque `impl` debe incluir el parámetro de lifetime del struct:

```rust
impl<'a> Descriptor<'a> {
    fn obtener_info(&self) -> &str {
        self.info
    }
}
```

El lifetime del valor retornado se infiere por las reglas de elision: está
ligado al de `&self`, lo que es correcto porque `self.info` no puede
sobrevivir al struct.

---
layout: default
---

## Ejercicio 34: El vector devorado
<br/>

```rust
fn procesar_primer_elemento(v: Vec<String>) {
    if let Some(primero) = v.first() {
        println!("Primero: {}", primero);
    }
}

fn main() {
    let mis_datos = vec![String::from("A"), String::from("B")];
    procesar_primer_elemento(mis_datos);
    println!("Total elementos: {}", mis_datos.len()); // ❌ ¿Por qué el vector entero dejó de existir?
}
```

---
layout: default
---

## Respuesta 34: El vector devorado
<br/>

La función recibe `Vec<String>` **por valor**, tomando propiedad del vector
completo. Aunque solo usa el primer elemento, el vector entero fue consumido
al cruzar la barrera de la función. Después de la llamada, `mis_datos` ya no
existe.

Corrección: cambiar la firma a `fn procesar_primer_elemento(v: &Vec<String>)`
o `v: &[String]`.

---
layout: default
---

## Ejercicio 35: Extracción parcial de Tuplas
<br/>

```rust
fn main() {
    let tupla = (String::from("Llave"), String::from("Valor"));
    let llave = tupla.0; // Extraemos el primer elemento
    println!("Llave: {}", llave);
    println!("Tupla completa: {:?}", tupla); // ❌ ¿Por qué la tupla quedó "parcialmente destruída"?
}
```

---
layout: default
---

## Respuesta 35: Extracción parcial de Tuplas
<br/>

Al hacer `let llave = tupla.0`, se **mueve** el primer elemento de la tupla
fuera de ella. La tupla queda parcialmente destruida: `tupla.0` ya no tiene
dueño válido, así que la tupla entera se vuelve inutilizable como unidad.
Rust no permite usar un valor del que algún campo fue movido.

Corrección: clonar (`tupla.0.clone()`) o desestructurar completa en un único
`let (llave, valor) = tupla;`.

---
layout: default
---

## Ejercicio 36: El Option insaciable
<br/>

```rust
fn revisar_opcional(opt: Option<String>) {
    match opt {
        Some(texto) => println!("Texto: {}", texto),
        None => println!("Vacío"),
    }
}

fn main() {
    let mi_opcion = Some(String::from("Contenido"));
    revisar_opcional(mi_opcion);
    // 🤔 ¿Cómo podrías revisar 'mi_opcion' sin que la función le robe la propiedad?
}
```

---
layout: default
---

## Respuesta 36: El Option insaciable
<br/>

La función toma `Option<String>` por valor. Para no ceder la propiedad:

```rust
revisar_opcional(mi_opcion.as_ref()); // Convierte a Option<&String>
// o
revisar_opcional(&mi_opcion);         // Presta el Option completo
```

Y ajustar la firma a `fn revisar_opcional(opt: Option<&String>)` o
`fn revisar_opcional(opt: &Option<String>)`.

---
layout: default
---

## Ejercicio 37: Reemplazo en estructuras mutables
<br/>

```rust
struct Nodo {
    valor: String,
}

fn main() {
    let mut n = Nodo { valor: String::from("Viejo") };
    let extraido = n.valor; // ❌ Intentas sacar la propiedad dejando el struct vacío.
    n.valor = String::from("Nuevo");
    // Pista: Investiga std::mem::replace o std::mem::take para solucionar esto.
}
```

---
layout: default
---

## Respuesta 37: Reemplazo en estructuras mutables
<br/>

Mover `n.valor` directamente deja el campo en estado no inicializado, lo que
Rust no permite si el struct debe seguir siendo válido. La solución idiomática:

```rust
// Opción 1: replace (intercambia el valor por otro)
let extraido = std::mem::replace(&mut n.valor, String::from("Nuevo"));

// Opción 2: take (reemplaza por el default del tipo)
let extraido = std::mem::take(&mut n.valor);
n.valor = String::from("Nuevo");
```

---
layout: default
---

## Ejercicio 38: El Closure acaparador
<br/>

```rust
fn main() {
    let texto = String::from("Datos del sistema");
    let imprimir = || println!("{}", texto);
    
    let manejar_hilo = std::thread::spawn(imprimir); // ❌ El hilo exige que el closure tenga propiedad total.
    manejar_hilo.join().unwrap();
    // Pista: Necesitas usar la palabra clave 'move' antes de las barras del closure.
}
```

---
layout: default
---

## Respuesta 38: El Closure acaparador
<br/>

Los hilos en Rust exigen que todo lo que capturan tenga lifetime `'static` (o
sea propiedad del closure). `imprimir` captura `texto` por referencia, pero esa
referencia podría expirar antes de que el hilo termine. La solución es `move`:

```rust
let imprimir = move || println!("{}", texto);
```

Ahora el closure es **dueño** de `texto`, y puede vivir indefinidamente en el hilo.

---
layout: default
---

## Ejercicio 39: Clonación selectiva en bucles
<br/>

```rust
fn main() {
    let plantilla = String::from("Usuario: ");
    let nombres = vec!["Ana", "Pedro", "Luis"];
    let mut registros = Vec::new();

    for nombre in nombres {
        let mut registro = plantilla; // ❌ Falla en la segunda iteración.
        registro.push_str(nombre);
        registros.push(registro);
    }
}
```

---
layout: default
---

## Respuesta 39: Clonación selectiva en bucles
<br/>

En la primera iteración, `plantilla` se mueve dentro del bucle. En la segunda,
ya no existe. Solución: clonar en cada iteración.

```rust
let mut registro = plantilla.clone();
```

---
layout: default
---

## Ejercicio 40: La trampa del método .to_string()
<br/>

```rust
fn main() {
    let literal = "datos_estáticos";
    let s1 = literal.to_string();
    let s2 = s1; // Transferencia
    println!("{}", s1); // ❌ Falla. ¿Por qué el .to_string() genera una variable con Ownership en el Heap?
}
```

---
layout: default
---

## Respuesta 40: La trampa del método .to_string()
<br/>

`.to_string()` (y `.to_owned()`) **asigna un nuevo String en el Heap** con sus
propias reglas de ownership. A diferencia de un `&str` literal, el `String`
resultante no es `Copy`. Al hacer `let s2 = s1`, se transfiere la propiedad,
invalidando `s1`.

---
layout: default
---

## Ejercicio 41: El tipo Box\<T\> (Punteros Inteligentes)
<br/>

```rust
fn main() {
    let b1 = Box::new(String::from("Datos en el Heap profundo"));
    let b2 = b1; 
    // 🤔 ¿Box<T> se comporta igual que los tipos primitivos del Stack
    //    o hereda las leyes de Ownership del String?
}
```

---
layout: default
---

## Respuesta 41: El tipo Box\<T\>
<br/>

`Box<T>` **hereda las leyes de Ownership**. Es un puntero inteligente que posee
el dato en el Heap. Al hacer `let b2 = b1`, se mueve la propiedad del `Box`
(y del dato que contiene) a `b2`. `b1` queda inválido, igual que con `String`.

---
layout: default
---

## Ejercicio 42: Vaciando colecciones con .drain()
<br/>

```rust
fn main() {
    let mut palabras = vec![String::from("uno"), String::from("dos")];
    for p in palabras.drain(..) {
        println!("Procesando: {}", p);
    }
    println!("Elementos restantes: {}", palabras.len()); // 🤔 ¿Compila? ¿Qué estado tiene el vector ahora?
}
```

---
layout: default
---

## Respuesta 42: Vaciando colecciones con .drain()
<br/>

Sí compila. `.drain(..)` vacía el vector durante la iteración pero **no consume
el vector en sí**: la propiedad del `Vec` permanece en `palabras`. Al terminar
el bucle, `palabras` sigue existiendo, solo que vacío. `palabras.len()` devuelve
`0`.

---
layout: default
---

## Ejercicio 43: Pérdida de propiedad por indexación directa
<br/>

```rust
fn main() {
    let nombres = vec![String::from("Alex"), String::from("Maria")];
    let primero = nombres[0]; // ❌ ¿Por qué no puedes mover un elemento directamente usando índices?
    println!("{}", primero);
}
```

---
layout: default
---

## Respuesta 43: Pérdida de propiedad por indexación directa
<br/>

El operador de indexación `[]` devuelve una **referencia** al elemento, no el
elemento en sí. No se puede mover un valor fuera de un vector por índice porque
dejaría esa posición del vector en un estado no inicializado (hueco en la
memoria del `Vec`), lo que Rust no permite. Para extraer elementos usa
`.remove(0)`, `.pop()`, o `.swap_remove(0)`.

---
layout: default
---

## Ejercicio 44: La función constructora
<br/>

```rust
struct Config {
    ruta: String,
}

impl Config {
    fn new(r: String) -> Self {
        Config { ruta: r } // 🤔 ¿Quién tiene la propiedad de 'r' al finalizar esta función?
    }
}

fn main() {
    let path = String::from("/var/log");
    let c = Config::new(path);
}
```

---
layout: default
---

## Respuesta 44: La función constructora
<br/>

Al llamar `Config::new(path)`, la propiedad del String pasa al parámetro `r`.
Dentro de `new`, `r` se mueve al campo `ruta` del struct. Al retornar, el
struct (que ahora posee el String) se mueve a `c`. Al finalizar `main`, `c`
sale de alcance y el String se destruye.

**`Config` (a través de `c`) tiene la propiedad final.**

---
layout: default
---

## Ejercicio 45: Desestructuración con patrones (match)
<br/>

```rust
fn main() {
    let resultado: Result<String, i32> = Ok(String::from("Éxito"));
    if let Ok(texto) = resultado {
        println!("{}", texto);
    }
    // ❌ Si intentas usar 'resultado' aquí abajo, fallará.
    //    ¿Cómo evitas que 'if let' consuma la propiedad?
}
```

---
layout: default
---

## Respuesta 45: Desestructuración con patrones (match)
<br/>

`if let Ok(texto) = resultado` mueve el `String` contenido en `Ok`. Para evitar
consumir la propiedad, desestrctura una referencia:

```rust
if let Ok(texto) = &resultado {   // texto: &String
    println!("{}", texto);
}
println!("{:?}", resultado); // Sigue siendo válido
```

---
layout: default
---

## Ejercicio 46: Asignaciones encadenadas
<br/>

```rust
fn main() {
    let mut a = String::from("materia");
    let b = a;
    let c = b;
    a = c; // 🤔 ¿Esto es válido en Rust? Analiza el viaje de la propiedad bit a bit.
    println!("{}", a);
}
```

---
layout: default
---

## Respuesta 46: Asignaciones encadenadas
<br/>

Sí, es completamente válido. El viaje de la propiedad:

1. `a` posee "materia".
2. `let b = a;` → `b` posee "materia", `a` inválido.
3. `let c = b;` → `c` posee "materia", `b` inválido.
4. `a = c;`     → `a` vuelve a poseer "materia", `c` inválido.

En la línea del `println!`, `a` es el dueño legítimo.

---
layout: default
---

## Ejercicio 47: Mutabilidad heredada en colecciones
<br/>

```rust
fn main() {
    let mut lista = vec![String::from("Trigo")];
    let elemento = lista.pop().unwrap(); // Sacamos el elemento
    // 🤔 'elemento' fue extraído de un vector mutable. ¿Es 'elemento' mutable por defecto?
    // Intenta hacer: elemento.push_str(" limpio");
}
```

---
layout: default
---

## Respuesta 47: Mutabilidad heredada en colecciones
<br/>

No. `elemento` **no es mutable por defecto**. La mutabilidad no se hereda del
contenedor. El binding `elemento` es inmutable a menos que lo declares
explícitamente:

```rust
let mut elemento = lista.pop().unwrap();
elemento.push_str(" limpio"); // Ahora sí compila
```

---
layout: default
---

## Ejercicio 48: Shadowing vs Ownership Transfer
<br/>

```rust
fn main() {
    let x = String::from("Alfa");
    let x = String::from("Beta"); // Shadowing
    // 🤔 ¿La memoria de "Alfa" se liberó inmediatamente o sigue existiendo
    //    en el Heap hasta el fin del main?
}
```

---
layout: default
---

## Respuesta 48: Shadowing vs Ownership Transfer
<br/>

Con shadowing, la primera variable (`"Alfa"`) **no se destruye inmediatamente**
en el punto del shadowing. Ambas existen como bindings distintos en el mismo
scope. En Rust, el orden de destrucción es el **inverso al de declaración**,
al finalizar el scope. Por tanto:

1. Al cerrar `main`, primero se destruye el segundo `x` → libera "Beta".
2. Luego se destruye el primer `x` → libera "Alfa".

`"Alfa"` vive en el Heap hasta el fin de `main`.

---
layout: default
---

## Ejercicio 49: Propiedad en Enumeraciones Complejas
<br/>

```rust
enum Mensaje {
    Texto(String),
    Salir,
}

fn procesar(m: Mensaje) { /* Reclama propiedad */ }

fn main() {
    let m = Mensaje::Texto(String::from("Alerta"));
    procesar(m);
    // ❌ ¿Puedes usar 'm' si el enum por dentro contenía un String?
}
```

---
layout: default
---

## Respuesta 49: Propiedad en Enumeraciones Complejas
<br/>

No. Aunque el variant sea `Texto(String)`, el enum completo (`m`) se mueve a
`procesar(m)`. La presencia de un `String` dentro del enum hace que el enum
entero no sea `Copy`. Después de la llamada, `m` ya no es accesible.

---
layout: default
---

## Ejercicio 50: El operador de descarte (_)
<br/>

```rust
fn main() {
    let s = String::from("Materia efímera");
    let _ = s; // Descarte inmediato
    println!("{}", s); // ❌ ¿Por qué el guión bajo destruye o invalida la variable al instante?
}
```

---
layout: default
---

## Respuesta 50: El operador de descarte (_)
<br/>

`let _ = s;` **mueve** `s` hacia el patrón `_`, que descarta el valor
**inmediatamente** al final del statement (no al final del scope). Esto es
diferente a `_nombre`, que sí crea un binding y vive hasta el fin del scope.
El resultado: `s` queda inválido en la siguiente línea.

---
layout: default
---

## Ejercicio 51: Mutabilidad en cascada a través de funciones
<br/>

```rust
fn agregar_prefijo(s: &mut String) {
    s.insert_str(0, "Pre-");
}

fn main() {
    let s = String::from("config"); // ❌ ¿Qué le falta a esta variable para cruzar el túnel mutable?
    agregar_prefijo(&mut s);
}
```

---
layout: default
---

## Respuesta 51: Mutabilidad en cascada a través de funciones
<br/>

La variable `s` debe declararse `mut` para poder prestarla como referencia
mutable:

```rust
let mut s = String::from("config");
agregar_prefijo(&mut s);
```

---
layout: default
---

## Ejercicio 52: La referencia del Iterator
<br/>

```rust
fn main() {
    let mut numeros = vec![1, 2, 3];
    for n in &numeros { // Prestamos el vector como lectura
        numeros.push(*n); // ❌ Intentas modificar la colección mientras el bucle la lee. ¿Por qué truena?
    }
}
```

---
layout: default
---

## Respuesta 52: La referencia del Iterator
<br/>

El bucle `for n in &numeros` crea un **préstamo inmutable** del vector que dura
todo el ciclo. `numeros.push(*n)` exige un préstamo mutable. Rust prohíbe tener
ambos activos simultáneamente: la regla es "lectores múltiples O un escritor,
no los dos".

---
layout: default
---

## Ejercicio 53: El préstamo en funciones puras
<br/>

```rust
fn es_largo(s: &str) -> bool {
    s.len() > 10
}

fn main() {
    let mut texto = String::from("Inmutable durante la lectura");
    let r = &texto;
    let chequeo = es_largo(r); // 🤔 ¿Puede una función aceptar una referencia de otra referencia?
    println!("¿Es largo? {}", chequeo);
}
```

---
layout: default
---

## Respuesta 53: El préstamo en funciones puras
<br/>

Sí. Rust aplica **deref coercion**: `&String` se convierte automáticamente a
`&str` al pasar como argumento. Además, pasar `r` (que es `&String`) a una
función que acepta `&str` es válido: es un préstamo de un préstamo, y el
compilador lo resuelve transparentemente.

---
layout: default
---

## Ejercicio 54: Préstamos simultáneos en Structs
<br/>

```rust
struct Punto {
    x: i32,
    y: i32,
}

fn main() {
    let mut p = Punto { x: 10, y: 20 };
    let r1 = &mut p.x; // Modifica X
    let r2 = &mut p.y; // Modifica Y
    // 🤔 ¿Por qué Rust permite dos referencias mutables al mismo struct si apuntan a campos diferentes?
    *r1 += 1;
    *r2 += 1;
}
```

---
layout: default
---

## Respuesta 54: Préstamos simultáneos en Structs
<br/>

El borrow checker es suficientemente inteligente para distinguir **campos no
solapados** del mismo struct. `&mut p.x` y `&mut p.y` apuntan a regiones de
memoria distintas y no hay posibilidad de aliasing. Rust permite esta
bifurcación (split borrow) porque puede garantizar que no existe conflicto.

---
layout: default
---

## Ejercicio 55: El bloqueo por alcance estructural
<br/>

```rust
struct Monitor {
    estado: String,
}

fn main() {
    let mut m = Monitor { estado: String::from("Activo") };
    let ref_estado = &m.estado;    // Bloqueo de lectura en un campo
    let ref_struct = &mut m;       // ❌ Intento de bloqueo mutable del struct completo.
    println!("{}", ref_estado);
}
```

---
layout: default
---

## Respuesta 55: El bloqueo por alcance estructural
<br/>

`ref_estado = &m.estado` establece un préstamo inmutable sobre parte del struct.
`&mut m` exigiría un préstamo mutable del struct **completo**, lo que incluye
`m.estado`. Esto violaría la regla: no se puede tener un préstamo mutable de
algo mientras hay un préstamo inmutable activo sobre cualquier parte de él.

---
layout: default
---

## Ejercicio 56: Referencias mutables dentro de condicionales
<br/>

```rust
fn main() {
    let mut v = vec![1, 2, 3];
    let r = &mut v;
    if r.len() > 0 {
        r.push(4); // 🤔 ¿Por qué es seguro leer la longitud y luego modificar usando el mismo puntero mutable?
    }
}
```

---
layout: default
---

## Respuesta 56: Referencias mutables dentro de condicionales
<br/>

Existe una sola referencia mutable `r`. Usar `r.len()` (lectura a través de
`&mut`) y `r.push(4)` (escritura a través de `&mut`) sobre el **mismo** puntero
no crea aliasing. Las restricciones de Rust son sobre referencias **distintas**
al mismo dato, no sobre operaciones sucesivas a través de la misma referencia.
El código es completamente seguro y válido.

---
layout: default
---

## Ejercicio 57: El vector que se fue de gira
<br/>

```rust
fn main() {
    let nombres = vec![String::from("ana"), String::from("beto")];
    for n in nombres.into_iter() {
        println!("{n}");
    }
    println!("quedan {}", nombres.len());
}
```

🤔 El bucle recorre los nombres y luego se pide el largo del vector. ¿Compila?

---
layout: default
---

## Respuesta 57: El vector que se fue de gira
<br/>

No compila: **E0382, borrow of moved value: `nombres`**.

`into_iter()` toma la propiedad del vector para entregar los elementos por valor. Al
terminar el bucle, `nombres` ya no existe.

```rust
    for n in nombres.iter() {        // o: for n in &nombres
        println!("{n}");
    }
    println!("quedan {}", nombres.len());   // 2
```

Regla: `iter()` presta, `into_iter()` consume. El `for x in v` sin `&` es la segunda.

---
layout: default
---

## Ejercicio 58: Modificar la lista mientras se lee
<br/>

```rust
fn main() {
    let mut v = vec![1, 2, 3];
    for n in &v {
        if *n == 2 {
            v.push(99);
        }
    }
}
```

❌ Se recorre el vector y, al encontrar el 2, se agrega un elemento. ¿Qué dice el compilador?

---
layout: default
---

## Respuesta 58: Modificar la lista mientras se lee
<br/>

**E0502: cannot borrow `v` as mutable because it is also borrowed as immutable.**

El `for` mantiene vivo un préstamo inmutable durante todo el bucle, y `push` pide uno
mutable. Es la regla 1 del borrow checker, y aquí protege algo concreto: `push` puede
reasignar el buffer y dejar al iterador apuntando a memoria vieja.

```rust
    let posiciones: Vec<usize> = v.iter()
        .enumerate().filter(|(_, n)| **n == 2).map(|(i, _)| i).collect();
    for _ in posiciones { v.push(99); }   // el préstamo ya terminó
```

---
layout: default
---

## Ejercicio 59: Sacar un elemento por su índice
<br/>

```rust
fn main() {
    let palabras = vec![String::from("hola")];
    let primera = palabras[0];
    println!("{primera}");
}
```

🤔 Se quiere la primera palabra del vector. ¿Por qué falla algo tan simple?

---
layout: default
---

## Respuesta 59: Sacar un elemento por su índice
<br/>

**E0507: cannot move out of index of `Vec<String>`.**

Indexar no copia: intenta *mover* el `String` fuera del vector, y eso dejaría un
hueco en una posición que el vector sigue creyendo válida. Con `Vec<i32>` sí
funcionaría, porque `i32` es `Copy`.

Tres salidas, según lo que se quiera:

```rust
let primera = &palabras[0];            // prestarla
let primera = palabras[0].clone();     // copiarla
let primera = palabras.remove(0);      // sacarla de verdad del vector
```

---
layout: default
---

## Ejercicio 60: El map que no hizo nada
<br/>

```rust
fn main() {
    let v = vec![1, 2, 3];
    v.iter().map(|n| n * 2);
    println!("{v:?}");       // [1, 2, 3]
}
```

🤔 El código compila y corre, pero el vector sale intacto. ¿Por qué?

---
layout: default
---

## Respuesta 60: El map que no hizo nada
<br/>

Compila, con una advertencia que lo dice todo: **unused `Map` that must be used**,
y la nota *iterators are lazy and do nothing unless consumed*.

`map` no recorre nada: construye un iterador que describe la operación. Sin
consumidor, nadie llama a `next` y nadie ejecuta el closure.

```rust
let doblados: Vec<i32> = v.iter().map(|n| n * 2).collect();   // [2, 4, 6]
```

Y `map` nunca modifica el original: devuelve valores nuevos. Para cambiar en su
lugar hace falta `iter_mut`.

---
layout: default
---

## Ejercicio 61: Vaciar un Option prestado
<br/>

```rust
fn tomar(opt: &mut Option<String>) -> Option<String> {
    *opt
}
```

❌ La función recibe el `Option` por referencia mutable y quiere devolver su contenido. ¿Compila?

---
layout: default
---

## Respuesta 61: Vaciar un Option prestado
<br/>

**E0507: cannot move out of `*opt` which is behind a mutable reference.**

`opt` es un préstamo, no el dueño. Mover el valor afuera dejaría al dueño real con un
hueco detrás de una referencia que sigue viva.

```rust
fn tomar(opt: &mut Option<String>) -> Option<String> {
    opt.take()       // deja None en su lugar y devuelve lo que había
}
```

`Option::take` es `mem::replace(self, None)`: intercambia en vez de sacar, así que en
ningún instante hay un hueco.

---
layout: default
---

## Ejercicio 62: El valor del mapa
<br/>

```rust
use std::collections::HashMap;

fn main() {
    let mut mapa = HashMap::new();
    mapa.insert("a", String::from("uno"));
    let valor = mapa["a"];
    println!("{valor}");
}
```

🤔 Se busca el valor de una llave en un `HashMap<&str, String>`. ¿Cuál es el problema?

---
layout: default
---

## Respuesta 62: El valor del mapa
<br/>

**E0507: cannot move out of index of `HashMap<&str, String>`.**

Es el mismo error del ejercicio 59: indexar un mapa devuelve el valor por
referencia, y asignarlo a una variable intenta moverlo fuera de la estructura.

```rust
let valor = &mapa["a"];              // prestado
let valor = mapa["a"].clone();       // copiado
let valor = mapa.get("a");           // Option<&String>, sin panic
```

`mapa["a"]` además hace *panic* si la llave no existe. `get` devuelve `Option`.

---
layout: default
---

## Ejercicio 63: El collect indeciso
<br/>

```rust
fn main() {
    let v = vec![1, 2, 3];
    let doblados = v.iter().map(|n| n * 2).collect();
    println!("{doblados:?}");
}
```

❌ El `collect` no dice a dónde va. ¿Qué reclama el compilador?

---
layout: default
---

## Respuesta 63: El collect indeciso
<br/>

**E0283: type annotations needed**, con la nota *cannot satisfy
`_: FromIterator<i32>`*.

`collect` puede producir un `Vec`, un `HashSet`, un `String` o cualquier tipo que
implemente `FromIterator`. Sin destino declarado, el compilador no tiene manera de
elegir. Dos formas de decírselo:

```rust
let doblados: Vec<i32> = v.iter().map(|n| n * 2).collect();
let doblados = v.iter().map(|n| n * 2).collect::<Vec<i32>>();
```

---
layout: default
---

## Ejercicio 64: Sumarle diez a cada elemento
<br/>

```rust
fn main() {
    let mut v = vec![1, 2, 3];
    for n in v.iter() {
        *n += 10;
    }
}
```

🤔 El vector es `mut` y el bucle intenta modificar cada elemento. ¿Basta con eso?

---
layout: default
---

## Respuesta 64: Sumarle diez a cada elemento
<br/>

No: **E0594, cannot assign to `*n`, which is behind a `&` reference**. Y de paso
otra advertencia, *variable does not need to be mutable*, que delata el problema: el
`mut` del vector no se está usando.

`iter()` entrega `&T`, de solo lectura. Que el dueño sea mutable no vuelve mutables
los préstamos que reparte.

```rust
    for n in v.iter_mut() {   // entrega &mut i32
        *n += 10;
    }                          // [11, 12, 13]
```

Las tres formas: `iter()` da `&T`, `iter_mut()` da `&mut T`, `into_iter()` da `T`.

---
layout: default
---

## Ejercicio 65: El nodo de tamaño infinito
<br/>

```rust
struct Nodo {
    valor: i32,
    siguiente: Option<Nodo>,
}
```

❌ Una lista enlazada declarada de la forma más directa. ¿Qué error da, y por qué?

---
layout: default
---

## Respuesta 65: El nodo de tamaño infinito
<br/>

**E0072: recursive type `Nodo` has infinite size.**

Rust necesita el tamaño exacto de cada tipo al compilar. `Nodo` contiene un `Nodo`,
que contiene otro: la cuenta no termina. El `Option` no salva nada, porque su tamaño
depende del de su variante más grande.

```rust
struct Nodo {
    valor: i32,
    siguiente: Option<Box<Nodo>>,   // ahora el campo mide un puntero
}
```

`Box` corta la recursión porque su tamaño no depende de `T`: siempre es un puntero.

---
layout: default
---

## Ejercicio 66: La cuenta de los dueños
<br/>

```rust
use std::rc::Rc;

fn main() {
    let a = Rc::new(String::from("dato"));
    let b = Rc::clone(&a);
    {
        let _c = Rc::clone(&a);
        println!("dentro: {}", Rc::strong_count(&a));
    }
    println!("fuera: {}", Rc::strong_count(&a));
}
```

🤔 Este código compila y corre. ¿Qué imprime en cada línea?

---
layout: default
---

## Respuesta 66: La cuenta de los dueños
<br/>

`dentro: 3` y `fuera: 2`.

Dentro del bloque hay tres dueños vivos: `a`, `b` y `_c`. Al cerrar el bloque, `_c`
sale de scope, su `Drop` decrementa el contador y quedan dos.

El valor no se libera hasta que el contador llega a cero, o sea cuando mueran también
`a` y `b` al terminar `main`. `Rc::clone` no duplica el `String`: solo suma uno al
contador, y eso es todo lo que cuesta.

---
layout: default
---

## Ejercicio 67: Modificar lo compartido
<br/>

```rust
use std::rc::Rc;

struct Config { nivel: u8 }

fn main() {
    let c = Rc::new(Config { nivel: 1 });
    let otro = Rc::clone(&c);
    otro.nivel = 2;
}
```

❌ Dos dueños del mismo dato, y uno intenta cambiarlo. ¿Compila?

---
layout: default
---

## Respuesta 67: Modificar lo compartido
<br/>

**E0594: cannot assign to data in an `Rc`**, con la ayuda *trait `DerefMut` is
required to modify through a dereference, but it is not implemented for `Rc<Config>`*.

`Rc` resuelve la propiedad múltiple, no la mutación. Con dos dueños vivos no existe
acceso exclusivo, que es lo que la regla 1 del borrow checker exige para mutar. Por
eso `Rc` no implementa `DerefMut`.

```rust
let c = Rc::new(RefCell::new(Config { nivel: 1 }));
let otro = Rc::clone(&c);
otro.borrow_mut().nivel = 2;      // la regla se verifica en ejecución
```

---
layout: default
---

## Ejercicio 68: El que compila pero no corre
<br/>

```rust
use std::cell::RefCell;

fn main() {
    let celda = RefCell::new(vec![1, 2, 3]);
    let lectura = celda.borrow();
    celda.borrow_mut().push(4);
    println!("{lectura:?}");
}
```

🤔 Compila sin una sola advertencia. ¿Qué pasa al ejecutarlo?

---
layout: default
---

## Respuesta 68: El que compila pero no corre
<br/>

Aborta: **thread 'main' panicked at: RefCell already borrowed**.

`RefCell` no elimina la regla de borrowing, la mueve al tiempo de ejecución. El
guard que devuelve `borrow()` sigue vivo porque `lectura` se usa en la última línea,
así que `borrow_mut()` encuentra la bandera puesta y hace *panic*.

```rust
    let copia = celda.borrow().clone();   // el guard muere aquí
    celda.borrow_mut().push(4);
    println!("{copia:?}");
```

Quita el `println!` final y el mismo programa corre, porque NLL mata el guard antes.
El préstamo vale hasta donde llegue el guard.

---
layout: default
---

## Ejercicio 69: La colección de figuras
<br/>

```rust
trait Figura { fn area(&self) -> f64; }
struct Circulo(f64);
struct Cuadrado(f64);
// impl Figura para los dos...

fn main() {
    let figuras = vec![Circulo(1.0), Cuadrado(2.0)];
    for f in &figuras { println!("{}", f.area()); }
}
```

❌ Un vector con un círculo y un cuadrado, ambos implementan `Figura`. ¿Compila?

---
layout: default
---

## Respuesta 69: La colección de figuras
<br/>

**E0308: mismatched types.** Un `Vec<T>` exige que todos sus elementos sean del
mismo tipo `T`, e implementar el mismo trait no los vuelve el mismo tipo.

```rust
let figuras: Vec<Box<dyn Figura>> = vec![
    Box::new(Circulo(1.0)),
    Box::new(Cuadrado(2.0)),
];
```

Ahora el tipo del elemento es siempre el mismo puntero, y lo que cambia es a dónde
apunta. `dyn` borra el tipo concreto y `Box` le devuelve un tamaño.

---
layout: default
---

## Ejercicio 70: El trait que no puede ser dyn
<br/>

```rust
trait Duplicable { fn duplicar(&self) -> Self; }

struct Caja(i32);
impl Duplicable for Caja {
    fn duplicar(&self) -> Caja { Caja(self.0) }
}

fn main() {
    let v: Vec<Box<dyn Duplicable>> = vec![Box::new(Caja(1))];
}
```

🤔 El trait tiene un solo método y el tipo lo implementa. ¿Por qué no se puede guardar en un `Box<dyn>`?

---
layout: default
---

## Respuesta 70: El trait que no puede ser dyn
<br/>

**E0038: the trait `Duplicable` is not dyn compatible.**

`duplicar` devuelve `Self`. Detrás de un `dyn` no se sabe qué tipo es `Self`, así que
tampoco se sabe cuánto mide el valor de retorno ni cómo construir la entrada de la
tabla de métodos. Es la misma razón por la que no existe `Box<dyn Clone>`.

```rust
trait Duplicable {
    fn duplicar(&self) -> Self where Self: Sized;   // fuera de la tabla
    fn etiqueta(&self) -> String;                   // esta sí queda
}
```

El `where Self: Sized` deja ese método disponible solo por genérico, y el resto del
trait vuelve a servir como `dyn`.

---
layout: default
---

## Ejercicio 71: Los que nunca se liberan
<br/>

```rust
struct Nodo { valor: i32, otro: RefCell<Option<Rc<Nodo>>> }

impl Drop for Nodo {
    fn drop(&mut self) { println!("liberando {}", self.valor); }
}

fn main() {
    let a = Rc::new(Nodo { valor: 1, otro: RefCell::new(None) });
    let b = Rc::new(Nodo { valor: 2, otro: RefCell::new(None) });
    *a.otro.borrow_mut() = Some(Rc::clone(&b));
    *b.otro.borrow_mut() = Some(Rc::clone(&a));
    println!("fin de main");
}
```

🤔 Compila y corre sin error. Cada `Nodo` imprime al liberarse. ¿Qué sale?

---
layout: default
---

## Respuesta 71: Los que nunca se liberan
<br/>

Sale solo `fin de main`. **Ninguno de los dos `Drop` corre nunca.**

`a` apunta a `b` y `b` apunta a `a`, así que al terminar `main` cada contador baja de
2 a 1 y ninguno llega a cero. La memoria se filtra. Es código seguro: no hay acceso
inválido, solo memoria que nadie libera.

La salida es `Weak<T>`, una referencia que no cuenta como dueño:

```rust
*b.otro.borrow_mut() = Some(Rc::downgrade(&a));   // Weak, rompe el ciclo
```

Convención: los enlaces hacia abajo con `Rc`, los que regresan con `Weak`.

---
layout: default
---

## Ejercicio 72: El préstamo que se colgó solo
<br/>

```rust
impl Registro {
    fn agregar(&self, n: i32) {
        let items = self.items.borrow();
        if items.len() < 3 {
            self.items.borrow_mut().push(n);
        }
    }
}
```

❌ Un método que consulta antes de escribir, todo dentro del mismo tipo. Compila. ¿Corre?

---
layout: default
---

## Respuesta 72: El préstamo que se colgó solo
<br/>

Aborta en la primera llamada: **panicked at: RefCell already borrowed**.

El guard de `borrow()` está ligado a `items`, así que vive hasta el final del método.
Cuando la línea del `push` pide el préstamo mutable, el inmutable sigue puesto. El
`if` no cierra el préstamo: lo que lo cierra es la muerte del guard.

```rust
    fn agregar(&self, n: i32) {
        let cabe = self.items.borrow().len() < 3;   // el guard muere aquí
        if cabe {
            self.items.borrow_mut().push(n);
        }
    }
```

Regla práctica con `RefCell`: que ningún guard viva más de una expresión.

---
layout: default
---

## Ejercicio 73: El closure que se quedó corto
<br/>

```rust
use std::thread;

fn main() {
    let datos = vec![1, 2, 3];
    let h = thread::spawn(|| {
        println!("{datos:?}");
    });
    h.join().unwrap();
}
```

❌ Se lanza un hilo que imprime un vector declarado en `main`. ¿Qué falta?

---
layout: default
---

## Respuesta 73: El closure que se quedó corto
<br/>

**E0373: closure may outlive the current function, but it borrows `datos`, which is
owned by the current function.**

El closure toma `datos` prestado, pero el compilador no puede probar que el hilo
termine antes que `main`. Un préstamo que quizá sobreviva a su dueño es la regla 2 del
borrow checker, y aquí se aplica entre hilos.

```rust
    let h = thread::spawn(move || {   // se lleva la propiedad
        println!("{datos:?}");
    });
```

El `join()` no cuenta como prueba: el compilador exige `'static` en la firma de
`spawn`, sin importar lo que hagas después.

---
layout: default
---

## Ejercicio 74: El Rc que no cruzó
<br/>

```rust
use std::rc::Rc;
use std::thread;

fn main() {
    let compartido = Rc::new(vec![1, 2, 3]);
    let copia = Rc::clone(&compartido);
    let h = thread::spawn(move || println!("{copia:?}"));
    h.join().unwrap();
}
```

🤔 Se comparte un vector con un hilo usando `Rc`, y el closure sí lleva `move`. ¿Basta?

---
layout: default
---

## Respuesta 74: El Rc que no cruzó
<br/>

**E0277: `Rc<Vec<i32>>` cannot be sent between threads safely.**

El contador de `Rc` no es atómico: dos hilos incrementándolo a la vez pueden perder
una cuenta y liberar el valor todavía en uso. Por eso `Rc` no implementa `Send`, y el
compilador lo detiene al compilar en lugar de dejarlo fallar en ejecución.

```rust
use std::sync::Arc;
let compartido = Arc::new(vec![1, 2, 3]);
let copia = Arc::clone(&compartido);
```

`Arc` es el mismo tipo con el contador atómico. Paga un poco más por operación, y es
lo único que cambia.

---
layout: default
---

## Ejercicio 75: Contar con Arc
<br/>

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    let contador = Arc::new(0);
    let mut hilos = vec![];
    for _ in 0..4 {
        let c = Arc::clone(&contador);
        hilos.push(thread::spawn(move || { *c += 1; }));
    }
}
```

❌ Cuatro hilos incrementan un contador compartido con `Arc`. ¿Compila?

---
layout: default
---

## Respuesta 75: Contar con Arc
<br/>

**E0594: cannot assign to data in an `Arc`.**

Es el mismo error del ejercicio 67, ahora entre hilos. `Arc` resuelve *quién es el
dueño*, no *quién puede mutar*. Con cuatro dueños vivos no hay acceso exclusivo.

```rust
let contador = Arc::new(Mutex::new(0));
// ...
hilos.push(thread::spawn(move || { *c.lock().unwrap() += 1; }));
```

Son dos problemas y dos tipos: `Arc` por fuera para la propiedad compartida, `Mutex`
por dentro para la mutación. Es el `Rc<RefCell<T>>` del capítulo 6, entre hilos.

---
layout: default
---

## Ejercicio 76: El Mutex sin envoltura
<br/>

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
    let contador = Mutex::new(0);
    let mut hilos = vec![];
    for _ in 0..4 {
        hilos.push(thread::spawn(move || {
            *contador.lock().unwrap() += 1;
        }));
    }
}
```

🤔 Ahora sí hay `Mutex`, pero no `Arc`. Cada hilo lo usa directo. ¿Qué falla?

---
layout: default
---

## Respuesta 76: El Mutex sin envoltura
<br/>

**E0382: borrow of moved value: `contador`.**

El `move` del primer hilo se lleva el `Mutex` completo, así que en la segunda vuelta
del bucle ya no hay nada que mover. `Mutex` da exclusión mutua, no propiedad
compartida: sigue teniendo un solo dueño.

```rust
let contador = Arc::new(Mutex::new(0));
for _ in 0..4 {
    let c = Arc::clone(&contador);      // un dueño más por hilo
    hilos.push(thread::spawn(move || { *c.lock().unwrap() += 1; }));
}
```

`Arc<Mutex<T>>` aparece siempre junto porque cada uno resuelve la mitad.

---
layout: default
---

## Ejercicio 77: El clon fuera del bucle
<br/>

```rust
fn main() {
    let contador = Arc::new(Mutex::new(0));
    let c = Arc::clone(&contador);
    let mut hilos = vec![];
    for _ in 0..4 {
        hilos.push(thread::spawn(move || { *c.lock().unwrap() += 1; }));
    }
}
```

❌ Ya están `Arc` y `Mutex`, y hay un `Arc::clone`. Pero está en el lugar equivocado.

---
layout: default
---

## Respuesta 77: El clon fuera del bucle
<br/>

**E0382: use of moved value: `c`.**

Hay un solo clon para cuatro hilos. El primer `move` se lleva `c` y la segunda vuelta
del bucle ya no tiene qué mover. El `Arc::clone` va **dentro** del bucle, uno por
hilo:

```rust
    for _ in 0..4 {
        let c = Arc::clone(&contador);
        hilos.push(thread::spawn(move || { *c.lock().unwrap() += 1; }));
    }
```

Cada iteración crea su propio dueño. El contador de `Arc` llega a cinco y baja a uno
conforme los hilos terminan.

---
layout: default
---

## Ejercicio 78: El candado que se esperó a sí mismo
<br/>

```rust
use std::sync::Mutex;

fn main() {
    let m = Mutex::new(0);
    let a = m.lock().unwrap();
    let b = m.lock().unwrap();
    println!("{} {}", *a, *b);
}
```

🤔 Compila sin advertencias. ¿Qué imprime?

---
layout: default
---

## Respuesta 78: El candado que se esperó a sí mismo
<br/>

Nada. **El programa se cuelga para siempre** y hay que matarlo.

Es la diferencia entre `RefCell` y `Mutex`: uno aborta al detectar el segundo
préstamo, el otro **espera** a que se libere el primero. Y el primero lo tiene el
mismo hilo que está esperando, así que nadie lo va a soltar.

```rust
    let total = { let a = m.lock().unwrap(); *a };  // muere aquí
    let b = m.lock().unwrap();
```

Es el modo de falla que no tiene análogo mono-hilo. Dos candados distintos tomados en
distinto orden por dos hilos producen el mismo cuelgue.

---
layout: default
---

## Ejercicio 79: Los hilos que nadie esperó
<br/>

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        thread::sleep(Duration::from_millis(50));
        println!("desde el hilo");
    });
    println!("fin de main");
}
```

🤔 El hilo duerme 50 ms antes de imprimir, y `main` no llama a `join`. ¿Qué sale?

---
layout: default
---

## Respuesta 79: Los hilos que nadie esperó
<br/>

Solo `fin de main`. Probado tres veces, el mensaje del hilo no aparece nunca.

Cuando el hilo principal termina, el proceso termina y los demás hilos mueren donde
estén. `spawn` devuelve un `JoinHandle` justamente para poder esperarlos:

```rust
    let h = thread::spawn(|| { /* ... */ });
    println!("fin de main");
    h.join().unwrap();          // ahora sí espera
}
```

Y ojo con el `unwrap`: `join` devuelve `Result`, porque el hilo pudo hacer *panic*.

---
layout: default
---

## Ejercicio 80: Leer mientras se escribe
<br/>

```rust
use std::sync::{Arc, RwLock};

fn main() {
    let datos = Arc::new(RwLock::new(vec![1, 2, 3]));
    let escritura = datos.write().unwrap();
    println!("{}", datos.read().unwrap().len());
    println!("{}", escritura.len());
}
```

❌ Un `RwLock` permite muchos lectores. El código toma la escritura y luego lee. ¿Corre?

---
layout: default
---

## Respuesta 80: Leer mientras se escribe
<br/>

Se cuelga. `RwLock` admite **muchos lectores o un escritor**, nunca las dos cosas, y
el guard de escritura sigue vivo porque `escritura` se usa en la última línea.

Es la misma regla 1 del borrow checker, con la misma estructura de siempre: varias
`&` o una `&mut`. Lo único que cambia es que aquí violarla no es un error de
compilación ni un *panic*, sino una espera infinita.

```rust
    let n = datos.read().unwrap().len();   // el guard muere aquí
    datos.write().unwrap().push(4);
```

`RwLock` conviene cuando se lee mucho más de lo que se escribe. Si no, `Mutex` es más
simple y más rápido.
