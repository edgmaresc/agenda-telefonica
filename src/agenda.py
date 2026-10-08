"""Agenda telefónica v1.

Proyecto educativo de 2.º de Bachillerato.
Programación estructurada: solo funciones, sin clases.

Cada contacto es un diccionario: {"nombre": str, "telefono": str}.
La agenda es una lista de contactos.
"""

RUTA_DATOS = "data/contactos.txt"
SEPARADOR = ";"
LONGITUD_TELEFONO = 9


def validar_nombre(nombre):
    """Comprueba que el nombre no esté vacío tras quitar espacios."""
    return nombre.strip() != ""


def validar_telefono(telefono):
    """Comprueba que el teléfono tenga 9 dígitos.

    Se usa texto (str) y no número (int) para no perder
    un posible 0 inicial y para validar dígito a dígito.
    """
    texto = telefono.strip()
    return len(texto) == LONGITUD_TELEFONO and texto.isdigit()


def buscar_indice_por_nombre(contactos, nombre):
    """Devuelve la posición del contacto o -1 si no existe.

    La comparación ignora mayúsculas/minúsculas.
    """
    buscado = nombre.strip().lower()
    for i, contacto in enumerate(contactos):
        if contacto["nombre"].lower() == buscado:
            return i
    return -1


def anyadir_contacto(contactos, nombre, telefono):
    """Añade un contacto si los datos son válidos.

    Devuelve (ok, mensaje). No admite duplicados de nombre.
    """
    nombre_limpio = nombre.strip()
    telefono_limpio = telefono.strip()
    if not validar_nombre(nombre_limpio):
        return False, "El nombre no puede estar vacío."
    if not validar_telefono(telefono_limpio):
        return False, "El teléfono debe tener 9 dígitos."
    if buscar_indice_por_nombre(contactos, nombre_limpio) != -1:
        return False, "Ese nombre ya existe."
    contactos.append({"nombre": nombre_limpio, "telefono": telefono_limpio})
    return True, "Contacto añadido."


def buscar_por_nombre(contactos, texto):
    """Busca por nombre parcial, sin distinguir mayúsculas."""
    buscado = texto.strip().lower()
    return [c for c in contactos if buscado in c["nombre"].lower()]


def buscar_por_numero(contactos, numero):
    """Busca contactos con ese número exacto."""
    buscado = numero.strip()
    return [c for c in contactos if c["telefono"] == buscado]


def eliminar_contacto(contactos, nombre):
    """Elimina por nombre exacto (sin mayúsculas). True si se borró."""
    indice = buscar_indice_por_nombre(contactos, nombre)
    if indice == -1:
        return False
    del contactos[indice]
    return True


def listar_ordenados(contactos):
    """Devuelve una lista nueva ordenada por nombre."""
    return sorted(contactos, key=lambda c: c["nombre"].lower())


def cargar_contactos(ruta):
    """Carga contactos desde un fichero nombre;telefono (UTF-8).

    Si no existe, devuelve ([], 0). Ignora líneas corruptas.
    """
    contactos = []
    ignoradas = 0
    try:
        with open(ruta, mode="r", encoding="utf-8") as fichero:
            lineas = fichero.readlines()
    except FileNotFoundError:
        return [], 0
    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(SEPARADOR)
        if len(partes) != 2:
            ignoradas += 1
            continue
        ok, _mensaje = anyadir_contacto(contactos, partes[0], partes[1])
        if not ok:
            ignoradas += 1
    return contactos, ignoradas


def guardar_contactos(ruta, contactos):
    """Guarda los contactos en un fichero UTF-8."""
    with open(ruta, mode="w", encoding="utf-8") as fichero:
        for contacto in contactos:
            linea = contacto["nombre"] + SEPARADOR + contacto["telefono"] + "\n"
            fichero.write(linea)


def mostrar_contactos(contactos):
    """Muestra contactos ordenados o avisa si no hay ninguno."""
    if not contactos:
        print("Agenda vacía.")
        return
    for contacto in listar_ordenados(contactos):
        print(contacto["nombre"] + " - " + contacto["telefono"])


def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n--- Agenda telefónica ---")
    print("1. Añadir contacto")
    print("2. Buscar por nombre")
    print("3. Buscar por número")
    print("4. Eliminar contacto")
    print("5. Mostrar todos")
    print("0. Salir")


def main():
    """Bucle principal del programa."""
    contactos, ignoradas = cargar_contactos(RUTA_DATOS)
    if ignoradas > 0:
        print("Aviso: se ignoraron", ignoradas, "líneas con formato incorrecto.")
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono (9 dígitos): ")
            ok, mensaje = anyadir_contacto(contactos, nombre, telefono)
            print(mensaje)
            if ok:
                guardar_contactos(RUTA_DATOS, contactos)
        elif opcion == "2":
            texto = input("Texto a buscar: ")
            encontrados = buscar_por_nombre(contactos, texto)
            if not encontrados:
                print("No encontrado.")
            else:
                mostrar_contactos(encontrados)
        elif opcion == "3":
            numero = input("Número exacto: ")
            encontrados = buscar_por_numero(contactos, numero)
            if not encontrados:
                print("No encontrado.")
            else:
                mostrar_contactos(encontrados)
        elif opcion == "4":
            nombre = input("Nombre a eliminar: ")
            if eliminar_contacto(contactos, nombre):
                print("Contacto eliminado.")
                guardar_contactos(RUTA_DATOS, contactos)
            else:
                print("No existe ningún contacto con ese nombre.")
        elif opcion == "5":
            mostrar_contactos(contactos)
        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida. Elige entre 0 y 5.")


if __name__ == "__main__":
    main()

