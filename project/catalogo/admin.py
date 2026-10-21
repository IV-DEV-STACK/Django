from django.contrib import admin

# Register your models here.

from catalogo.models import Produto #importar tabela

admin.site.register(Produto) #registrar tabela

