class Evento:
    def __init__(self, cod_evento: int, desc_evento: str):
        self.cod_evento = cod_evento
        self.desc_evento = desc_evento

    @property
    def cod_evento(self):
        return self._cod_evento

    @cod_evento.setter
    def cod_evento(self, cod_evento: int):
        if cod_evento >= 1:
            self._cod_evento = cod_evento
            return self._cod_evento
        raise ValueError("Erro no código!")

    @property
    def desc_evento(self):
        return self._desc_evento

    @desc_evento.setter
    def desc_evento(self, desc_evento: str):
        if not isinstance(desc_evento, str) or desc_evento == '':
            raise ValueError("Erro na descrição")
        self._desc_evento = desc_evento
        return self._desc_evento
