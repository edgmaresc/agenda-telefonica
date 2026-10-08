"""Pruebas de la agenda telefónica v1 (pytest, sin clases)."""
from src.agenda import (
    anyadir_contacto,
    buscar_por_nombre,
    buscar_por_numero,
    eliminar_contacto,
    listar_ordenados,
    cargar_contactos,
    guardar_contactos,
    validar_nombre,
    validar_telefono,
)


def test_validar_nombre():
    assert validar_nombre("Ana") is True
    assert validar_nombre("   ") is False
    assert validar_nombre("") is False


def test_validar_telefono():
    assert validar_telefono("612345678") is True
    assert validar_telefono("123") is False
    assert validar_telefono("61234abcd") is False
    assert validar_telefono(" 612345678 ") is True


def test_anyadir_ok():
    agenda = []
    ok, _ = anyadir_contacto(agenda, "Ana", "612345678")
    assert ok is True
    assert agenda == [{"nombre": "Ana", "telefono": "612345678"}]


def test_anyadir_duplicado():
    agenda = []
    anyadir_contacto(agenda, "Ana", "612345678")
    ok, _ = anyadir_contacto(agenda, "ana", "600111222")
    assert ok is False
    assert len(agenda) == 1


def test_anyadir_datos_malos():
    agenda = []
    ok1, _ = anyadir_contacto(agenda, "  ", "612345678")
    ok2, _ = anyadir_contacto(agenda, "Pepe", "123")
    assert ok1 is False
    assert ok2 is False
    assert agenda == []


def test_buscar_por_nombre():
    agenda = []
    anyadir_contacto(agenda, "Ana", "612345678")
    anyadir_contacto(agenda, "Anabel", "600111222")
    anyadir_contacto(agenda, "Pepe", "600333444")
    assert len(buscar_por_nombre(agenda, "ana")) == 2
    assert len(buscar_por_nombre(agenda, "ANA")) == 2
    assert buscar_por_nombre(agenda, "zorro") == []


def test_buscar_por_numero():
    agenda = []
    anyadir_contacto(agenda, "Ana", "612345678")
    assert len(buscar_por_numero(agenda, "612345678")) == 1
    assert buscar_por_numero(agenda, "612345") == []
    assert buscar_por_numero(agenda, "000000000") == []


def test_eliminar():
    agenda = []
    anyadir_contacto(agenda, "Ana", "612345678")
    assert eliminar_contacto(agenda, "ANA") is True
    assert agenda == []
    assert eliminar_contacto(agenda, "Ana") is False


def test_ordenados():
    agenda = []
    anyadir_contacto(agenda, "pepe", "600333444")
    anyadir_contacto(agenda, "Ana", "612345678")
    nombres = [c["nombre"] for c in listar_ordenados(agenda)]
    assert nombres == ["Ana", "pepe"]


def test_guardar_y_cargar(tmp_path):
    ruta = tmp_path / "contactos.txt"
    agenda = []
    anyadir_contacto(agenda, "Ana", "612345678")
    guardar_contactos(str(ruta), agenda)
    cargada, ignoradas = cargar_contactos(str(ruta))
    assert ignoradas == 0
    assert cargada == agenda


def test_cargar_sin_fichero(tmp_path):
    ruta = tmp_path / "noexiste.txt"
    cargada, ignoradas = cargar_contactos(str(ruta))
    assert cargada == []
    assert ignoradas == 0


def test_cargar_ignora_corruptas(tmp_path):
    ruta = tmp_path / "contactos.txt"
    ruta.write_text("Ana;612345678\nMAL SIN SEPARADOR\nPepe;123\n", encoding="utf-8")
    cargada, ignoradas = cargar_contactos(str(ruta))
    assert len(cargada) == 1
    assert cargada[0]["nombre"] == "Ana"
    assert ignoradas == 2
