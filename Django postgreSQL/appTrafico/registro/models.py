from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class sensor(models.Model):

	nombre = models.CharField(max_length=50)
	
	def __str__(self):
		return " %s "%(self.nombre)


class sensor_dato(models.Model):
	SAMPACHO = 'SAM'
	RIO_CUARTO = 'RC'
	GENERAL_DEHEZA = 'GD' 
	UBICACION = [(SAMPACHO, 'Sampacho'), (RIO_CUARTO, 'Rio Cuarto'), (GENERAL_DEHEZA, 'General Deheza'),]
	nombre_sensor = models.ForeignKey(sensor, on_delete = models.CASCADE)
	ubicacion = models.CharField(max_length=50,choices = UBICACION, default = SAMPACHO,)
	temperatura = models.IntegerField(validators=[MinValueValidator(-10),MaxValueValidator(50)])
	presion = models.IntegerField(validators=[MinValueValidator(880),MaxValueValidator(1080)])
	humedad = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
	fecha = models.DateTimeField()
