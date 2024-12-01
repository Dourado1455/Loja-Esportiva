from django.shortcuts import render
from .models import Produto

# View para listar os produtos
def listar_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos cadastrados
    return render(request, 'loja/listar_produtos.html', {'produtos': produtos})
