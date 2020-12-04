from django.forms import forms
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from .forms import SensorForm, usuarioForm
from .models import sensor, sensor_dato 
from django.views.generic import ListView
from datetime import datetime
import csv
from plotly.offline import plot
import plotly.graph_objects as go
import os
import math
import statistics as stats



# Create your views here.

def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			nombre_sensor = sensor(nombre = request.POST['username'])
			nombre_sensor.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()

	return render(request, 'registro/nuevousuario.html',{'formulario':formulario})

def ingresar(request):	
	if not request.user.is_anonymous:
		return HttpResponseRedirect(reverse('registro:privado'))
	if request.method=='POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username= usuario, password= clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect(reverse('registro:privado'))
					#return render(request, 'registro/privado.html')				
				else:
					return render(request, 'registro/noactivo.html')
			else:
				return render(request,'registro/nousuario.html')
	else:
		formulario = AuthenticationForm()
	return render(request, 'registro/ingresar.html',{'formulario':formulario})

@login_required(login_url='/ingresar')
def privado(request):
	if request.method=='GET':
		usuario=request.user
		formulario = SensorForm()
		return render(request,'registro/privado.html',{'usuario':usuario, 'formulario':formulario})
	else:
		formulariopost = SensorForm(request.POST)
		if formulariopost.is_valid():
			nombresensor_post=sensor.objects.get(nombre=request.user)
			ubicacion_post = request.POST['ubicacion']
			temperatura_post = request.POST['temperatura']
			presion_post = request.POST['presion']
			humedad_post = request.POST['humedad']
			sensor_posteo=sensor_dato(nombre_sensor=nombresensor_post,ubicacion=ubicacion_post,temperatura=temperatura_post,presion=presion_post,humedad=humedad_post,fecha=datetime.now())
			sensor_posteo.save()
			cantdatos=20
			Dato_Proc=sensor_dato.objects.filter(nombre_sensor=nombresensor_post.id)[:cantdatos]
		else:
			return HttpResponse("Se cargaron mal los datos")

		etiquetas=["","","","","","","","",""]

		Lista_datos_temp_RC = [variable.temperatura for variable in Dato_Proc if variable.ubicacion == 'RC']
		Lista_datos_presion_RC=[variable.presion for variable in Dato_Proc if variable.ubicacion == 'RC']
		Lista_datos_humedad_RC=[variable.humedad for variable in Dato_Proc if variable.ubicacion == 'RC']
		Eje_X_RC=[variable.fecha for variable in Dato_Proc if variable.ubicacion == 'RC']
		Lista_datos_temp_SAM = [variable.temperatura for variable in Dato_Proc if variable.ubicacion == 'SAM']
		Lista_datos_presion_SAM = [variable.presion for variable in Dato_Proc if variable.ubicacion == 'SAM']
		Lista_datos_humedad_SAM = [variable.humedad for variable in Dato_Proc if variable.ubicacion == 'SAM']
		Eje_X_SAM = [variable.fecha for variable in Dato_Proc if variable.ubicacion == 'SAM']
		Lista_datos_temp_GD = [variable.temperatura for variable in Dato_Proc if variable.ubicacion == 'GD']
		Lista_datos_presion_GD = [variable.presion for variable in Dato_Proc if variable.ubicacion == 'GD']
		Lista_datos_humedad_GD = [variable.humedad for variable in Dato_Proc if variable.ubicacion == 'GD']
		Eje_X_GD = [variable.fecha for variable in Dato_Proc if variable.ubicacion == 'GD']

		#---------------------------------------------------------------------------------------------------------
		#Creacion de la grafica propiamente dicha.
		#Rio Cuarto:
		layout=go.Layout(title="Temperatura en Rio Cuarto",xaxis_title="datos subidos",yaxis_title="Temperatura en grados")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_RC,y= Lista_datos_temp_RC,mode='lines',name='test',opacity=0.8, marker_color='red')
		figura.add_trace(grafica)
		html_div1_1 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[0] = html_div1_1

		layout=go.Layout(title="Presion en Rio Cuarto",xaxis_title="datos subidos",yaxis_title="Presion en HectoPascales")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_RC,y= Lista_datos_presion_RC,mode='lines',name='test',opacity=0.8, marker_color='green')
		figura.add_trace(grafica)
		html_div2_1 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[1] = html_div2_1


		layout=go.Layout(title="Humedad en Rio Cuarto",xaxis_title="datos subidos",yaxis_title="Humedad como porcentaje")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_RC,y= Lista_datos_humedad_RC,mode='lines',name='test',opacity=0.8, marker_color='blue')
		figura.add_trace(grafica)
		html_div3_1 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[2] = html_div3_1

		#------------------------------------------------------------------------------------------------------------------
		#Sampacho:

		layout=go.Layout(title="Temperatura en Sampacho",xaxis_title="datos subidos",yaxis_title="Temperatura en grados")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_SAM,y= Lista_datos_temp_SAM,mode='lines',name='test',opacity=0.8, marker_color='red')
		figura.add_trace(grafica)
		html_div1_2 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[3] = html_div1_2

		layout=go.Layout(title="Presion en Sampacho",xaxis_title="datos subidos",yaxis_title="Presion en HectoPascales")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_SAM,y= Lista_datos_presion_SAM,mode='lines',name='test',opacity=0.8, marker_color='green')
		figura.add_trace(grafica)
		html_div2_2 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[4] = html_div2_2

		layout=go.Layout(title="Humedad en Sampacho",xaxis_title="datos subidos",yaxis_title="Humedad como porcentaje")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_SAM,y= Lista_datos_humedad_SAM,mode='lines',name='test',opacity=0.8, marker_color='blue')
		figura.add_trace(grafica)
		html_div3_2 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[5] = html_div3_2

		#-------------------------------------------------------------------------------------------------------------------
		#General Deheza

		layout=go.Layout(title="Temperatura en General Deheza",xaxis_title="datos subidos",yaxis_title="Temperatura en grados")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_GD,y= Lista_datos_temp_GD,mode='lines',name='test',opacity=0.8, marker_color='red')
		figura.add_trace(grafica)
		html_div1_3 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[6] = html_div1_3

		layout=go.Layout(title="Presion en General Deheza",xaxis_title="datos subidos",yaxis_title="Presion en HectoPascales")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_GD,y= Lista_datos_presion_GD,mode='lines',name='test',opacity=0.8, marker_color='green')
		figura.add_trace(grafica)
		html_div2_3 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[7] = html_div2_3

		layout=go.Layout(title="Humedad en General Deheza",xaxis_title="datos subidos",yaxis_title="Humedad como porcentaje")
		figura=go.Figure(layout=layout)
		grafica=go.Scatter(x=Eje_X_GD,y= Lista_datos_humedad_GD,mode='lines',name='test',opacity=0.8, marker_color='blue')
		figura.add_trace(grafica)
		html_div3_3 = plot(figura, include_plotlyjs=False, output_type='div')
		etiquetas[8] = html_div3_3

		return render(request, 'registro/datocargado.html',{'Lista':Dato_Proc,'etiquetas':etiquetas})


