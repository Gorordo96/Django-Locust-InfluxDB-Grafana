from django import forms
from .models import sensor, sensor_dato


class SensorForm(forms.ModelForm):
	
	class Meta:
		model = sensor_dato
		fields = ('ubicacion','temperatura','presion','humedad')


class usuarioForm(forms.Form):

	UBICACION = [('RC','Rio Cuarto'),('SAM','Sampacho'),('GD','General Deheza')]
	DATOS = [('TEMP','Temperatura'),('PRE','Presion'),('HUM','Humedad')]
	SelecUbic=forms.MultipleChoiceField(required=False,label='ubicacion',widget=forms.CheckboxSelectMultiple(),choices=UBICACION)
	SelecDato=forms.MultipleChoiceField(required=False,label='dato',widget=forms.CheckboxSelectMultiple(),choices=DATOS)



