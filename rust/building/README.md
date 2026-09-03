# Building

Pista de **desarrollo aplicado** en Rust: construir cosas que alguien usaría, en
contraste con `../fundamentals/`, que se enfoca en dominar el lenguaje a través
de algoritmos.

Las notas de conceptos (Módulos, Crates y Cargo, y lo que se agregue después)
ya no viven aquí como deck aparte: se fusionaron a `rust/fundamentals/notes`
(páginas con prefijo `F`), para tener un solo deck de estudio. Este directorio
queda para los proyectos Cargo en sí.

## Estructura

```
building/
└── projects/    # un proyecto Cargo independiente por cada cosa construida,
                 # con su propio Cargo.toml y su README con los detalles
                 # específicos de las crates que usa  ← por crear
```

## Por qué separado de `fundamentals/`

- **Dependencias aisladas.** Los trials son binarios sueltos sin dependencias
  pesadas; meter `tokio`/`axum`/`polars` en ese paquete inflaría la compilación
  de los 34 trials.
- **Las notas de concepto viven junto al lenguaje.** Por eso están en
  `fundamentals/notes`; lo que sí cambia seguido (versiones, firmas concretas,
  recetas de cada crate) vive en el README de su proyecto, junto al
  `Cargo.toml` que fija su versión.
