<h1 align="left">
  <img src="https://github.com/PonchoCeniceros/academia-jedi/blob/main/.assets/jedi.png" width="90" align="absmiddle">
  &nbsp;
  Academia Jedi
</h1>

> *"La fuerza de un Jedi fluye de la Fuerza. Pero cuidado. La ira, el miedo, la agresión — el lado oscuro son."*
> — Maestro Yoda

Este es mi campo de entrenamiento personal en los caminos de la Fuerza. Aquí, cada problema es una **Prueba** — un test de disciplina, claridad y dominio del código. Un Padawan no atraviesa las Pruebas con prisa. Medita, refina y regresa hasta que la solución fluye tan naturalmente como la Fuerza misma.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Rust](https://img.shields.io/badge/rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)

---

## 🏛️ Estructura del Templo

El Templo se organiza por **lenguaje**. Cada Prueba se identifica por su ID de LeetCode. Dentro del camino Rust hay dos senderos: *fundamentals* (dominar el lenguaje) y *building* (construir cosas útiles con él). Los Pergaminos de estudio de ambos viven juntos en un solo deck, dentro de `fundamentals/notes`.

```text
.
├── rust/
│   ├── fundamentals/        # El camino del dominio del lenguaje
│   │   ├── notes/           # Los Pergaminos (presentación de estudio; fundamentos + aplicado)
│   │   └── trials/          # La Cámara Rust (cargo test)
│   │       ├── Cargo.toml   # Un solo proyecto para gobernarlos a todos
│   │       ├── holocron.sh  # El Holocrón — camino Rust
│   │       └── src/bin/     # Un pergamino por Prueba
│   │           ├── 1_two_sum.rs
│   │           └── ...
│   └── building/            # El camino de la construcción (APIs, datos) — proyectos Cargo, por crear
├── python/
│   ├── trials/              # La Cámara Python (Pytest)
│   │   ├── 1.py             # Two Sum
│   │   ├── 20.py            # Valid Parentheses
│   │   └── ...
│   ├── utils/               # Conocimiento compartido (logging)
│   └── holocron.sh          # El Holocrón — camino Python
├── docs/
│   ├── algorithms/          # Patrones de razonamiento (sin lenguaje)
│   └── whiteboards/         # Meditaciones visuales
├── roadmap.csv              # El Registro de Pruebas
└── README.md                # El Códex Jedi
```

### Los dos Pergaminos

| Deck | Tema | Puerto |
| --- | --- | --- |
| `rust/fundamentals/notes` | **Rust Fundamentos + Aplicado** — el lenguaje y cómo construir con él | 3031 |
| `docs/algorithms` | **Algoritmos** — patrones, independiente del lenguaje | 3033 |

```bash
pnpm --dir rust/fundamentals/notes run dev
pnpm --dir docs/algorithms run dev
```

---

## 🌌 Las Pruebas

Una Prueba solo se considera **dominada** cuando todos los tests pasan — y la solución es tan clara y simple como el lado luminoso exige.

### Camino Python
```python
@pytest.mark.parametrize("input, expected", [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
])
def test_solution(input, expected):
    assert Solution().longestCommonPrefix(input) == expected
```

### Camino Rust
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_sum() {
        assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
    }
}
```

---

## ⚔️ Los Holocrones (Automatización)

Los scripts **Holocrón** guían a los Padawans a través de sus Pruebas — generando los pergaminos, iniciando los tests y llevando registro de las misiones completadas. Un verdadero Jedi no desperdicia energía en configuración. Se concentra en la Fuerza.

Ambos Holocrones resuelven su propia ubicación: funcionan desde la raíz del Templo o desde su propia cámara.

### Camino Python (`python/holocron.sh`)
```bash
# Comenzar una nueva Prueba
python/holocron.sh -m "9. Palindrome Number"

# Iniciar el entrenamiento
python/holocron.sh -t 9

# Consultar el Registro de Pruebas
python/holocron.sh -l
```

### Camino Rust (`rust/fundamentals/trials/holocron.sh`)
```bash
# Comenzar una nueva Prueba
rust/fundamentals/trials/holocron.sh -m "1. Two Sum"

# Iniciar el entrenamiento
rust/fundamentals/trials/holocron.sh -t 1

# Ejecutar la Prueba
rust/fundamentals/trials/holocron.sh -r 1

# Consultar el Registro de Pruebas
rust/fundamentals/trials/holocron.sh -l
```

Ambos Holocrones conjuran pergaminos con:
- ⚔️ **Estructura de tests** lista para ser empuñada.
- 📡 **Logging estandarizado** con `utils.log` (Python).
- 🦀 **Binario Cargo** forjado por Prueba (Rust).

---

## 🔮 El Código Jedi

> *No hay emoción, hay paz.*
> *No hay ignorancia, hay conocimiento.*
> *No hay pasión, hay serenidad.*

1. **Claridad sobre Velocidad** — El código debe ser legible antes de ser ingenioso. El lado oscuro promete atajos; el Jedi construye cimientos.
2. **Refinamiento Continuo** — Una Prueba no termina cuando el test pasa. Termina cuando ya no se puede eliminar nada más.
3. **Abraza el Proceso** — Cada test fallido es una lección. Cada test aprobado es un paso más hacia la maestría.

*Que la Fuerza te acompañe.* 🌌
