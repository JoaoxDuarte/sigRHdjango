import pytest
from ....domain.entities.vinculo import Vinculo


def test_cod_vinculo_dont_accept_str_value():
    with pytest.raises(Exception):
        Vinculo("cod_vinculo", "tipo_vinculo")


def test_tipo_vinculo_dont_accept_int_value():
    with pytest.raises(Exception):
        Vinculo(6, 1)


def test_vinculo_dont_accept_negative_value():
    with pytest.raises(Exception):
        Vinculo(-15, "tipo_vinculo")


def test_cod_vinculo_dont_accept_zero():
    with pytest.raises(Exception):
        Vinculo(0, "tipo_vinculo")


def test_cod_vinculo_dont_accept_null():
    with pytest.raises(Exception):
        Vinculo(None, "tipoVinculo")


def test_tipo_vinculo_dont_accept_null():
    with pytest.raises(Exception):
        Vinculo(6, "")
