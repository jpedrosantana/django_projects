from django.shortcuts import render
from .models import ItemPedido
from .forms import FormCriarPedido
from carrinho.carrinho import Carrinho
from django.core import serializers

# Create your views here.
def criar_pedido(request):
    carrinho = Carrinho(request)
    if request.method == 'POST':
        form = FormCriarPedido(request.POST)
        if form.is_valid():
            pedido = form.save() #Salva o pedido no banco
            carrinho.limpar_carrinho()
        
        return render(request, 'pedidos/pedido/concluir.html', {'pedido': pedido})
            
    else:
        form = FormCriarPedido() #cria objeto vazio
        return render(request, 'pedidos/pedido/criar.html', {'carrinho': carrinho, 'form': form})