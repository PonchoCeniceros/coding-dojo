---
layout: section
---

# Structs

---
layout: center
---

## ¿Qué es un struct?

1. Un **struct** agrupa varios valores relacionados bajo un solo tipo, cada uno con su propio nombre (*campo*) y tipo.
2. A diferencia de una tupla, cada campo tiene un nombre — el código ya no depende del orden para saber qué representa cada valor.

<br>

```rust
struct Punto {
    x: f64,
    y: f64,
}

fn main() {
    let origen = Punto { x: 0.0, y: 0.0 };
    println!("({}, {})", origen.x, origen.y);
}
```

---
layout: center
---

## `impl`: Funciones Asociadas y Métodos

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left">
  <div>

```rust
struct Punto {
    x: f64,
    y: f64,
}

impl Punto {
    // funcion asociada: no recibe self,
    // se invoca como Punto::origen()
    fn origen() -> Self {
        Self { x: 0.0, y: 0.0 }
    }

    // metodo: recibe &self, se invoca
    // sobre una instancia ya creada
    fn distancia(&self, otro: &Punto) -> f64 {
        ((self.x - otro.x).powi(2)
            + (self.y - otro.y).powi(2)).sqrt()
    }
}
```

  </div>

<div class="text-sm space-y-4">

* `Self` (mayúscula) es un alias del tipo que implementa el bloque — evita repetir `Punto` dentro del `impl`.
* `&self` presta la instancia de forma inmutable; `&mut self` la presta de forma mutable si el método necesita modificar campos.
* Las funciones asociadas (sin `self`) suelen usarse como constructores, por convención llamadas `new`.

</div>

</div>

---
layout: center
---

## Un Método es Azúcar Sintáctico sobre un Préstamo

Cuando se llama a un método con `caja.metodo(...)`, Rust no hace nada mágico: por debajo, toma el préstamo que `self` pide y lo pasa como primer argumento a la función asociada.

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left">
  <div>

```rust
struct Caja {
    valor: i32,
}

impl Caja {
    fn ver(&self) -> &i32 {
        &self.valor
    }

    fn cambiar(&mut self, n: i32) {
        self.valor = n;
    }
}
```

  </div>

<div class="text-sm space-y-4">

```rust
let mut caja = Caja { valor: 5 };

caja.ver();
// == Caja::ver(&caja)

caja.cambiar(10);
// == Caja::cambiar(&mut caja, 10)
```

</div>

</div>

<div class="important-note">

`&self` y `&mut self` no son un mecanismo aparte del *borrowing* — son el mismo `&`/`&mut` de siempre, tomado automáticamente sobre la instancia. Por eso las reglas del borrow checker aplican igual a las llamadas de métodos.

</div>

---
layout: center
---

## Las Reglas de Borrowing También Aplican a Métodos

Como `caja.ver()` es `Caja::ver(&caja)` y `caja.cambiar(10)` es `Caja::cambiar(&mut caja, 10)`, la regla ya vista — *una mutable o varias inmutables, nunca ambas al mismo tiempo* — se cumple igual entre llamadas a métodos:

<div class="grid grid-cols-2 gap-y-6 gap-x-8 items-center mt-4 w-full text-left">

  <div class="[&_pre]:my-0">
    <span class="text-xs cp-ok font-bold block mb-1">Válido: dos préstamos de solo lectura</span>

```rust
fn main() {
    let caja = Caja { valor: 5 };
    let a = caja.ver();
    let b = caja.ver();
    println!("{a} y {b}");
}
```

  </div>

  <div class="[&_pre]:my-0">
    <span class="text-xs cp-err font-bold block mb-1">Error: préstamo vivo + método mutable</span>

```rust
fn main() {
    let mut caja = Caja { valor: 5 };
    let v = caja.ver();     // &self activo
    caja.cambiar(10);       // &mut self: conflicto
    println!("{v}");
}
```

  </div>

</div>

<br/>

> `caja.ver()` solo lee — se pueden llamar tantas veces como se quiera. Pero mientras su resultado siga en uso, `caja.cambiar(10)` pide un `&mut self` que no puede coexistir con ese préstamo de lectura.

---
layout: center
---

## Derive Traits

Escribir a mano comparaciones, formateo o clonado para cada struct sería repetitivo. El atributo `#[derive(...)]` le pide al compilador que genere esa implementación automáticamente.

<br>

```rust
#[derive(Debug, Clone, PartialEq, Eq)]
struct Punto {
    x: i32,
    y: i32,
}
```

<div class="important-note">

* **`Debug`**: habilita el formato `{:?}` para imprimir el struct completo (útil para depurar).
* **`Clone`**: habilita `.clone()` para duplicar el valor explícitamente, incluso si vive en el heap.
* **`PartialEq` / `Eq`**: habilitan comparar dos instancias con `==`, campo por campo.

</div>

---
layout: center
---

## Unit Structs vs. Structs con Campos

1. No todos los structs necesitan guardar datos. Un ***unit struct*** se declara sin campos ni llaves, solo como marcador de tipo:

```rust
struct Marcador;

fn main() {
    let m = Marcador;
}
```

2. Sirven para representar un concepto o agrupar funciones relacionadas bajo un `impl`, sin necesitar una instancia con datos — equivalen a un espacio de nombres con identidad de tipo propia.
3. Un struct con campos, en cambio, existe para *cargar información*: cada instancia es distinta porque sus valores lo son.

<div class="important-note">

Regla práctica: si el tipo solo necesita comportamiento (métodos) sin estado propio, un unit struct basta; si necesita representar datos distintos por instancia, corresponde declarar campos.

</div>
