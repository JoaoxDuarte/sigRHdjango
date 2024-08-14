from datetime import datetime
from random import randint

from faker import Faker
from sigrh_interno.domain.entities.cargo import Cargo
from sigrh_interno.domain.entities.carreira import Carreira
from sigrh_interno.domain.entities.categoria import Categoria
from sigrh_interno.domain.entities.empresa import Empresa
from sigrh_interno.domain.entities.lotacao import Lotacao
from sigrh_interno.domain.entities.pessoa import Pessoa
from sigrh_interno.domain.entities.servidor import Servidor
from sigrh_interno.domain.entities.vinculo import Vinculo


def data_nascimento_fake(fake):
    return fake.date_between_dates(date_start=datetime(1960,1,1),
                                    date_end=datetime(2004,1,1)).year


def email_fake_format(fake, nome_fake):
    email_fake = nome_fake + fake.ascii_free_email()
    email_fake = nome_fake + "@" + email_fake.split("@")[-1]
    email_fake = email_fake.replace(' ','').lower()
    return email_fake


def tipo_sanguinio():
    tipo_sanguinio_possivel = ['A+','A-','B+','AB+','O+','B-','AB-','O-']
    tipo_sanguinio_fake = tipo_sanguinio_possivel[randint(0,7)]
    return tipo_sanguinio_fake


def servidor_fake():

    fake = Faker('pt_BR')
    empresa = Empresa(randint(1,9999),'DescricaoEmpresa', 'EMP')
    categoria = Categoria(randint(1,9999),'descricao')
    lotacao = Lotacao(randint(1,9999),'descricao',25,empresa)
    vinculo = Vinculo(randint(1,9999),'tipo_vinculo')
    carreira = Carreira(randint(1,9999),'descricaoCarreira')
    cargo = Cargo(randint(1,9999),'descricaoCargo', carreira)

    genero_possivel = ["Masculino", "Feminino", "Outros"]

    estado_civil_possivel = ['SOLTEIRO', 'CASADO','DIVORCIADO','VIÚVO']
    estado_civil_fake = estado_civil_possivel[randint(0,3)]

    genero_fake = genero_possivel[randint(0,2)]
    if genero_fake == "Masculino":
        nome_fake = fake.name_male()
    elif genero_fake == "Feminino":
        nome_fake = fake.name_female()
    else:
        nome_fake = fake.name()

    pessoa = Pessoa(nome_fake, fake.cpf(),str(data_nascimento_fake(fake)),
                   email_fake_format(fake, nome_fake),
                   tipo_sanguinio(),genero_fake,estado_civil_fake)
    servidor = Servidor(pessoa, randint(10000,99999), lotacao,20,cargo,categoria,vinculo)
    return servidor
