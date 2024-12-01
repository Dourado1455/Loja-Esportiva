from django.contrib import admin
from .models import Produto, NotaFiscal, Cliente, Fornecedor, Funcionario, ItemNotaFiscal

admin.site.register(Produto)
admin.site.register(NotaFiscal)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Funcionario)
admin.site.register(ItemNotaFiscal)
