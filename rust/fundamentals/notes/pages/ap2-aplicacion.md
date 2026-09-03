---
layout: section
---

# Aplicación
El cheatsheet aplicado a los trials del repo

---
layout: center
---

## Aplicación · Move + `.clone()` — Reverse Linked List (206)

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left items-center">
  <div>

```rust
// reverse_list CONSUME la lista
pub fn reverse_list(head: Node) -> Node {
    /* ... */
}

// en el test, para no perder la entrada:
let head = Solution::reverse_list(input.clone());
let ans  = Solution::get_vec(head);
```

  </div>

<div class="cp-card text-sm space-y-2">

<div class="font-bold cp-brand">Corrida mental</div>

`Node = Option<Box<ListNode>>` vive en el **heap** → pasarlo a `reverse_list` lo **mueve**.

Sin `.clone()`, `input` quedaría inutilizable después de esa línea. La copia conserva el original para el resto del test.

<div class="opacity-70">Cheatsheet: <b>Heap → Movimiento</b> · ¿usable? No, salvo <code class="cp-code-inline">.clone()</code></div>

</div>

</div>

---
layout: center
---

## Aplicación · `&mut T` exclusiva — Remove Duplicates (26)

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left items-center">
  <div>

```rust
pub fn remove_duplicates(
    nums: &mut Vec<i32>,
) -> i32 {
    let mut set = HashSet::new();
    nums.retain(|&x| set.insert(x));
    nums.len() as i32
}

let mut arr = vec![1, 1, 2];
Solution::remove_duplicates(&mut arr);
// arr quedó modificado in-place
```

  </div>

<div class="cp-card text-sm space-y-2">

<div class="font-bold cp-brand">Corrida mental</div>

`&mut Vec<i32>` es un préstamo **exclusivo**: mientras dura, nadie más puede leer ni escribir `arr`.

Permite mutar in-place con `retain` sin mover el `Vec` ni devolver uno nuevo.

<div class="opacity-70">Cheatsheet: <b>&mut T → una sola</b>, y sin <code class="cp-code-inline">&</code> activas</div>

</div>

</div>

---
layout: center
---

## Aplicación · `&T` compartida — Longest Common Prefix (14)

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left items-center">
  <div>

```rust
for word in strs.iter() {   // word: &String
    if len > word.len() {
        len = word.len();
    }
}
// strs sigue disponible: se recorre
// otra vez más abajo
```

  </div>

<div class="cp-card text-sm space-y-2">

<div class="font-bold cp-brand">Corrida mental</div>

`.iter()` entrega `&String`: préstamos **compartidos**, de los que pueden existir muchos a la vez.

`strs` no se mueve: sigue usable tras el bucle, y de hecho se vuelve a iterar después.

<div class="opacity-70">Cheatsheet: <b>&T → muchas lecturas</b> simultáneas</div>

</div>

</div>

---
layout: center
---

## Aplicación · Copy de escalares — Container With Most Water (11)

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left items-center">
  <div>

```rust
let mut i = 0_usize;
let mut j = height.len() - 1;

while i < j {
    let a = min(height[i], height[j]); // i32
    if height[i] < height[j] { i += 1; }
    else { j -= 1; }
}
```

  </div>

<div class="cp-card text-sm space-y-2">

<div class="font-bold cp-brand">Corrida mental</div>

`i`, `j` (`usize`) y los `height[i]` (`i32`) viven en el **stack** → se **copian**.

Por eso `i += 1` y las comparaciones funcionan libremente, sin mover ni prestar nada.

<div class="opacity-70">Cheatsheet: <b>Stack → Copia</b> · ambos siguen vivos</div>

</div>

</div>

---
layout: center
---

## Aplicación · `&mut` "puntero láser" — Reverse Linked List (206)

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left items-center">
  <div>

```rust
let mut head: Node = None;
let mut iter: &mut Node = &mut head;

for &val in values.iter() {
    *iter = Some(Box::new(
        ListNode { val, next: None }
    ));
    iter = &mut iter.as_mut().unwrap().next;
}
head
```

  </div>

