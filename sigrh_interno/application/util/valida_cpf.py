import re


def valida_cpf(cpf: str):
    if not re.match(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf) and not (
            re.match(r'[0-9]{9}-?[0-9]{2}', cpf)):
        raise Exception("Formato inválido")

    documento = cpf.replace('.', '').replace('-', '')
    str_cpf = documento
    num_dv1 = 0
    num_dv2 = 0
    num_checkout_dv1 = 0
    num_checkout_dv2 = 0
    i = 1

    num_checkout_dv1 = int(str_cpf[9:10])
    num_checkout_dv2 = int(str_cpf[10:11])

    if len(str_cpf) == 11:
        for i in range(1, 10):
            num_dv1 = num_dv1 + int(str_cpf[i-1:i]) * i
            num_dv1 = num_dv1 % 11

        for i in range(2, 11):
            num_dv2 = num_dv2 + int(str_cpf[i-1:i]) * (i - 1)
            num_dv2 = num_dv2 % 11
    else:
        raise Exception("CPF inválido")

    if num_dv1 == 10:
        num_dv1 = 0
    if num_dv2 == 10:
        num_dv2 = 0

    if num_dv1 != num_checkout_dv1 or num_dv2 != num_checkout_dv2:
        raise Exception('Dígito inválido')
