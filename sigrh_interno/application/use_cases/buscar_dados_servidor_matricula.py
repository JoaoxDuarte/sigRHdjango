from ...domain.repositories.servidor_repository import ServidorRepository

class BuscarDadosServidorMatricula:
    def __init__(self, servidor_repository: ServidorRepository):
        self.servidor_repository = servidor_repository

    def run(self, matricula: str):
        return self.servidor_repository.get_servidor_by_matricula(matricula)
        