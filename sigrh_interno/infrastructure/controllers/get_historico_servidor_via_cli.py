"""
Pegar o servidor por cli
"""
from sigrh_interno.application.use_cases.buscar_dados_servidor_cpf import BuscarDadosServidorCpf
from sigrh_interno.infrastructure.exceptions.servidor_nao_encontrado_exception\
import ServidorNaoEncontradoException

from sigrh_interno.infrastructure.repository_implementation.servidor_repository_api_impl\
import ServidorRepositoryApiImpl


class GetHistoricoServidorViaCLI:
    """classe pegar o Servidor/Historico por CLI"""
    def __init__(self):
        self.servidor_repository = ServidorRepositoryApiImpl()
        self.use_case = BuscarDadosServidorCpf(self.servidor_repository)

    def run(self):
        """classe para rodar/iniciar"""
        while True:
            print('digite o cpf do servidor')
            input_cpf = input()
            try:
                servidor = self.use_case(input_cpf)
                print(servidor)
            except ServidorNaoEncontradoException:
                print('Servidor não encontrado.')
            except Exception:
                print('CPF está no formato invalido')
            print('----------------------------------------------')

    def __call__(self):
        return self.run()
