from django import forms
from django.core.mail import send_mail
from lojavirtual import settings

#Importando o pacote forms e criando uma classe que herde de forms.Forms 
#que é a classe mãe de todos os formulários no Django
class FormFaleConosco(forms.Form):
    #initial faz a inicialização da classe ser descendente de form e não da view, permitindo inicializar o campo separadamente
    nome=forms.CharField(required=True, initial='Seu nome aqui') #Required indica preenchimento obrigatório
    email_origem=forms.EmailField(required=True, label='Entre com seu e-mail:')
    mensagem=forms.CharField(required=True, widget=forms.Textarea) #widget define qual o tipo do controle será usado para renderizar um componente do formulário

    def enviar_mensagem_por_email(self):
        send_mail('FALE CONOSCO: mensagem recebida',
            self.data['mensagem'],
            self.data['email_origem'],
            [settings.EMAIL_FALE_CONOSCO], 
            fail_silently=False) #faz com que erros sejam mostrados