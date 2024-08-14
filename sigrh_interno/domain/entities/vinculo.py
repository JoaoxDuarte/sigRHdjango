# CodVinculo
#TipoVinculo (descricaoVinculo)

class Vinculo:
    def __init__(self, cod_vinculo: int, tipo_vinculo: str):
        self.cod_vinculo = cod_vinculo
        self.tipo_vinculo = tipo_vinculo

    @property
    def cod_vinculo(self):
        return self._cod_vinculo

    @cod_vinculo.setter
    def cod_vinculo(self, cod_vinculo):
        if cod_vinculo >= 1:
            self._cod_vinculo = cod_vinculo
            return self._cod_vinculo
        raise ValueError("Código de vinculo errado!")

    @property
    def tipo_vinculo(self):
        return self._tipo_vinculo

    @tipo_vinculo.setter
    def tipo_vinculo(self, tipo_vinculo):
        if isinstance(tipo_vinculo, str) and not len(tipo_vinculo) == 0:
            self._tipo_vinculo = tipo_vinculo
            return self._tipo_vinculo
        raise ValueError("Tipo de vinculo incorreto!")
