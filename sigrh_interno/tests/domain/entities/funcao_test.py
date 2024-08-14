import pytest
from ....domain.entities.funcao import Funcao

def test_desc_funcao_need_to_be_string():
    with pytest.raises(Exception):
        Funcao(6, 85)

def test_cod_func_need_to_be_integer():
    with pytest.raises(Exception):
        Funcao("6", "desc_funcao")

def test_desc_funcao_dont_accept_string_empty():
    with pytest.raises(Exception):
        Funcao(5, "")

def test_cod_func_dont_accept_null():
    with pytest.raises(Exception):
        Funcao(0, "desc_funcao")
