from django.urls import path
from . import views
from django.views.generic import TemplateView

#mapeamento das urls genéricas
app_name='main' #namespace
urlpatterns=[
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/<str:slug_categoria>/', views.listar_produtos, name='listar_produtos_por_categoria'),
    #path('produto/<int:id>/<str:slug_produto>/', views.detalhes_produto, name='detalhes_produto'),
    path('produto/<str:slug_produto>/', views.detalhes_produto, name='detalhes_produto'),
    ]