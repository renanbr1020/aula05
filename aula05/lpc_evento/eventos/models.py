from django.db import models
from django.contrib.auth.models import User 

class Endereco (models.Model):
    logradouro  = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=2,null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField (max_length=10)
      
    def __str__(self):
        return '{} - {}, {}'.format(self.logradouro,self.cidade,self.uf)


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='endereco', null=True, blank=False)
    usuario = models.OneToOneField(User)
    
    def __str__(self):
        return self.nome

class PessoaFisica (Pessoa):
    cpf = models.CharField(max_length=20)
    mae = models.CharField(max_length=128)
    pai = models.CharField(max_length=128)

    class Meta ():
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'

class Evento(models.Model):
    realizador = models.ForeignKey(PessoaFisica, related_name='pessoasFisicas',null=True, blank=False)
    endereco = models.ForeignKey(Endereco, related_name='enderecos', null=True)

    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    sigla = models.CharField(max_length=5,null=True)
    numero = models.CharField(max_length=10,null=True)
    ano = models.DateField()
    
class Inscricao (models.Model):
    evento = models.ForeignKey(Evento, related_name='eventos', null=True, blank=False)
    pessoa = models.ForeignKey(PessoaFisica, related_name='participantes', null=True, blank=False)
    data = models.DateTimeField()
    preco = models.FloatField()

    class Meta ():
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
    