def procUser(request):
	if request.method == 'GET':
		formulariousuario=usuarioForm()
		return render(request, 'registro/procUser.html',{'formuser':formulariousuario})
	else:
		formularioresp=usuarioForm(request.POST)
		if formularioresp.is_valid():

			ubicacion_valor=formularioresp.cleaned_data.get("SelecUbic")
			dato_valor=formularioresp.cleaned_data.get("SelecDato")
			etiquetas=["","","","","","","","",""] # TEMP,PRES,HUM ->RC TEMP,PRES,HUM ->SAMP TEMP,PRES,HUM ->GD
			rang_temporal=["","","","","",""]

			if (len(ubicacion_valor) > 0) and (len(dato_valor) > 0):
				cantdatosarec=100
				for consultaubic in ubicacion_valor:
					basedatosrec_proc=sensor_dato.objects.filter(ubicacion=consultaubic)[:cantdatosarec]

					if 'TEMP' in dato_valor:
						temperaturarec=[]
						label=["-10 < Temp < -5","-5 < Temp < -0","0 < Temp < 5","5 < Temp < 10","10 < Temp < 15","-15 < Temp < 20","20 < Temp < 25","25 < Temp < 30","30 < Temp < 35","35 < Temp < 40","40 < Temp < 45","45 < Temp < 50"]
						contadores=[0,0,0,0,0,0,0,0,0,0,0,0]

						for filadebasedatos in basedatosrec_proc:
							contadores[math.trunc((filadebasedatos.temperatura+10)/5)]=contadores[math.trunc((filadebasedatos.temperatura+10)/5)]+1
							temperaturarec.append(filadebasedatos.temperatura)

						if consultaubic == 'RC':
							layout = go.Layout(title="Distribucion de Temperatura en Rio Cuarto", xaxis_title="Temperatura en grados",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout,data=[go.Pie(labels=label,values=contadores)])
							html_div1_1 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[0]=html_div1_1
							rang_temporal[0]=basedatosrec_proc[0].fecha
							rang_temporal[1]=basedatosrec_proc[len(basedatosrec_proc)-1].fecha

						if consultaubic == 'SAM':
							layout = go.Layout(title="Distribucion de Temperatura en Sampacho",xaxis_title="Temperatura en grados",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout, data=[go.Pie(labels=label,values=contadores)])
							html_div1_2 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[1] = html_div1_2
							rang_temporal[2] = basedatosrec_proc[0].fecha
							rang_temporal[3] = basedatosrec_proc[len(basedatosrec_proc) - 1].fecha

						if consultaubic == 'GD':
							layout = go.Layout(title="Distribucion de Temperatura en General Deheza",xaxis_title="Temperatura en grados",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout, data=[go.Pie(labels=label,values=contadores)])
							html_div1_3 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[2]=html_div1_3
							rang_temporal[4] = basedatosrec_proc[0].fecha
							rang_temporal[5] = basedatosrec_proc[len(basedatosrec_proc) - 1].fecha

					if 'PRE' in dato_valor:
						presionrec = []
						label = ["880 < Pres < 905", "905 < Pres < 930", "930 < Pres < 955", "955 < Pres < 980", "980 < Pres < 1005","1005 < Pres < 1030", "1030 < Pres < 1055", "1055 < Pres < 1080"]
						contadores = [0, 0, 0, 0, 0, 0, 0, 0]

						for filadebasedatos in basedatosrec_proc:
							contadores[math.trunc((filadebasedatos.presion - 880) / 25)] = contadores[math.trunc((filadebasedatos.presion - 880) / 25)] + 1
							presionrec.append(filadebasedatos.presion)

						if consultaubic == 'RC':
							layout = go.Layout(title="Distribucion de presion en Rio Cuarto", xaxis_title="Presion en Hectopascales",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout,data=[go.Pie(labels=label,values=contadores)])
							html_div2_1 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[3]=html_div2_1
							rang_temporal[0] = basedatosrec_proc[0].fecha
							rang_temporal[1] = basedatosrec_proc[len(basedatosrec_proc) - 1].fecha

						if consultaubic == 'SAM':
							layout = go.Layout(title="Distribucion de presion en Sampacho",xaxis_title="Presion en Hectopascales",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout, data=[go.Pie(labels=label,values=contadores)])
							html_div2_2 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[4]=html_div2_2
							rang_temporal[2] = basedatosrec_proc[0].fecha
							rang_temporal[3] = basedatosrec_proc[len(basedatosrec_proc) - 1].fecha

						if consultaubic == 'GD':
							layout = go.Layout(title="Distribucion de presion en General Deheza",xaxis_title="Presion en Hectopascales",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout, data=[go.Pie(labels=label,values=contadores)])
							html_div2_3 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[5]=html_div2_3
							rang_temporal[4] = basedatosrec_proc[0].fecha
							rang_temporal[5] = basedatosrec_proc[len(basedatosrec_proc) - 1].fecha

					if 'HUM' in dato_valor:
						humedadrec=[]
						contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
						label=["0<Hum<5","5<Hum<10","10<Hum<15","15<Hum<20","20<Hum<25","25<Hum<30","30<Hum<35","35<Hum<40","40<Hum<45","45<Hum<50","50<Hum<55","55<Hum<60","60<Hum<65","65<Hum<70","70<Hum<75","75<Hum<80","80<Hum<85","85<Hum<90","90<Hum<95","95<Hum<100"]
						for filadebasedatos in basedatosrec_proc:
							contadores[math.trunc((filadebasedatos.humedad) / 5)] = contadores[math.trunc((filadebasedatos.humedad) / 5)] + 1
							humedadrec.append(filadebasedatos.humedad)


						if consultaubic == 'RC':
							layout = go.Layout(title="Distribucion de Humedad en Rio Cuarto", xaxis_title="Humedad en porcentaje",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout,data=[go.Pie(labels=label,values=contadores)])
							html_div3_1 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[6]=html_div3_1
							rang_temporal[0] = basedatosrec_proc[0].fecha
							rang_temporal[1] = basedatosrec_proc[len(basedatosrec_proc) - 1].fecha

						if consultaubic == 'SAM':
							layout = go.Layout(title="Distribucion de Humedad en Sampacho",xaxis_title="Humedad en porcentaje",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout, data=[go.Pie(labels=label,values=contadores)])
							html_div3_2 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[7]=html_div3_2
							rang_temporal[2] = basedatosrec_proc[0].fecha
							rang_temporal[3] = basedatosrec_proc[len(basedatosrec_proc) - 1].fecha

						if consultaubic == 'GD':
							layout = go.Layout(title="Distribucion de Humedad en General Deheza",xaxis_title="Humedad en porcentaje",yaxis_title="acumulacion de valores")
							fig = go.Figure(layout=layout, data=[go.Pie(labels=label,values=contadores)])
							html_div3_3 = plot(fig, include_plotlyjs=False, output_type='div')
							etiquetas[8]=html_div3_3
							rang_temporal[4] = basedatosrec_proc[0].fecha
							rang_temporal[5] = basedatosrec_proc[len(basedatosrec_proc) - 1].fecha

				return render(request, 'registro/datopUser.html',{'ubicacion':ubicacion_valor,'dato':dato_valor,'etiquetas':etiquetas,'rango_temp':rang_temporal})
			else:
				return HttpResponse("Se produjo un error, no puede dejar los campos vacios")
		else:
			return HttpResponse("Se produjo un error")


