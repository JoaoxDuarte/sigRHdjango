class Empresa:
    def __init__(self, cod_empresa, desc_empresa, sigla_empresa):
        self.cod_empresa = cod_empresa
        self.desc_empresa = desc_empresa
        self.sigla_empresa = sigla_empresa

    @property
    def cod_empresa(self):
        return self._cod_empresa

    @cod_empresa.setter
    def cod_empresa(self, cod_empresa):
        if cod_empresa < 1:
            raise ValueError("Valor do codigo da empresa incorreto")
        self._cod_empresa = cod_empresa

    @property
    def desc_empresa(self):
        return self._desc_empresa

    @desc_empresa.setter
    def desc_empresa(self, desc_empresa):
        if desc_empresa == str:
            raise ValueError("Descrição dessa empresa não existe !")
        self._desc_empresa = desc_empresa
