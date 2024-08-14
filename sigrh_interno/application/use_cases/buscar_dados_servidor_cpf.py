"""Busca dados do servidor por cpf"""
from ..util.valida_cpf import valida_cpf
from ...domain.repositories.servidor_repository import ServidorRepository


class BuscarDadosServidorCpf:
    """Classe Busca dados do servidor por cpf"""
    def __init__(self, servidor_repository : ServidorRepository):
        self.servidor_repository = servidor_repository

    def run(self, cpf : str):
        """Valida as regras de négocio"""
        valida_cpf(cpf)

        #Se validado encaminha para o repositório
        return self.servidor_repository.get_servidor_by_cpf(cpf)

    def __call__(self, cpf : str):
        return self.run(cpf)
        