# Visualización de métricas

## ¿ Qué es grafana ?
<div style="text-align:justify">Grafana es una herramienta para visualizar datos de serie temporales. A partir de una serie de datos recolectados se obtiene un panorama gráfico de la situación muy simple de interpretar y visualizar, se utiliza para el monitoreo de infraestructura de IT, mediciones de aplicaciones, control de procesos, sensores industriales, automatización de hogares y medición del clima entre otros usos.</div>

![Grafana](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Logo-grafana.png)

<div style="text-align:justify">El objetivo de Grafana es presentar los datos de monitoreo de una manera más fácil de usar y agradable, recolectada y/o procesada por aplicaciones de terceros, aunque puede recopilar de forma nativa datos de Cloudwatch, Graphite, Elasticsearch, OpenTSDB, Prometheus, Hosted Metrics e InfluxDB. Tambien existe una versión Enterprise de Grafana (grafana.com) que usa complementos para otras fuentes de datos y ofrece soporte 24×7, pero en general estos complementos de fuentes de datos pueden crearse de fuente abierta.</div>

<div style="text-align:justify">Como editor de métricas flexible, ofrece la posibilidad de crear paneles de control genéricos que se pueden cambiar rápidamente para mostrar diferentes estadísticas de un cluster, servidor o aplicaciones específicas. Gracias a su rapidez y flexibilidad, los nombres de grupo, hosts, aplicaciones o nombres de elementos pueden ser reemplazados con solamente cambiar una variable dentro de la plantilla.</div>

<div style="text-align:justify">Grafana asimismo facilita la obtención de los datos a partir de docenas de bases de datos, de forma nativa, y que pueden ser mezcladas fácilmente en el mismo tablero. Un tablero o dashboard de Grafana es una vista que contiene múltiples gráficos y paneles individuales organizados en forma de grilla. Los dashboards son el concepto clave detrás de Grafana, pues son el medio a través del cual se logra simplificar y agrupar métricas en una vista simple y amigable con el objetivo de mejorar la comprensión sobre los datos e información disponible. También es posible definir reglas de alertas de forma visual para las métricas más importantes. Grafana evalúa estas reglas de forma permanente y continua y envía notificaciones en diferentes formas.</div>

### ¿Cómo crear un dashboard en Grafana?

<div style="text-align:justify">Después de instalar Grafana, accederemos a su interfaz web para empezar con la creación de los dashboards. Una vez hagamos login tendremos que configurar un Data Source, que será desde donde Grafana obtenga los datos de las métricas. De este modo, podremos crear un dashboard presionando el botón New dashboard.</div>

<div style="text-align:justify">Para el caso de nuestra infraestructura de red, tenemos que realizar la siguiente configuración: </div>

![ConfiguracionDataSource](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Configuracion_datasource_influx.png)

<div style="text-align:justify">Lo que indica a Grafana que la fuente de datos se encuentra <em>http://172.21.0.4:8086</em> y corresponde una base de datos de InfluxDB.</div>


## ¿Qué es InfluxDB?

<div style="text-align:justify">InfluxDB es un sistema de gestión de bases de datos desarrollado por la empresa InfluxData, Inc. como software de código abierto, por lo que puede ser utilizado de forma gratuita. Sin embargo existe una versión comercial que proporciona algunos servicios adicionales.</div>

<div style="text-align:justify">InfluxDB ha sido concebido para bases de datos de time series (TSDB), que almacenan series temporales. Estas bases de datos se usan, entre otras cosas, para almacenar y evaluar datos de sensores o protocolos con marcas temporales durante un período de tiempo determinado.</div>

<div style="text-align:justify">En estos casos es posible que entren millones de juegos de datos, como los que proporcionan los equipos del Internet de las cosas o los instrumentos científicos de medición a través de un flujo continuo de datos. Este tipo de datos deben procesarse rápidamente en cuanto llegan a la base de datos.
Por ello, InfluxDB cuenta con un servicio de tiempo que usa el Network Time Protocol (NTP) para garantizar que el tiempo está sincronizado en todos los sistemas.</div>

<div style="text-align:justify">Las bases de datos de InfluxDB suelen ser muy compactas y solo necesitan contar con dos o tres columnas. En ellas se guarda, por ejemplo, la fuente de los datos, el valor en sí y la marca temporal correspondiente.</div>

![EstructuraInflux](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Estructura_Influxdb.PNG)

<div style="text-align:justify">InfluxDB distingue entre tags y fields. Mientras que los tags solo contienen metadatos incluidos en el índice, los fields incluyen valores que pueden evaluarse más adelante. Por lo tanto, en nuestro ejemplo, la primera columna es una tag y la segunda, un field. Esta distinción facilita el manejo de la base de datos y la evaluación de los datos de medición.</div>

