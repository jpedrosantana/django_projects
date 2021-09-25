"""lojavirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajuda/', TemplateView.as_view(template_name='ajuda.html'), name='ajuda'),
    path('fale-conosco/', views.ViewFaleConosco.as_view(), name='fale_conosco'),
    #path("", TemplateView.as_view(template_name='index.html'), name='index'), #o django entende a string vazia como um mapeamento para a pagina principal do projeto
    path('carrinho', include('carrinho.urls', namespace='carrinho')),
    path('', include('main.urls', namespace='main')) #urls genéricas
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

