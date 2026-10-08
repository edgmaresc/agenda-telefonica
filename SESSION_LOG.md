# Diario de sesiones

## Sesión 1 - 2026-10-02
### Objetivo
Preparar la estructura y la memoria del proyecto.

### Realizado
- Creadas carpetas `src/`, `tests/`, `data/`, `docs/` y plantillas `__init__.py`, `.gitignore`, `requeriments.txt` (con typo por renombrar).
- Redactados borradores `README`, `TODO`, `AGENTS`.

### Comprobaciones
- `git status`: rama `main` sin commits, todo `untracked`.
- `src/agenda.py` y `tests/test_agenda.py` no existen todavía.
- `README ## Ejecución` con bloque mal cerrado.

### Pendiente
- T0 acordar plan v1, T1 commit inicial.

### Primer paso de la próxima sesión
- Validar redacción propuesta de los 5 docs y hacer commit inicial T1.

## Sesión 2 - 2026-10-07
### Objetivo
Aprobar docs v1 y codificar T2-T8 con pruebas T9.

### Realizado
- Reredactados `README`, `TODO`, `AGENTS`, `CHANGE_LOG`, `SESSION_LOG` (validaciones, formato `nombre;telefono`, pytest).
- Creado `src/agenda.py`: validación 9 dígitos, no duplicados, búsqueda parcial/exacta, eliminar, ordenar, persistencia `;` UTF-8, menú 1-5 + 0.
- Creado `tests/test_agenda.py`: 12 pruebas (validar, añadir, duplicado, datos malos, búsquedas, eliminar, orden, guardar/cargar, sin fichero, corruptas).
- Actualizado `TODO`: T0, T2-T8 y T9-escritura a Terminadas.

### Comprobaciones
- Revisión visual de `src/agenda.py` y `tests/test_agenda.py`: coherentes con README.
- `py_compile` y `pytest -v` NO verificables: la terminal no devuelve salida en este entorno.
- `git status/commit` NO ejecutable por la misma razón. `requeriments.txt` sigue pendiente de renombrar.

### Pendiente
- En tu terminal: `python3 -m py_compile src/agenda.py tests/test_agenda.py`, instalar pytest (`sudo apt install python3-pytest` o `pip install pytest`), `pytest -v`, `python -m src.agenda` manual.
- `git mv requeriments.txt requirements.txt`, `git add .`, `git commit -m "feat: agenda v1 + docs v1"`.
- T10: cerrar CHANGE_LOG v0.1.0 tras el verde de pytest.
