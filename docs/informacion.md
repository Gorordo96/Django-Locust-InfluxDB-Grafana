# Información

## ¿Como ejecutar el proyecto?

<div style="text-align:justify">
Al descargar la carpeta correspondiente al proyecto, presente en el repositorio "Versiones Finales", debemos abrir una consola de comandos en la raiz del mismo, precisamente donde se encuentra el archivo docker-compose.yml y ejecutar:
</div>

`` docker-compose up``

<div style="text-align:justify">
Este simple comando llevara a cabo una serie de instrucciones predefinidas que levantaran automaticamente entre 7 a 9 servicios, dependiendo de la base de datos que se este utilizando. Estos servicios son:
</div>

* **Django** en la siguiente ubicacion: _172.2x.0.2:8010_
* **Locust** en la siguiente ubicacion: _172.2x.0.3:8089_
* **Influxdb** en la siguiente ubicacion: _172.2x.0.4:8086_
* **Chronograf** en la siguiente ubicacion: _172.2x.0.5:8888_
* **Grafana** en la siguiente ubicacion: _172.2x.0.6:3000_
* **cAdvisor** en la siguiente ubicacion: _172.2x.0.7:8080_
* **PostgreSQL** (opcional) en el caso de estar usando esta db: _172.20.0.8_
* **Telegraf** (opcional) en la siguiente ubicacion: _172.20.0.9_
* **Reporter** en la siguiente ubicacion: _172.2x.0.10:8686_


![DockerFile](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Estructura_docker.png)

<div style="text-align:justify">
Como puede observarse, todos los contenedores pertenecen a la misma red interna "172.2x.0.0/16" (en donde la 'x' sera 0 si se usa PostgreSQL o 1 si se usa Sqlite3)  y son capaces de comunicarse bajo  cualquier arquitectura de red sobre la cual se levante. Con respecto al ultimo servicio, "Reporter", tiene unicamente la tarea de importar las metricas de Grafana a PDF.
Para comprender mas en detalle como es que interactuan entre si los distintos servicios se debe de observar la siguiente figura:</div>

![Conexion_de_Servicios](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Diagrama_Servicios_SQlite.jpg)

<div style="text-align:justify">Esta portabilidad de la estructura entera es gracias a los beneficios que aporta Docker Compose a la tecnologia Docker, ya que Docker Compose es una herramienta que permite simplificar el uso de Docker. A partir de archivos YAML es mas sencillo crear contendores, conectarlos, habilitar puertos, volumenes, etc.
Con Compose se puede crear diferentes contenedores y al mismo tiempo, en cada contenedor, diferentes servicios, unirlos a un volúmen común, iniciarlos y apagarlos, etc. Es un componente fundamental para poder construir aplicaciones y microservicios.
En vez de utilizar Docker via una serie inmemorizable de comandos bash y scripts, Docker Compose  permite mediante archivos YAML, poder instruir al Docker Engine a realizar tareas, preprogramadas. Y esta es la clave, la facilidad para dar una serie de instrucciones, y luego repetirlas en diferentes ambientes.
A continuacion se hara una descripcion del archivo para la implementacion con SQlite:
</div>

