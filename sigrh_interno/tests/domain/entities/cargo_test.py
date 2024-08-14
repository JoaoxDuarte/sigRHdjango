# from sig

import pytest

from sigrh_interno.domain.entities.carreira import Carreira
from ....domain.entities.cargo import Cargo


def test_cargo_dont_accept_negative_code():
    with pytest.raises(Exception):
        Cargo(-5, "descCargo", Carreira(1, 'l'))


def test_can_create_cargo_with_code_1():
    # arranje act
    cargo_objeto = Cargo(1, "descCargo", Carreira(1, 'l'))
    # assert
    assert cargo_objeto is not None
