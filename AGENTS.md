## Contexto
Proyecto educativo 2.º Bachillerato. Python estructurado. Lenguaje claro en español.

## Lectura obligatoria antes de actuar
Orden: `README.md` → `TODO.md` → `SESSION_LOG.md` → `CHANGE_LOG.md` → este `AGENTS.md`.

## Reglas obligatorias
1. No programes si se pide plan. No cambies requisitos por iniciativa propia.
2. Funciones sencillas, nombres descriptivos, constantes en MAYÚSCULAS. UTF-8 siempre.
3. Prohibido en v1 sin autorización: clases, BD, decoradores, dependencias nuevas.
4. Si necesitas dependencia, justifica por qué y actualiza `requirements.txt` + README.
5. No borres archivos ni reescribas todo por un problema pequeño sin aprobación.
6. Explica cambios con nivel Bachillerato.
7. Pruebas: usa `pytest` con funciones `test_*` y `assert`. No uses `unittest.TestCase` (es POO y choca con "sin clases").
8. Para cada comportamiento nuevo/ragtouched: añade o actualiza prueba en `tests/test_agenda.py`.
9. No subir datos reales: `data/contactos.txt` está ignorado. Usa fixtures/temporales en tests.
10. Al terminar: lista archivos modificados, comando `pytest -v` ejecutado y resultado.

## Flujo
ANALIZAR → PLANIFICAR → ESPERAR APROBACIÓN → IMPLEMENTAR → PROBAR (`pytest -v`) → DOCUMENTAR (`README` si cambia uso, `CHANGE_LOG`, `SESSION_LOG`, `TODO` checkboxes).

## Criterio de finalización
Una tarea T solo está terminada si: código entendido por alumno, `pytest -v` en verde, y `TODO` + `SESSION_LOG` + `CHANGE_LOG` reflejan estado real.
