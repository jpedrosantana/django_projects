from django import forms
from .models import Pedido

#Form para encapsular detalhes dos pedidos
class FormCriarPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'logradouro', 'numero', 'complemento',
                    'bairro', 'cidade', 'uf', 'cep']
