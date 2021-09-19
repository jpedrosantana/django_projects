from django.test import TestCase
from django.urls import reverse

# Create your tests here.
#As classes herdam de TestCase e devem aplicar métodos conhecidos dessa classe
class TestarPaginas(TestCase):
    def testar_se_pagina_principal_carrega_completamente(self):
        response = self.client.get('/') #simula um browser wseb
        self.assertEqual(response.status_code, 200) #Assert compara uma resposta recebida com uma esperada
        self.assertTemplateUsed(response, 'base.html')
        #self.assertContains(response, 'Controle de Estoque')
        self.assertContains(response, 'Loja Virtual')

    def testar_se_pagina_ajuda_carrega_completamente(self):
        response=self.client.get(reverse('ajuda')) #reverse recebe uma constante e retorna a url que contem essa constante na propriedade name do arquivo urls.py
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, '<h2>Ajuda</h2>')