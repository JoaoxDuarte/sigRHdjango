"""
implementação do teste da api do repositório do servidor
"""
from unittest.mock import patch
from sigrh_interno.infrastructure.repository_implementation.\
servidor_repository_api_impl import(ServidorRepositoryApiImpl)


#Abrir arquivo xml
class MockedRequestResponse:
    """Abrindo arquivo mock xml"""
    def __init__(self):
        with (open('tests/infrastructure/repository_implementation/response.example.xml',
             'r',encoding='utf-8') as example_response):
            self.content = example_response.read()

@patch('requests.get', return_value=MockedRequestResponse())
def test_can_parse_the_response_xml(mock):
    """teste passando o arquivo em XML"""
    repository_impl = ServidorRepositoryApiImpl()
    servidor = repository_impl.get_servidor_by_cpf('24433632015')

    assert servidor.pessoa.nome == 'FULANO DE TAL'
    assert servidor.pessoa.cpf == '24433632015'
    assert servidor.pessoa.tipo_sanguineo == 'AB+'

    assert servidor.matricula == '12801323'

    assert servidor.vinculo.cod_vinculo == 7

    assert servidor.lotacao.cod_lotacao == 50205010000
    assert servidor.lotacao.empresa.sigla_empresa == 'SEDEST'
