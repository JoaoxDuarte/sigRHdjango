import pytest
from ....application.util.valida_cpf import valida_cpf


def test_valida_cpf_need_len_11():
    with pytest.raises(Exception):
        valida_cpf("386.287.180-010")


def test_valida_cpf_need_to_be_string():
    with pytest.raises(Exception):
        valida_cpf(95284835000)


def test_valida_cpf_dont_accept_text_string():
    with pytest.raises(Exception):
        valida_cpf("386.28c.18a-01")


def test_valida_cpf_numdvn_need_to_be_equal_num_checkout_dvn():
    with pytest.raises(Exception):
        valida_cpf("08873149031")


def test_cpf_valida_can_create_cpf_with_score_line():
    valida_cpf("256.642.940-51")


def test_valida_cpf_dont_accept_random_position_score_line():
    with pytest.raises(Exception):
        valida_cpf("256-64.2.940-51")


def test_cpfs():
    valida_cpf("164.870.932-03")
    valida_cpf("904.863.217-03")
