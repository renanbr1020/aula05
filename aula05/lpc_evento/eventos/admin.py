from django.contrib import admin

# Register your models here.

from django.contrib import admin
from eventos.models import Pessoa,Endereco,PessoaFisica, Evento, Inscricao

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(Inscricao)