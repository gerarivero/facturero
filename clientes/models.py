from django.db import models

# Create your models here.


class Cliente(models.Model):
	alta= 		models.DateTimeField(auto_now_add=True)
	cuil= 		models.CharField(max_length=11, unique=True, db_index=True)
	razon_social= models.CharField(max_length=100, blank= True)
	nombre= 	models.CharField(max_length=80)
	apellido= 	models.CharField(max_length=50)
	direccion=	models.CharField(max_length=100)
	telefono=	models.CharField(max_length=15)
	mail= 		models.EmailField()

	def __str__(self):
		return self.nombre + " " + self.apellido
		
	class Meta:
		ordering= ('nombre',)	

class Factura(models.Model):
	cliente= models.ForeignKey(Cliente)
	alta=	models.DateTimeField(auto_now_add=True)
	f_factura=	models.DateField()	
	f_vencimiento= models.DateField()

	FA = 'A'
	FB = 'B'
	FC = 'C'

	tipo_factura= (
		(FA, 'Factura A'),
		(FB, 'Factura B'),
		(FC, 'Factura C')
	)

	tipo= models.CharField(max_length=1, choices=tipo_factura, default=FB)
	detalle= models.CharField(max_length=200)

	def __str__(self):
		return 'Tipo: ' + self.tipo + ' de ' + self.cliente.nombre

	class Meta:
		ordering= ('f_vencimiento',)	

class LineaFactura(models.Model):
	factura= models.ForeignKey(Factura, on_delete= models.CASCADE)
	codigo_prod= models.IntegerField()
	detalle= models.CharField(max_length=200)
	cantidad= models.IntegerField(default=1)
	precio_unit= models.DecimalField(max_digits=6,decimal_places=2,default=0.00)	
	
	def _get_total(self):
		return self.cantidad * self.precio_unit
	
	total= property(_get_total)