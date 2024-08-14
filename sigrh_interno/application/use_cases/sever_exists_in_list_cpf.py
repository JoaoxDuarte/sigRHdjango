from ...domain.repositories.servidor_repository import ServidorRepository
from ..util.valida_cpf import valida_cpf


class SeverExistsInListCpf:
    def __init__(self, servidor_repository: ServidorRepository):
        self.servidor_repository = servidor_repository

    def run(self, list_cpf: list[str]):
        cpf_invalid = []
        cpf_found = []
        for cpf in list_cpf:
            try:
                valida_cpf(cpf)
            except Exception:
                cpf_invalid.append(cpf)
                continue
            try:
                self.servidor_repository.get_servidor_by_cpf(cpf)
                cpf_found.append(cpf)
            except Exception:
                pass

        return (cpf_found, cpf_invalid)
