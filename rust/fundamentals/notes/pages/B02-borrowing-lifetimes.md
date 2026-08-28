---
layout: section
---

# Borrowing y Lifetimes

---
layout: center
---

1. Para flexibilizar el sistema de *ownership*, Rust implementa un mecanismo complementario llamado ***borrow checker***. Este sistema establece reglas sobre cómo tu programa puede acceder a los datos, especialmente cuando múltiples partes necesitan leer o modificar la misma información.

2. Esto previene errores complejos (*bugs*) cuando diferentes secciones del programa intentan manipular los mismos datos de forma simultánea.

---
layout: center
---

## Referencias

En Rust, una **referencia** (`&`) es un puntero que permite acceder a un dato sin tomar su propiedad (*ownership*). 

* **Préstamo:** El dueño original conserva el control del dato; solo le da un permiso temporal a otra variable.
* **Sintaxis:** Se utiliza el operador `&` para crear una referencia de lectura, y `&mut` para una referencia que permita modificar el dato.

---
layout: center
---

## Reglas del **borrow checker**

Para asegurar que estos préstamos temporales no corrompan la memoria ni causen problemas al compilar, el *borrow checker* vigila estrictamente dos condiciones:

<div class="important-note">

1. Para un instante de tiempo dado, está permitida una y sólo una referencia mutable ó cualquier cantidad de referencias inmutables.
2. Toda referencia debe ser siempre válida.

</div>

---
layout: center
---

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left">
  <div>
    <span class="text-xs cp-ok font-bold block mb-1">Válido: Muchas lecturas</span>

```rust
fn main() {
    let x = String::from("hola");
    let r1 = &x;
    let r2 = &x;
    println!("{r1} y {r2}");
}
```

  </div>

  <div>
    <span class="text-xs cp-err font-bold block mb-1">Error: Mezcla de lectura y escritura</span>

```rust
fn main() {
    let mut x = String::from("hola");
    let r1 = &x;
    let r2 = &mut x;
    println!("{r1}");
}
```

  </div>
</div>
<br/>

> Puedes tener infinitas lecturas, pero si creas una referencia mutable (`&mut`), no puede existir nadie más accediendo a ese dato al mismo tiempo.

---
layout: center
---

## Tipos de **lifetimes**

<br/>

## Lifetimes concretos $L$

* Son tiempos de vida reales y físicos de las variables en memoria.
* Están determinados por el lugar donde se crean las variables y los brakets que marcan su destrucción.
* Son estáticos y ocurren al ejecutar el bloque de código.


## Lifetimes genéricos $'a$

* Son variables abstractas que funcionan como parámetros de tiempo.
* No representan un tiempo fijo, sino una relación o un "cupo".

---
layout: center
---

