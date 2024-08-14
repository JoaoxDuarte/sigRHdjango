"""
implementação do repositório do servidor
"""
from datetime import datetime
import os
import xml.etree.ElementTree as ET
import requests
from sigrh_interno.domain.entities.carreira import Carreira
from sigrh_interno.domain.entities.servidor import Servidor
from sigrh_interno.domain.entities.vinculo import Vinculo
from sigrh_interno.domain.entities.cargo import Cargo
from sigrh_interno.domain.entities.categoria import Categoria
from sigrh_interno.domain.entities.empresa import Empresa
from sigrh_interno.domain.entities.lotacao import Lotacao

from sigrh_interno.infrastructure.exceptions.\
servidor_nao_encontrado_exception import ServidorNaoEncontradoException

from ...domain.repositories.servidor_repository import ServidorRepository
from ...domain.entities.pessoa import Pessoa


class ServidorRepositoryApiImpl(ServidorRepository):
    """
    Classe da implementação da API do respositório
    """
    def __init__(self):
        self.url = f'{os.getenv("SIGRHAPI_URL")}{os.getenv("API_TOKEN")}/buscarHistoricoServidor/'

    def get_pessoa(self,servidor_node):
        """Pegar a entidade pessoa"""
        nome_servidor = servidor_node.findtext('nome')
        cpf_servidor = servidor_node.findtext('cpf')
        data_nascimento_servidor = servidor_node.findtext('dataNascimento')
        email_servidor = servidor_node.findtext('email')
        tipo_sanguineo_servidor = servidor_node.findtext('tipoSanguineo')
        sexo_servidor = servidor_node.findtext('sexo')
        estado_civil_servidor = servidor_node.findtext('estadoCivil')

        entidade_pessoa = Pessoa(nome_servidor,
            cpf_servidor,
            data_nascimento_servidor,
            email_servidor,
            tipo_sanguineo_servidor,
            sexo_servidor,
            estado_civil_servidor )
        return entidade_pessoa

    def get_empresa(self,empresa_node):
        """Pegar a entidade empresa"""
        cod_empresa =  int(empresa_node.findtext('codEmpresa'))
        desc_empresa = empresa_node.findtext('descEmpresa')
        sigla_empresa = empresa_node.findtext('siglaEmpresa')

        entidade_empresa = Empresa(cod_empresa, desc_empresa, sigla_empresa)
        return entidade_empresa

    def get_lotacao(self,lotacao_node, entidade_empresa):
        """Pegar a entidade lotacao"""
        cod_lotacao = int(lotacao_node.findtext('codLotacao'))
        desc_lotacao = lotacao_node.findtext('descLotacao')
        data_inicio = datetime.strptime(lotacao_node.findtext('dataInicio'),'%d/%m/%Y')
        entidade_lotacao = Lotacao(cod_lotacao, desc_lotacao, data_inicio, entidade_empresa)
        return entidade_lotacao

    def get_carreira(self,carreira_node):
        """Pegar a entidade carreira"""
        cod_carreira = int(carreira_node.findtext('codCarreira'))
        desc_carreira = carreira_node.findtext('descCarreira')
        entidade_carreira = Carreira(cod_carreira, desc_carreira)
        return entidade_carreira

    def get_cargo(self, cargo_node, entidade_carreira):
        """Pegar a entidade cargo"""
        cod_cargo = int(cargo_node.findtext('codCargo'))
        desc_cargo = cargo_node.findtext('descCargo')
        entidade_cargo = Cargo(cod_cargo, desc_cargo, entidade_carreira)
        return entidade_cargo

    def get_categoria(self, categoria_node):
        """Pegar a entidade categoria"""
        cod_categoria = int(categoria_node.findtext('codCategoria'))
        desc_categoria = categoria_node.findtext('descCategoria')
        entidade_categoria = Categoria(cod_categoria, desc_categoria)
        return entidade_categoria

    def get_vinculo(self, vinculo_node):
        """Pegar a entidade vinculo"""
        cod_vinculo = int(vinculo_node.findtext('codTipoVinculo'))
        desc_vinculo = vinculo_node.findtext('tipoVinculo')
        entidade_vinculo = Vinculo(cod_vinculo, desc_vinculo)
        return entidade_vinculo




    def get_servidor_by_cpf(self, cpf: str):
        cpf = cpf.replace('.', '').replace('-', '')
        xml_response = requests.get(self.url + cpf, timeout=500)
        xml_model = ET.fromstring(xml_response.content)
        if int(xml_model.find('status').findtext('codMensagem')) != 200:
            raise ServidorNaoEncontradoException()
        lotacao_node = xml_model.find('servidor').find('lotacao')

        entidade_pessoa = self.get_pessoa(xml_model.find('servidor'))


        #Empresa
        entidade_empresa = self.get_empresa(lotacao_node.find('empresa'))
        #lotacao
        entidade_lotacao = self.get_lotacao(lotacao_node, entidade_empresa)
        #carreira
        entidade_carreira = self.get_carreira(lotacao_node.find('carreira'))

        #cargo
        entidade_cargo = self.get_cargo(lotacao_node.find('cargo'),entidade_carreira)

        #categoria
        entidade_categoria = self.get_categoria(lotacao_node.find('categoria'))

        #vinculo
        entidade_vinculo = self.get_vinculo(lotacao_node.find('vinculo'))


        #matricula
        matricula = lotacao_node.findtext('matricula')

        #carga horaria
        carga_horaria =  int(lotacao_node.findtext('cargaHoraria'))
        entidade_servidor = Servidor(entidade_pessoa,
                            matricula,
                            entidade_lotacao,
                            carga_horaria,
                            entidade_cargo,
                            entidade_categoria,
                            entidade_vinculo)

        return entidade_servidor

    def get_servidor_by_matricula(self, matricula: str):
        return None

    def get_servidor_by_orgao(self, orgao:str):
        return None
