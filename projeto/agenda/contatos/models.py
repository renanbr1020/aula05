from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField ('nome', max_length =50)
    descricao = models.TextField()
    data_nascimento = models.DateTimeField (blank=True, null=True) #não precisa ser obrigatório
    telefone = models.CharField('telefone',max_length =20,blank=True, null=True)

def __str__(self):
    return self.nome