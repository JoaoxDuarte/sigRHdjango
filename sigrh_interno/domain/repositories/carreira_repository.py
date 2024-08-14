from abc import ABC, abstractmethod
from ..entities.carreira import Carreira


class CarreiraRepository(ABC):

    @abstractmethod
    def consultar_carreira_por_codigo(self, codigo: int):
        pass

    @abstractmethod
    def registrar_carreira(self, carreira: Carreira):
        pass
