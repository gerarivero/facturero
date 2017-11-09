from django.contrib import admin
from .models	import Cliente, Factura, LineaFactura
# Register your models here.





@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	pass


class detalle_x_linea(admin.TabularInline):
	list_display= ['cogido_prod','detalle','cantidad','precio_unit','total']
	readonly_fields= ('total',)
	model= LineaFactura
	extra=1

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
	fields= [('cliente','tipo'),('f_factura','f_vencimiento'),'detalle']
	inlines= [detalle_x_linea]