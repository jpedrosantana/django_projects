from django.contrib import admin
from .models import Categoria, Produto #importando as classes

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=['nome', 'slug'] #especifica os campos que serão mostrados na tela
    prepopulated_fields={'slug': ('nome',)} #informa ao django admin quais campos serão preenchidos automaticamente por persistência

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=['nome', 'slug', 'preco', 'estoque', 'disponivel', 
                'data_criacao', 'data_ultima_atualizacao']
    list_filter=['disponivel', 'data_criacao', 'data_ultima_atualizacao'] #especifica os campos que poderão ser usados para filtrar os dados
    list_editable=['preco', 'estoque', 'disponivel'] #indica campos editáveis, obrigatório que constem também no list_display
    prepopulated_fields={'slug':('nome',)}
