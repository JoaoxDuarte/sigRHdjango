from sigrh_interno.application.use_cases.buscar_dados_servidor_cpf import BuscarDadosServidorCpf
from sigrh_interno.domain.repositories import servidor_repository
from sigrh_interno.infrastructure.controllers.get_historico_servidor_via_cli import GetHistoricoServidorViaCLI
from sigrh_interno.infrastructure.repository_implementation.servidor_repository_api_impl import ServidorRepositoryApiImpl
from dotenv import load_dotenv
if __name__ == '__main__':
    load_dotenv()
    controller = GetHistoricoServidorViaCLI()
    controller()
