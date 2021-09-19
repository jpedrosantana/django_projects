from django.forms import forms
from django.shortcuts import render
from django.views.generic.edit import FormView
from main import forms

# Create your views here.
class ViewFaleConosco(FormView):
    template_name="fale_conosco.html" #qual template será utilizado para renderizar os dados do form
    form_class= forms.FormFaleConosco #classe do formulário que a view instanciará para conter os dados
    success_url='/' #caso não haja excessões, local que será redirecionado

    def form_valid(self, form):
        form.enviar_mensagem_por_email()
        return super().form_valid(form)

