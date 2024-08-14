
from sigrh_interno.domain.entities.pessoa import Pessoa
from .categoria import Categoria
from .lotacao import Lotacao
from .vinculo import Vinculo
from .cargo import Cargo


class Servidor:
    def __init__(
            self,
            pessoa: Pessoa,
            matricula: str,
            lotacao: Lotacao,
            carga_horaria: int,
            cargo: Cargo,
            categoria: Categoria,
            vinculo: Vinculo
        ):
        self.pessoa = pessoa
        self.matricula = matricula
        self.lotacao = lotacao
        self.carga_horaria = carga_horaria
        self.cargo = cargo
        self.categoria = categoria
        self.vinculo = vinculo

    @property
    def pessoa(self):
        return self._pessoa

    @pessoa.setter
    def pessoa(self, pessoa: Pessoa):
        if (not pessoa or not isinstance(pessoa, Pessoa)):
            raise Exception("Nome da pessoa incorreto")
        self._pessoa = pessoa

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula: str):
        if not matricula:
            raise Exception("Descrição do cargo incorreto")
        self._matricula = matricula

    @property
    def lotacao(self):
        return self._lotacao

    @lotacao.setter
    def lotacao(self, lotacao: Lotacao):
        if (not lotacao or not isinstance(lotacao, Lotacao)):
            raise Exception("Lotação incorreta")
        self._lotacao = lotacao

    @property
    def carga_horaria(self):
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria : int):
        # Carga horaria minima de 20 horas semanais e maxima de 60 horas semanais
        if (carga_horaria < 20 or carga_horaria > 60):
            raise ValueError("Carga horaria invalida")
        self._carga_horaria = carga_horaria

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):

        if (not cargo or not isinstance(cargo, Cargo)):
            raise Exception("Cargo incorreto")
        self._cargo = cargo

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        if (not categoria or not isinstance(categoria, Categoria)):
            raise Exception("Categoria incorreta")
        self._categoria = categoria

    @property
    def vinculo(self):
        return self._vinculo

    @vinculo.setter
    def vinculo(self, vinculo):
        if (not vinculo or not isinstance(vinculo, Vinculo)):
            raise Exception("Vinculo incorreto")
        self._vinculo = vinculo
