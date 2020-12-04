from django.urls import path
from . import views #es la referencia relativa de en donde esta views.py


app_name= 'registro'
urlpatterns = [
	path('nuevo',views.nuevo_usuario,name="nuevo_usuario"),
	path('ingresar',views.ingresar,name="ingresar"),
	path('privado',views.privado,name="privado"),
	path('datocargado',views.privado,name="datocargado"),
	path('procUser',views.procUser,name="procesado_usuario"),
]
