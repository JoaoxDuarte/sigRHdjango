import pytest
from ....domain.entities.evento import Evento

def test_cod_evento_dont_accept_negative_value():
    with pytest.raises(Exception):
        Evento(-8, "descEvento")

def test_desc_evento_need_to_be_string():
    with pytest.raises(Exception):
        Evento(8, 5)

def test_desc_evento_dont_accept_empty():
    with pytest.raises(Exception):
        Evento(8, "")