``` 
version: '3.2'

services:
 web:
  build: appTrafico
  command: python manage.py runserver 172.21.0.2:8010
  volumes:
   - ./appTrafico:/TraficoGyL
  ports:
   - "8010:8010"
  networks:
   red_servicios:
    ipv4_address: 172.21.0.2
  container_name: Django_SQlite

 locust:
  build: ScriptLocust
  command: -f /mnt/locust/Test_locust_regUser_08-11-2020.py
  volumes:
   - ./ScriptLocust:/mnt/locust
  ports:
   - "8089:8089"
  links:
   - web:web
  networks:
   red_servicios:
    ipv4_address: 172.21.0.3
  container_name: Locust_SQlite

 influxdb:
  build: influxdb
  env_file: configuration.env
  ports:
   - '8086:8086'
  volumes:
   - influxdb_data:/var/lib/influxdb
  networks:
   red_servicios:
    ipv4_address: 172.21.0.4
  container_name: Influxdb_SQlite


 chronograf:
  image: chronograf:1.5
  volumes:
   - chronograf_data:/var/lib/chronograf
  ports:
   - '8087:8888'
  networks:
   red_servicios:
    ipv4_address: 172.21.0.5
  container_name: Chronograf_SQlite

 grafana:
  build: grafana
  env_file: configuration.env
  links:
   - influxdb
  ports:
   - '3000:3000'
  volumes:
   - grafana_data:/var/lib/grafana
   - ./grafana/dashboard:/var/lib/grafana/dashboards
  networks:
   red_servicios:
    ipv4_address: 172.21.0.6
  container_name: Grafana_SQlite

 reporter:
  image: izakmarais/grafana-reporter:${gr_version:-latest}
  command: "-ip 172.21.0.6:3000"
  ports:
    - "8686:8686"
  networks:
   red_servicios:
    ipv4_address: 172.21.0.10
  container_name: Reporter_Grafana_SQlite     

 cadvisor:
  image: google/cadvisor
  command: -storage_driver=influxdb -storage_driver_db=influx -storage_driver_host=172.21.0.4:8086
  ports:
   - "8080:8080"
  volumes:
   - /:/rootfs:ro
   - /var/run:/var/run:rw
   - /sys:/sys:ro
   - /var/lib/docker/:/var/lib/docker:ro
  links:
   - influxdb:influxdb 
  privileged: true
   
  networks:
   red_servicios:
    ipv4_address: 172.21.0.7
  container_name: cAdvisor_SQlite

networks:
 red_servicios:
  driver: bridge
  ipam:
   config:
    - subnet: 172.21.0.0/16

volumes:
  grafana_data: {}
  influxdb_data: {}
  chronograf_data: {}


```

1- La primera linea del archivo acusa una instruccion **"version:"**. Indica la version base de compose que se esta utilizando para construir cada contenedor. ¿Que cambia elegir una version u otra? La variedad y forma de ejecutar los comandos para construir los contenedores.

* Enlace de referencia: https://docs.docker.com/compose/compose-file/compose-versioning/

2- **"services:"** es la segunda linea dentro del archivo y es tan importante como la primera. Especifica los servicios que estaran presentes en cada contenedor. Como se puede observar en la porcion de codigo expuesta anteriormente, ellos se denominan como: web,locust,influxdb,grafana,etc.
 Cada uno de ellos, tiene configurado varios parametros. Entre ellos se encuentran:

2.1- **build**:  especifica la ubicación de nuestro Dockerfile. Un Dockerfile es un archivo de texto plano que contiene una serie de instrucciones necesarias para crear una imagen que, posteriormente, se convertirá en una sola aplicación utilizada para un determinado propósito.
 ![DockerFile](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/imagen.png)

 Teniendo presente que en el trabajo se estan realizando pruebas con 2 bases datos diferentes, en el segundo caso se implementa PostgreSQL, en donde se configuran 2 servicios adicionales que corresponden a la propia base de datos y a Telegraf. Siendo su docker compose correspondiente, el siguiente:
 
