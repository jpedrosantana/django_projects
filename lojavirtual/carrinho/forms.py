from django import forms

OPCOES_QUANTIDADE_PRODUTO = []
for i in range(1,50):
    OPCOES_QUANTIDADE_PRODUTO.append((i, str(i))) #valor inteiro como controle, e strings como legenda

class FormAdicionarProdutoAoCarrinho(forms.Form):
    quantidade = forms.TypedChoiceField( #controle drop-down com as quantidades
        choides=OPCOES_QUANTIDADE_PRODUTO, coerce=int #valor convertido para inteiro (propriedade coerce)
    )
    atualizar = forms.BooleanField(required=False, widget=forms.HiddenInput)

