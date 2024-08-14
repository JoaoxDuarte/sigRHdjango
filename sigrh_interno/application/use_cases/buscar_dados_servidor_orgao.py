from ...domain.repositories.servidor_repository import ServidorRepository

class BuscarDadosServidorOrgao:
    def __init__(self, servidor_repository : ServidorRepository):
        self.servidor_repository = servidor_repository

    def run(self, orgao : str):
        return self.servidor_repository.get_servidor_by_orgao(orgao)
    