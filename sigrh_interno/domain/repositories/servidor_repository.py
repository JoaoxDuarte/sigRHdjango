from abc import ABC, abstractmethod


class ServidorRepository(ABC):

    @abstractmethod
    def get_servidor_by_cpf(self, cpf: str):
        pass

    @abstractmethod
    def get_servidor_by_matricula(self, matricula: str):
        pass

    @abstractmethod
    def get_servidor_by_orgao(self, orgao:str):
        pass
