class Funcao:
    def __init__(self, cod_func: int, desc_funcao: str):
        self.cod_func = cod_func
        self.desc_funcao = desc_funcao

    @property
    def cod_func(self):
        return self._cod_func

    @cod_func.setter
    def cod_func(self, cod_func: int):
        if cod_func >= 1:
            self._cod_func = cod_func
            return self._cod_func
        raise ValueError("Erro no código")

    @property
    def desc_funcao(self):
        return self._desc_funcao

    @desc_funcao.setter
    def desc_funcao(self, desc_funcao: str):
        if not isinstance(desc_funcao, str) or desc_funcao == "":
            raise ValueError("Erro na descrição")
        self._desc_funcao = desc_funcao
        return self.desc_funcao
