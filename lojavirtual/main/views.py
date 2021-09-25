from django.forms import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from main import forms
from .models import Categoria, Produto

# Create your views here.
class ViewFaleConosco(FormView):
    template_name="fale_conosco.html" #qual template será utilizado para renderizar os dados do form
    form_class= forms.FormFaleConosco #classe do formulário que a view instanciará para conter os dados
    success_url='/' #caso não haja excessões, local que será redirecionado

    def form_valid(self, form):
        form.enviar_mensagem_por_email()
        return super().form_valid(form)

    
def listar_produtos(request, slug_categoria=None):
    categoria = None
    lista_categorias = Categoria.objects.all() #carregada com todas as categorias
    lista_produtos = Produto.objects.filter(disponivel=True) #carregada com filtro dos produtos disponiveis

    if slug_categoria:
        categoria=get_object_or_404(Categoria, slug=slug_categoria)
        lista_produtos = Produto.objects.filter(categoria=categoria)
    contexto={
            'categoria': categoria,
            'lista_categorias': lista_categorias,
            'lista_produtos': lista_produtos,
        }
    return render(request, 'produto/listar.html', contexto)


def detalhes_produto(request, slug_produto):
    produto=get_object_or_404(Produto, slug=slug_produto, disponivel=True)
    contexto = {
        'produto': produto,
    }
    return render(request, 'produto/detalhes.html', contexto)

"""

def detalhes_produto(request, id, slug_produto):
    produto=get_object_or_404(Produto, id=id, slug=slug_produto, disponivel=True)
    contexto = {
        'produto': produto,
    }
    return render(request, 'produto/detalhes.html', contexto)
"""
