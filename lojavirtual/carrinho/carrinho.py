#arquivo com a classe que representa a abstração de um carrinho de compras
from decimal import Decimal
from django.conf import settings
from main.models import Produto

class Carrinho:
    def __init__(self, request):
        self.__sessao = request.session #armazenamento da sessão atual
        carrinho = self.__sessao.get(settings.ID_CARRINHO) #localiza na sessão objeto correspondente a chave

        if not carrinho: #se não for inicializada, adiciona um dicionário vazio
            carrinho = self.__sessao[settings.ID_CARRINHO] = {}
        self.__carrinho = carrinho

    def adicionar(self, produto, quantidade=1, atualizar_quantidade=False):
        id_produto = str(produto.id) #str pois o Django usa JSON para serializar os dados
        if id_produto not in self.__carrinho: #se o produto não estiver no carrinho, inicia com qte zerada
            self.__carrinho[id_produto] = {
                'quantidade': 0,
                'preco': str(produto.preco),
            }
        if atualizar_quantidade:
            self._Carrinho__carrinho[id_produto]['quantidade'] = quantidade
        else:
            self._Carrinho__carrinho[id_produto]['quantidade'] += quantidade
        self.__salvar()

    def __salvar(self):
        self.__sessao[settings.ID_CARRINHO] = self.__carrinho #grava dados do carrinho na sessão
        self.__sessao.__alterada = True
        #self.__sessao.modified = True #informa ao django que a sessão sofreu modificação e deve ser salva

    def remover(self, produto):
        id_produto = str(produto.id)
        if produto.id in self.__carrinho:
            del self.__carrinho[id_produto]
            self.__salvar()

    def __iter__(self): #método que itera sobre os itens no carrinho e obtem objetos de produto armazenados
        ids_produtos = self.__carrinho.keys()
        produtos = Produto.objects.filter(id__in=ids_produtos)
        carrinho = self.__carrinho.copy()
        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto
        for item in carrinho.values():
            item['preco']=Decimal(item['preco'])
            item['subtotal']=Decimal(item['preco'])*Decimal(item['quantidade'])
            yield item

    def __len__(self): #retorna qte total de itens no carrinho
        resultado = 0
        for item in self.__carrinho.values():
            resultado += item['quantidade']
        return resultado

    def get_total_geral(self): #soma os subtotais dos produtos
        resultado = Decimal(0.0)
        for item in self.__carrinho.values():
            subtotal = Decimal(item['quantidade'])*Decimal(item['preco'])
            resultado = resultado + subtotal
        return resultado

    def limpar_carrinho(self):
        del self.__sessao[settings.ID_CARRINHO]
        self.__salvar()
'''
    def limpar_carrinho(self):
        for key in request.session.keys():
            del request.session[key]
            request.session.modified = True
'''
    