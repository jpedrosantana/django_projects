from .carrinho import Carrinho

#o unico método retorna um dicionário com o carrinho de compras da aplicação
def carrinho(request):
    resultado = {
        'carrinho': Carrinho(request)
    }
    return resultado