<div class="cp-card text-sm space-y-2">

<div class="font-bold cp-brand">Corrida mental</div>

`iter: &mut Node` es un préstamo **exclusivo** que se va reapuntando al `next` de cada nodo.

Solo puede existir ese único `&mut` sobre la cadena a la vez. El borrow checker lo garantiza en compilación.

<div class="opacity-70">Cheatsheet: <b>&mut T → una sola</b> · enlaza con Listas Enlazadas</div>

</div>

</div>

---
layout: center
---

## Aplicación · Efecto cebolla `Rc<RefCell<TreeNode>>` — Invert Binary Tree (226)

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left items-center">
  <div>

```rust
type Node = Option<Rc<RefCell<TreeNode>>>;

fn pre_order(n: &Node) {
    // n.left NO compila: n es un
    // Option, no un TreeNode
    if let Some(rc) = n {       // &Rc<..>
        let nodo = rc.borrow(); // Ref<TreeNode>
        // visitar(nodo.val);
        pre_order(&nodo.left);
        pre_order(&nodo.right);
    }
}
```

  </div>

<div class="cp-card text-sm space-y-2">

<div class="font-bold cp-brand">Corrida mental — 4 capas</div>

<div class="grid gap-x-3 gap-y-1" style="grid-template-columns:auto 1fr;font-size:0.72rem">
  <div class="font-mono opacity-80">Option</div><div>¿hay nodo? → <code>if let Some</code></div>
  <div class="font-mono opacity-80">Rc</div><div>propiedad compartida → deref</div>
  <div class="font-mono opacity-80">RefCell</div><div>mutabilidad interior → <code>.borrow()</code></div>
  <div class="font-mono opacity-80">TreeNode</div><div>datos → ya <code>.left</code> / <code>.right</code></div>
</div>

No se puede mover desde atrás de un `&`: por eso `if let Some(rc) = n` **presta** (match ergonomics), no consume.

<div class="opacity-70">Cheatsheet: <b>no sacar un valor de un préstamo</b> · <code>.borrow()</code> = lectura compartida</div>

</div>

</div>

---
layout: center
---

## Aplicación · HashMap + `get` → Option — Two Sum (1)

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left items-center">
  <div>

```rust
let mut visto: HashMap<i32, i32> = HashMap::new();

for (idx, val) in nums.iter().enumerate() {
    let falta = target - val;
    if let Some(&i) = visto.get(&falta) {
        return vec![i, idx as i32];
    }
    visto.insert(*val, idx as i32);
}
```

  </div>

<div class="cp-card text-sm space-y-2">

<div class="font-bold cp-brand">Corrida mental</div>

`visto.get(&falta)` devuelve `Option<&i32>`. El compilador obliga a manejar el caso "no está" con `if let Some`.

`Some(&i)` desestructura el `&` para copiar el `i32` (Copy), sin retener un préstamo del HashMap.

<div class="opacity-70">Cheatsheet: <b>get → Option</b> · abrir con <code>if let Some</code></div>

</div>

</div>

---
layout: center
---

## Aplicación · HashSet + `insert`/`contains` — Contains Duplicate (217)

<div class="grid grid-cols-2 gap-x-6 mt-4 w-full text-left items-center">
  <div>

```rust
let mut visto: HashSet<i32> = HashSet::new();

for n in nums.iter() {
    if visto.contains(&n) {
        return true;
    }
    visto.insert(*n);
}
false
```

  </div>

<div class="cp-card text-sm space-y-2">

<div class="font-bold cp-brand">Corrida mental</div>

`contains(&n)` **presta** el elemento (`&i32`) para consultar sin moverlo. El `Vec` original queda intacto.

`insert(*n)` copia el `i32` (Copy) al set; se podría acortar usando que `insert` devuelve `false` si ya existía.

<div class="opacity-70">Cheatsheet: <b>&T</b> para consultar · <code>i32</code> se copia al insertar</div>

</div>

</div>

<div class="cp-ver-tambien">

Ver también · Cheatsheet · 3.2 Ownership · 6.2 Rc, RefCell y árboles

</div>
