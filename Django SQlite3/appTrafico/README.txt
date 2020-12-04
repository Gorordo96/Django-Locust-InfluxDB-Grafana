Necesitas las librerias "plotly" y "kaleido" para obtener graficas.
para instalar, los comandos son: --> pip install plotly
				 --> pip install -U kaleido

Para correr al servidor, es recomendable tener una unica salida a internet. Para que pueda ser accedido dentro de la red lan
se debe ejecutar el comando python manage.py runserver "IPCONCONEXIONAINTERNET":"PUERTO". Puerto puede ser a eleccion. Preferentemente
8010 ya que 8080 genera error y 8089 es el servicio Locust.