1. El *borrow checker* evalúa constantemente que los **lifetimes concretos** ($L$) de las referencias se ajusten de forma segura a los límites marcados por los **lifetimes genéricos** ($'a$).
2. En términos simples: vigila estrictamente que ninguna referencia viva más tiempo que el dueño original de los datos, evitando así punteros colgados (*dangling pointers*).

---
layout: center
---

## ¿Por qué se necesitan los lifetimes genéricos?

1. **Relación de supervivencia:** Son necesarios para indicarle al compilador qué vínculo tienen las referencias entre sí cuando no puede deducirlo por su cuenta.
2. **Garantía de seguridad:** Se aplican para asegurar que un dato retornado (o guardado en una `struct`) nunca viva más tiempo que la referencia original que le dio origen.


---
layout: center
---

## Ecuación general de los lifetimes

<div class="important-note">

  Sean $L$ y $'a$ lifetimes, $s$ y $t$ referencias de entrada y $r$ la referencia de salida en una función. El borrow checker evalua que:

  $$ max(L(r)) ≤ \ 'a \ | \ 'a = min(L(s), L(t)) $$

  para determinar que toda referencia debe ser siempre válida durante el flujo del programa.

</div>

---
layout: center
---

````md magic-move

```rust
fn foo(a: &str, b: &str) -> &str {
    if a.len() >= b.len() {a} else {b}
}

fn main() {
    let s = String::from("Hello world in english!");
    let t = String::from("Hola mundo en español!");
    let r = foo(&s, &t);
    println!("{}", r);
}
```

```rust
fn foo<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() >= b.len() {a} else {b}
}

fn main() {
    let s = String::from("Hello world in english!");
    let t = String::from("Hola mundo en español!");
    let r = foo(&s, &t);
    println!("{}", r);
}
```
````

<br/>

````md magic-move

```
error[E0106]: missing lifetime specifier
 --> src/main.rs:1:29
  |
1 | fn foo(a: &str, b: &str) -> &str {
  |           ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but the signature does not say whether it is borrowed from `a` or `b`
help: consider introducing a named lifetime parameter

```

```
Hello world in english!
```
````

---
layout: center
---

````md magic-move

```rust
struct User {
    age: i32,
    name: & str
}

fn main() {
    let n = "Giovanny";
    let usr = User {
        age: 32,
        name: n
    };
    println!("Mi nombre es {} y tiengo {} años", usr.name, usr.age);
}
```

```rust
struct User<'a> {
    age: i32,
    name: &'a str
}

fn main() {
    let n = "Giovanny";
    let usr = User {
        age: 32,
        name: n
    };
    println!("Mi nombre es {} y tiengo {} años", usr.name, usr.age);
}
```
````

<br/>

````md magic-move

```
error[E0106]: missing lifetime specifier
 --> src/main.rs:3:11
  |
3 |     name: & str
  |           ^ expected named lifetime parameter
  |
help: consider introducing a named lifetime parameter

```

```
Mi nombre es Giovanny y tiengo 32 años
```
````

---
layout: center
---

## Evaluación de las referencias

<div class="grid grid-cols-2 gap-y-6 gap-x-8 items-center mt-4">

  <div class="[&_pre]:my-0">

  ```rust
  fn foo<'a>(a: &'a str, b: &'a str) -> &'a str {
      if a.len() >= b.len() {a} else {b}
  }
  
  fn main() {
      let s = String::from("Hello world in english!");
      let t = String::from("Hola mundo en español!");
      let r = foo(&s, &t);
      println!("{}", r);
  }
  ```

  </div>

<div class="text-center text-sm space-y-4">

  $$ 'a = \min(L(s), L(t)) $$
  
  Sustituyendo los tiempos de vida reales:
  $$ L(s) = L(t) = L(r) $$
  $$ 'a = L(s) $$

  Condición del *borrow checker*:
  $$ \max(L(r)) \le \ 'a $$
  $$ L(r) \le L(s) \quad \Rightarrow \quad \color{green}{\text{Válido}} $$

  </div>

</div>

---
layout: center
---


<div class="grid grid-cols-2 gap-y-6 gap-x-8 items-center mt-4">

  <div class="[&_pre]:my-0">

  ```rust
  fn foo<'a>(a: &'a str, b: &'a str) -> &'a str {
      if a.len() >= b.len() {a} else {b}
  }
  
  fn main() {
      let r: &str;
      let s = String::from("Hello world in english!");
      {
          let t = String::from("Hola mundo en español!");
          r = foo(&s, &t);
      }
      println!("{}", r);
  }
  ```

  </div>

  <div class="text-center text-sm space-y-4">

  $$ 'a = \min(L(s), L(t)) $$

  Como $t$ vive en un bloque interno más pequeño:
  $$ L(t) < L(s) \quad \Rightarrow \quad 'a = L(t) $$

  Condición del *borrow checker*:
  $$ \max(L(r)) \le \ 'a $$
  $$ L(r) \le L(t) \quad \Rightarrow \quad \color{red}{\text{FALSO}} $$

  </div>

</div>

---
layout: center
---

## Seguridad de Memoria en Rust

Al trabajar en conjunto, el sistema de **Ownership**, el **Borrow Checker** y las reglas de **Lifetimes** eliminan los errores de gestión de memoria más comunes de la industria:

* **Punteros nulos:** Rust garantiza que toda referencia apunte siempre a un lugar válido en memoria.
* **Desbordamientos de búfer:** Valida estrictamente que las lecturas y escrituras ocurran dentro de los límites de los arreglos.
* **Punteros colgados / Doble liberación:** Erradicados por completo gracias al control estricto de ámbitos de vida.

---
layout: center
---

* **Carreras de datos (Data races):** Impide el acceso simultáneo y desordenado a un mismo dato en entornos multihilo.
* **Comportamientos indefinidos:** El compilador rechaza cualquier zona gris de la memoria (*undefined behavior*).
* **Cero Garbage Collector:** No se necesita pausar el programa en ejecución; todo se resuelve al compilar.

**Conclusión:** Rust traslada la seguridad de la memoria al **tiempo de compilación**. Si tu código compila, es matemáticamente seguro en memoria.

