from random import randrange, sample
from faker import Faker

from sigrh_interno.domain.repositories.servidor_repository import ServidorRepository
from sigrh_interno.application.use_cases.sever_exists_in_list_cpf import SeverExistsInListCpf

fake = Faker('pt_BR')

fake_cpf = fake.cpf()
print(fake_cpf)


class ServidorRepoistoryMock(ServidorRepository):
    def __init__(self, cpf_list):
        self.cpf_list = cpf_list

    def get_servidor_by_cpf(self, cpf: str):
        if cpf in self.cpf_list:
            return object()
        raise Exception()

    def get_servidor_by_matricula(self, matricula):
        return None

    def get_servidor_by_orgao(self, orgao: str):
        return None


def test_capture_existing_cpf():
    #AAA - Arrange | Act | Assert
    # Arrange - preparar tudo que você vai usar | Fazer mocks/stubs
    reference_cpf = fake.cpf()
    repository = ServidorRepoistoryMock([reference_cpf])
    use_case = SeverExistsInListCpf(repository)

    # Act - Realizar a ação que você deseja testar
    cpf_found, cpf_invalid = use_case.run([reference_cpf])

    # Assert - Testar se o resultado foi o esperado
    assert cpf_found == [reference_cpf]
    assert len(cpf_invalid) == 0


def test_capture_invalid_cpf():
    # Arrange
    reference_cpf = '00000000079'
    repository = ServidorRepoistoryMock([])
    use_case = SeverExistsInListCpf(repository)

    # Act
    cpf_found, cpf_invalid = use_case.run([reference_cpf])

    # Assert
    assert len(cpf_found) == 0
    assert cpf_invalid == [reference_cpf]


def test_functionality_working_for_complex_case():
    # Arrange
    valid_cpf = []
    invalid_cpf = []
    for _ in range(10):
        valid_cpf.append(fake.cpf())
        invalid_cpf.append(
            '000000000' + str(randrange(1, 9)) + str(randrange(1, 9)))

    reference_cpf = sample(valid_cpf, 4)

    repository = ServidorRepoistoryMock(reference_cpf)
    use_case = SeverExistsInListCpf(repository)

    # Act
    cpf_found, cpf_invalid = use_case.run(valid_cpf + invalid_cpf)

    # Assert
    assert set(cpf_found) == set(reference_cpf)
    assert set(cpf_invalid) == set(invalid_cpf)