```
 
version: '3.2'

services:

 web:
  build: appTrafico
  command: python manage.py runserver 172.20.0.2:8010
  volumes:
   - ./appTrafico:/TraficoGyL
  ports:
   - "8010:8010"
  depends_on:
   - db
  networks:
   red_servicios:
    ipv4_address: 172.20.0.2
  container_name: Django

 db:
  image: postgres:13.0
  environment:
   - POSTGRES_DB=postgres
   - POSTGRES_USER=postgres
   - POSTGRES_PASSWORD=postgres
  volumes:
   - postgres_data:/var/lib/postgresql/data
   - ./postgres/postgresql.conf:/etc/postgresql/postgresql.conf
  command: postgres -c config_file=/etc/postgresql/postgresql.conf
  networks:
   red_servicios:
    ipv4_address: 172.20.0.8
  container_name: Postgres

 locust:
  build: ScriptLocust
  command: -f /mnt/locust/Test_locust_regUser_08-11-2020.py
  volumes:
   - ./ScriptLocust:/mnt/locust
  ports:
   - "8089:8089"
  links:
   - web:web
  networks:
   red_servicios:
    ipv4_address: 172.20.0.3
  container_name: Locust

 influxdb:
  build: influxdb
  env_file: configuration.env
  ports:
   - '8086:8086'
  volumes:
   - influxdb_data:/var/lib/influxdb
  networks:
   red_servicios:
    ipv4_address: 172.20.0.4
  container_name: Influxdb


 chronograf:
  image: chronograf:1.5
  volumes:
   - chronograf_data:/var/lib/chronograf
  ports:
   - '8087:8888'
  networks:
   red_servicios:
    ipv4_address: 172.20.0.5
  container_name: Chronograf

 telegraf:
  image: telegraf:1.16
  volumes:
   - ./telegraf/telegraf.conf:/etc/telegraf/telegraf.conf:ro
   - /var/run/docker.sock:/var/run/docker.sock
  links:
   - influxdb
  networks:
   red_servicios:
    ipv4_address: 172.20.0.9
  container_name: Telegraf  
  

 grafana:
  build: grafana
  env_file: configuration.env
  links:
   - influxdb
  ports:
   - '3000:3000'
  volumes:
   - grafana_data:/var/lib/grafana
   - ./grafana/dashboard:/var/lib/grafana/dashboards
  networks:
   red_servicios:
    ipv4_address: 172.20.0.6
  container_name: Grafana

 reporter:
  image: izakmarais/grafana-reporter:${gr_version:-latest}
  command: "-ip 172.20.0.6:3000"
  ports:
    - "8686:8686"
  networks:
   red_servicios:
    ipv4_address: 172.20.0.10
  container_name: Reporter_Grafana   


 cadvisor:
  image: google/cadvisor
  command: -storage_driver=influxdb -storage_driver_db=influx -storage_driver_host=172.20.0.4:8086
  ports:
   - "8080:8080"
  volumes:
   - /:/rootfs:ro
   - /var/run:/var/run:rw
   - /sys:/sys:ro
   - /var/lib/docker/:/var/lib/docker:ro
  links:
   - influxdb:influxdb 
  privileged: true
   
  networks:
   red_servicios:
    ipv4_address: 172.20.0.7
  container_name: cAdvisor

networks:
 red_servicios:
  driver: bridge
  ipam:
   config:
    - subnet: 172.20.0.0/16

volumes:
  grafana_data: {}
  influxdb_data: {}
  chronograf_data: {}
  postgres_data: {}
  
```
 
 Para los servicios web, el archivo dockerfile contiene las siguientes instrucciones: 

 * **FROM** indica que debe utilizarse una imagen existente como base que se encuentra alojada en el sitio web "docker hub"
 * **ENV PYTHONUNBUFFERED 1** indica que debe imprimirse por pantalla los detalles de la ejecucion del dockerfile. Esto permite llevar un control y saber en que parte del codigo se producen errores.
 * **RUN** es una instruccion que permite ejecutar comandos dentro del contenedor. En este caso, dentro de la imagen base referenciada por FROM, se creara una carpeta denominada "TraficoGyL"
 * **WORKDIR** El comando se usa para definir el directorio de trabajo de un contenedor Docker en un momento dado. Si no se especifica, docker crea automaticamente un entorno diferente. Para que dicho entorno coincida con la carpeta que creamos, debemos utilizar el comando WORKDIR.
 * **COPY** Este comando permite copiar archivos presentes en el mismo entorno donde esta alojado el dockerfile para que se hagan presentes dentro del contenedor. Esto nos resulta util, ya que definimos todos los paquetes python necesarios para el contenedor junto con sus versiones dentro del archivo requerimientos.txt y lo copiamos a la carpeta TraficoGyL dentro del contenedor.
 * **RUN** Ejecutamos un comando para instalar todos los paquetes necesarios dentro del contenedor y preparar la imagen para levantar el servicio.
 * **COPY** Este ultimo comando copia toda la aplicacion relacionada al servicio a la carpeta de trabajo.

```
FROM python:3.7.9-buster

ENV PYTHONUNBUFFERED 1   

RUN mkdir /TraficoGyL

WORKDIR /TraficoGyL

COPY requerimientos.txt /TraficoGyL 

RUN pip3 install -r requerimientos.txt     
     
COPY . /TraficoGyL
```
<div style="text-align:justify">
Una vez preparado el dockerfile, desde el archivo ".yml" solamente debe indicarse la ruta donde esta presente. En nuestro caso, todo lo relacionado al servicio web, tanto la aplicacion en si, como el archivo dockerfile y requerimientos.txt se encuentran en la carpeta "appTrafico". Por eso la linea build: "appTrafico".
</div>

2.2- **command**: indica que en la construccion del servicio debe ejecutarse un comando particular dentro del contenedor. Para el caso de la aplicacion web, como se esta utilizando django, debe ejecutarse un comando como: python manage.py runserver (direccionIP:puerto). Esto permite que al finalizar docker-compose este presente y listo el servicio web.

