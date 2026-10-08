# Agenda Telefónica

## Objetivo
Aplicación de consola en Python para gestionar contactos (nombre + teléfono).
Proyecto educativo de 2.º de Bachillerato: programación estructurada, sin clases.

## Requisitos
- Python 3.10 o superior.
- `pytest` para pruebas (ver `requirements.txt`).
- Codificación UTF-8 en código y datos.

## Funcionalidades de la versión 1
1. Añadir contacto: `nombre` no vacío (se guarda sin espacios extra), `telefono` solo dígitos, 9 caracteres. No se admiten nombres duplicados (comparación insensible a mayúsculas).
2. Buscar por nombre: búsqueda parcial, insensible a mayúsculas/minúsculas. Si no hay coincidencia, muestra "No encontrado".
3. Buscar por número: búsqueda exacta de dígitos. Si no hay coincidencia, muestra "No encontrado".
4. Eliminar por nombre exacto (insensible a mayúsculas). Si no existe, avisa sin borrar.
5. Mostrar todos ordenados alfabéticamente por nombre (insensible a mayúsculas). Si agenda vacía, muestra "Agenda vacía".
6. Persistencia automática en `data/contactos.txt`: se carga al iniciar (si no existe, empieza vacía) y se guarda tras añadir/eliminar. Líneas corruptas se ignoran y se avisa.

## Formato de datos (`data/contactos.txt`)
- Fichero de texto, UTF-8, una línea por contacto: `nombre;telefono`
- Ejemplo: `Ana;612345678`
- Este fichero está ignorado en Git (ver `.gitignore`). Para pruebas se usan datos de ejemplo.

## Estructura
- `src/agenda.py`: programa y menú (punto de entrada).
- `src/__init__.py`: marca paquete.
- `tests/test_agenda.py`: pruebas con `pytest` (funciones + `assert`, sin `unittest.TestCase`).
- `data/`: datos de ejecución (no se sube `contactos.txt` real).
- `docs/`: documentación adicional si hace falta.

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecución
```bash
python -m src.agenda
```

## Pruebas
```bash
pytest -v
```

## Restricciones didácticas (v1)
- Programación estructurada, funciones pequeñas y nombres descriptivos.
- Sin clases, sin bases de datos, sin decoradores.
- Constantes en mayúsculas cuando proceda (ej. `RUTA_DATOS`).
- Código y comentarios en español, comprensible para Bachillerato.
