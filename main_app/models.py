from django.db import models

# Create your models here.

class PessoaModel(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=320)
    tipo_sanguineo = models.CharField(max_length=3)
    sexo = models.CharField(max_length=9)
    estado_civil = models.CharField(max_length=10)


class EmpresaModel(models.Model):
    cod_empresa = models.IntegerField(primary_key=True)
    desc_empresa = models.CharField(max_length=300)
    sigla_empresa = models.CharField(max_length=6)

class LotacaoModel(models.Model):
    cod_lotacao = models.IntegerField(primary_key=True)
    desc_lotacao = models.CharField(max_length=300)
    data_inicio = models.DateField()
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)


class CarreiraModel(models.Model):
    cod_carreira = models.IntegerField(primary_key=True)
    desc_carreira = models.CharField(max_length=300)

class CargoModel(models.Model):
    cod_cargo = models.IntegerField(primary_key=True)
    desc_cargo = models.CharField(max_length=300)
    carreira = models.ForeignKey(CarreiraModel,on_delete=models.CASCADE)

class CategoriaModel(models.Model):
    cod_categoria = models.IntegerField(primary_key=True)
    desc_categoria = models.CharField(max_length=300)

class VinculoModel(models.Model):
    cod_vinculo = models.IntegerField()
    tipo_vinculo = models.CharField(max_length=20)

class ServidorModel(models.Model):
    pessoa = models.ForeignKey(PessoaModel, on_delete=models.CASCADE)
    lotacao = models.ForeignKey(LotacaoModel, on_delete=models.CASCADE)
    cargo = models.ForeignKey(CargoModel, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    vinculo = models.ForeignKey(VinculoModel, on_delete=models.CASCADE)

    matricula = models.CharField(max_length=15)
    carga_horaria = models.IntegerField()
