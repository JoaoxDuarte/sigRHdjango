from ...domain.entities.carreira import Carreira


class Cargo:
    def __init__(self, cod_cargo: int, desc_cargo: str, carreira: Carreira):
        self.cod_cargo = cod_cargo
        self.desc_cargo = desc_cargo
        self.carreira = carreira

    @property
    def cod_cargo(self):
        return self._cod_cargo

    @cod_cargo.setter
    def cod_cargo(self, code_cargo: int):
        if code_cargo < 1:
            raise ValueError("Codigo do cargo incorreto")
        self._cod_cargo = code_cargo

    @property
    def desc_cargo(self):
        return self._desc_cargo

    @desc_cargo.setter
    def desc_cargo(self, desc_cargo: str):
        if not desc_cargo:
            raise Exception("Descrição do cargo incorreto")
        self._desc_cargo = desc_cargo

    @property
    def carreira(self):
        return self._carreira

    @carreira.setter
    def carreira(self, carreira: str):
        if not isinstance(carreira, Carreira):
            raise Exception("Carreira do cargo incorreta")
        self._carreira = carreira