<H5>¿Donde observamos los datos de nuestra base de datos influxDB en forma de tabla ?</H5>

<div style="text-align:justify">En <strong>Chronograf</strong>. Este servicio es la interfaz de usuario y el componente administrativo de la plataforma InfluxDB 1.x. Como herramienta, ademas de visualizar la estructura de la base de datos, trae integrada diferentes plantillas y bibliotecas para crear cuadros de mando rápidamente con visualizaciones en tiempo real. Muy parecido a Grafana.</div>

<div style="text-align:justify">Chronograf permite ver rápidamente los datos que se han almacenado en InfluxDB para que pueda generar consultas y alertas sólidas. De esta forma, al conocer la manera que está estructurada la base de datos, resulta más sencillo realizar consultas desde Grafana. </div>

### ¿Cuáles son las ventajas de InfluxDB?

<div style="text-align:justify">Las TSDB como InfluxDB son mucho más rápidas que las bases de datos relacionales a la hora de almacenar y procesar datos de medición con marcas temporales. Un sistema de gestión de bases de datos (DBMS) dedica parte de su rendimiento a la organización de un índice complejo, que en este ámbito de aplicación no se usa. InfluxDB también es capaz de mantener una elevada velocidad de escritura, ya que usa un índice muy sencillo.</div>

### Monitoreo de Postgres
<div style="text-align:justify">Para el monitoreo y visualizacion de metricas referidas a postgres es necesario incluir otra fuente de datos influxdb definida como <em>telegraf</em>. Esta ultima, esta junto a la base de datos de <em>influx</em> donde se almacenan metricas de Django, Locust y Cadvisor. La unica diferencia es que la base de datos <em>telegraf</em> solo recibe metricas de un unico agente (contenedor telegraf) dedicado puramente y exclusivamente al monitoreo de postgres.</div>

![ConfiguracionPostgres](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Configuracion_datasource_telegraf.png)

## Inclusión de link para reporte a PDF y apitoken 

<div style="text-align:justify">Con la finalidad de poder obtener los reportes de las distintas simulaciones realizadas y que se deseen realizar, es que al esquema dockerizado se le ha incorporado el servicio “reporter” con el único sentido de poder obtener y guardar mediante un PDF los dashboard de Grafana. Para poder obtener estos reportes, es que se debe realizar una configuración adicional sobre los dashboard que estén creados. En Settings, se debe ir hasta “Links” y luego completar los campos de la siguiente manera:</div>

![ConfiguracionDashboardReporte](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Contenido_visualizacion_settings.png)

<div style="text-align:justify">En el campo de URL se debe ingresar la IP asignada al servicio “reporter” seguido de “/api/report” y luego el nombre del dashboard tal como figura en el navegador, en este ejemplo en particular era “postgres-overview”. Quedando esta url de la siguiente manera:</div>

http://172.20.0.10:8686/api/report/postgres-overview?apitoken=*clave apitoken*=

<div style="text-align:justify">Esto nos añade en la esquina superior derecha del dashboard un botón el cual nos redireccionará en una nueva pestana a realizar el reporte en PDF</div>

![BotonReporte](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Contenido_visualizacion_registropdf.png)

<div style="text-align:justify">Si se presta atención a la dirección antes presentada, se puede observar que seguido al nombre del dashboard se encuentra la palabra “apitoken” acompañado de su clave. Este es un argumento fundamental y el cual nos permite limitar el acceso o visibilidad de los dashboard. Como para acceder a Grafana se ha configurado un usuario y contraseña, para poder exportar los dashboard a otros servicios, es necesario que se cuente con un “apitoken” o “apikey” el cual da los permisos para que los servicios tengan acceso a los dashboard. Para poder obtener esta clave es que en la esquina superior izquierda, sobre el icono de Grafana, se debe de clickear y dirigir a Admin -> Apikey.</div>

![CreacionApikey](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Contenido_visualizacion_apikey.png)

<div style="text-align:justify">Una vez que se está en la pestaña de API Keys, se debe asignar un nombre a la key y clickear en Add, esto nos abrirá una ventana con el código que se mostrará por única vez.</div>

![ObtencionKey](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Contenido_visualizacion_apikeyclave.png)

<div style="text-align:justify">El próximo paso es copiar la key y se debe pegar en la url del link para poder generar el reporte. De esta manera el servicio “reporter” tendrá acceso al dashboard y podrá realizar el PDF con los parámetros configurados en el dashboard.</div>

