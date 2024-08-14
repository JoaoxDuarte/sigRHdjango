class Carreira:
    def __init__(self, cod_carreira: int, desc_carreira: str):
        self.cod_carreira = cod_carreira
        self.desc_carreira = desc_carreira

    @property
    def cod_carreira(self):
        return self._cod_carreira

    @cod_carreira.setter
    def cod_carreira(self, cod_carreira: int):
        if cod_carreira <= 0:
            raise ValueError("codigo da carreira incorreto")
        self._cod_carreira = cod_carreira

    @property
    def desc_carreira(self):
        return self._desc_carreira

    @desc_carreira.setter
    def desc_carreira(self, desc_carreira: str):
        if not desc_carreira:
            raise Exception("Descrição de carreira incorreta")
        self._desc_carreira = desc_carreira
