
class Pessoa:
    def __init__(self, nome, cpf, data_nascimento, email, tipo_sanguineo, sexo, estado_civil):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.tipo_sanguineo = tipo_sanguineo
        self.sexo = sexo
        self.estado_civil = estado_civil

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise ValueError("Nome do servidor incorreto !")
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if not isinstance(cpf, str):
            raise ValueError("Este CPF é invalido !")
        self._cpf = cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        if not isinstance(data_nascimento, str):
            raise ValueError("Esta data de nascimento não é valida !")
        self._data_nascimento = data_nascimento

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise ValueError("Este e-mail não é valido !")
        self._email = email

    @property
    def tipo_sanguineo(self):
        return self._tipo_sanguineo

    @tipo_sanguineo.setter
    def tipo_sanguineo(self, tipo):
        tipo_sanguineo_possivel = {'A+','A-','B+','AB+','O+','B-','AB-','O-'}
        if not tipo in tipo_sanguineo_possivel:
            raise ValueError("Este tipo sanguíneo não existe !")
        self._tipo_sanguineo = tipo

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, genero):
        genero_possivel = {'MASCULINO', 'FEMININO', 'OUTROS'}
        genero = genero.upper()
        if not genero in genero_possivel:
            raise ValueError("Este gênero não é valido !")
        self._sexo = genero

    @property
    def estado_civil(self):
        return self._estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil):
        estado_civil_possivel = {'SOLTEIRO', 'CASADO', 'SEPARADO','DIVORCIADO','VIÚVO'}
        estado_civil = estado_civil.upper()
        if not estado_civil in estado_civil_possivel:
            raise ValueError("Este estado civil não é valido !")
        self._estado_civil = estado_civil
