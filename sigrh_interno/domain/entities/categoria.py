class Categoria:
    def __init__(self, cod_categoria: int, desc_categoria: str):
        self.cod_categoria = cod_categoria
        self.desc_categoria = desc_categoria

    @property
    def cod_categoria(self):
        return self._cod_categoria

    @cod_categoria.setter
    def cod_categoria(self, cod_categoria: int):
        if cod_categoria < 1:
            raise ValueError("Código de categoria não encontrado!")
        self._cod_categoria = cod_categoria

    @property
    def desc_categoria(self):
        return self._desc_categoria

    @desc_categoria.setter
    def desc_categoria(self, desc_categoria: str):
        if not desc_categoria:
            raise ValueError("Descrição de categoria não encontrada!")
        self._desc_categoria = desc_categoria
