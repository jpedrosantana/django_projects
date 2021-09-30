from django.contrib import admin
from .models import Pedido, ItemPedido

# Register your models here.
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido #define qual classe será editada na linha de detalhe do Admin
    raw_id_fields = ['produto'] #lupa para buca

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'logradouro', 'numero', 'complemento', 
                    'bairro', 'cidade', 'uf', 'cep', 'data_criacao', 'pago']
    list_filtar = ['pago', 'data_criacao', 'nome']
    inlines = [ItemPedidoInline]

admin.site.register(Pedido, PedidoAdmin)
