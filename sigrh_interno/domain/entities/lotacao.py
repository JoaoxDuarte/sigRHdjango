from datetime import datetime
from .carreira import Carreira
from .empresa import Empresa


class Lotacao:
    def __init__(self,
        cod_lotacao: int,
        desc_lotacao: str,
        data_inicio: datetime,
        empresa: Empresa):
        self.cod_lotacao = cod_lotacao
        self.desc_lotacao = desc_lotacao
        self.data_inicio = data_inicio
        self.empresa = empresa

    @property
    def cod_lotacao(self):
        return self._cod_lotacao

    @cod_lotacao.setter
    def cod_lotacao(self, cod_lotacao: int):
        if cod_lotacao < 1:
            raise ValueError("Código de lotação não encontrado!")
        self._cod_lotacao = cod_lotacao

    @property
    def desc_lotacao(self):
        return self._desc_lotacao

    @desc_lotacao.setter
    def desc_lotacao(self, desc_lotacao: str):
        if not desc_lotacao:
            raise Exception("Descrição de lotação não encontrada!")
        self._desc_lotacao = desc_lotacao

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio: datetime):
        if not isinstance(data_inicio, datetime):
            raise ValueError("Data de início não encontrada!")
        self._data_inicio = data_inicio

    @property
    def empresa(self):
        return self._empresa

    @empresa.setter
    def empresa(self, empresa: str):
        if isinstance(empresa, Carreira):
            raise Exception("Empresa não encontrada!")
        self._empresa = empresa