2.3-**volumes**: Establece que un directorio del sistema operativo estara presente de una direccion particular dentro del contenedor. Esto permite importar toda la aplicacion web dentro del contenedor, y al realizar cambios en el directorio, esos cambios instantaneamente estaran presentes dentro del contenedor. Esto facilita realizar operaciones y cambios en el contenedor, sin tener que ingresar constantemente o trabajar dentro del mismo.

2.4- **ports**: Establece que se van a exponer los puertos del contenedor a determinados puertos del host. esto permite que los servicios y contenedores sean accesibles ademas desde fuera de la estructura dockerizada. 

2.5- **network**: Establece que se utilizara una estructura de red interna asociada al grupo de contenedores donde cada uno tendra una direccion ip diferente.

Algunos contenedores tienen ademas otros comandos como **links** que permiten vincular de forma explicita los diferentes servicios. Si bien ya estan dentro de la misma red y no deberia haber ningun tipo de inconveniente, se agrega dicha instruccion para apuntar un servicio a otro, esto genera que ante cualquier cambio de un contenedor, la configuracion se mantenga funcional.
Los contenedores influxdb y grafana, fueron agregados teniendo en cuenta un repositorio de github, cuya referencia se encuentra a continuacion: 

* https://github.com/BushnevYuri/DockerGrafanaInfluxKit


Este proyecto funcional, incluye ademas, configuraciones adicionales que son dignas de analizar. Entre ellas **env_file**. Este argumento dentro de docker-compose permite especificar un archivo donde se encuentran variables de entorno que permiten configurar de forma dinamica el servicio dentro del contenedor.


```
###################
# Grafana options
###################
GF_SECURITY_ADMIN_USER=admin
GF_SECURITY_ADMIN_PASSWORD=admin
GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-worldmap-panel,grafana-piechart-panel
####################
# InfluxDB options
####################
INFLUX_USER=admin
INFLUX_PASSWORD=admin
INFLUX_DB=influx
```

## ¿Se necesita algun procedimiento adicional?

La primera vez que se va a ejecutar el proyecto debe realizar migraciones de la aplicacion  en django. Para ello, debe identificar el "id" del contenedor con el nombre "django". Entonces luego de inicializar toda la estructura con docker-compose up, en otra terminal ejecute los siguientes comandos como super usuario: 

```
docker ps

docker exec -i -t <id_conteiner_django> /bin/bash

python manage.py migrate

```
Estos comandos ejecutados unicamente la primera vez, dejarian lista toda la estructura docker para ejecutar cualquier tipo de prueba. Si adicionalmente, desea realizar las mismas pruebas de performance que se detallan en este informe, debera realizar un paso adicional. Registrar los usuarios simulados que cargaran datos sobre la base de datos. Para ello, con toda la estructura activa debera ejecutar el archivo python denominado como "Cargar_Usuarios_Django.py". Este ejecutable python generara el registro de una cantidad determinada de usuarios (Variable definida dentro del Script) de forma automatica y entrega finalmente un archivo de extension ".txt" que contendra los usuarios y contraseñas generados y cargados que leera locust para ejecutar cada prueba.
Los comandos que debera llevar a cabo son: 

```

python Cargar_Usuarios_Django.py

docker-compose down

docker-compose up 

```
El reinicio de la estructura es necesario para que el archivo de texto se mapee dentro del contenedor locust y pueda ser accedido por el propio servicio. Sin mas detalles, quedara todo el entorno listo, para ejecutar pruebas de performance. Detalle importante: Si ya realizo todos estos pasos en su equipo donde va a desarrollar las pruebas de performance, no debe realizarlo nuevamente a menos que elimine todos los volumenes e imagenes asociadas al proyecto.

### Importante Aclaracion

Los comandos detallados anteriormente, sirve para la estructura con PostgreSQL , ya que para la estructura de servicios con SQLite3 la base de datos viene integrada y conectada con la aplicacion, asi como con todos los datos con los que se estuvo probando. Para SQLite lo unico que necesita hacer es docker-compose up.

En caso de querer limpiar la base de datos pero conservar los modelos, debera seguir los siguientes pasos:

```
docker ps

docker exec -i -t <id_conteiner_django> /bin/bash

python manage.py flush

```
En caso de querer eliminar la base de datos con sus modelos y armar una aplicacion distinta, primero debera eliminar el archivo de base de datos SQLite3 y posteriormente ejecutar:

```
docker ps

docker exec -i -t <id_conteiner_django> /bin/bash

python manage.py migrate

```




