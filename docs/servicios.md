# Servicios

<div style="text-align:justify">
En esta instancia es conveniente destacar que para el desarrollo de una aplicación web existen muchas opciones. Dentro de ellas, es posible visualizar que existen un gran número de framework y CMS(Sistemas de Gestión de Contenidos o Content Management Systems por sus siglas en inglés). 
</div>


## ¿Qué es un framework?

<div style="text-align:justify">
Un framework es un marco de trabajo. En programación hace referencia a una serie de herramientas con las que puedes construir algo más fácil y rápido con algún lenguaje de programación. En el caso de desarrollo web, se denominan frameworks de aplicaciones web. Este tipo de marco de trabajo es un tipo de framework que permite el desarrollo de sitios web dinámicos, web services (servicios web) y aplicaciones web.
</div>

<div style="text-align:justify">
El propósito de este tipo de framework es permitir a los desarrolladores construir aplicaciones web y centrarse en los aspectos interesantes, aliviando la típica tarea repetitiva asociada con patrones comunes de desarrollo web. La mayoría de los frameworks de aplicaciones web proporcionan los tipos de funcionalidad básica común, tales como sistemas de templates (plantillas), manejo de sesiones de usuario, interfaces comunes con el disco o el almacenamiento en base de datos de contenido cacheado, y persistencia de datos. Normalmente, los frameworks de aplicación web además promueven la reutilización y conectividad de los componentes, así como la reutilización de código, y la implementación de bibliotecas para el acceso a base de datos.
</div>

### Si existe un gran número de framework, ¿Qué criterio seria necesario para elegir uno?

<div style="text-align:justify">
En desarrollos de gran magnitud, un framework de calidad proporciona una estructura simple y sencilla para organizar el proyecto. Además de otorgarle al desarrollador la suficiente libertad como para crear contenido único asociado al sitio web sin interferir. Esto significa que bajo la utilización de un gran framework será posible encontrar un montón de proyectos distintos y muy variados uno a otro. 
</div>

<div style="text-align:justify">
últimamente, los framework más populares y versátiles manejan una estructura Modelo-Vista-Controlador(MVC). En este patrón, el "Modelo" hace referencia al acceso a la capa de datos, la "Vista" se refiere a la parte del sistema que selecciona qué mostrar y cómo mostrarlo, y el "Controlador" implica la parte del sistema que decide qué vista usar, dependiendo de la entrada del usuario, accediendo al modelo si es necesario.
</div>

### Frameworks más populares

<div style="text-align:justify">
Hay una amplia gama de frameworks para aplicaciones web disponibles para Linux que son distribuidos bajo licencia Open Source. Entre ellos puede destacarse:
</div>

-  **Angular.js**  _Un framework basado en JavaScript_
-  **Ruby on Rails**  _Framework MVC basado en Ruby, orientado al desarrollo de aplicaciones web_
-  **CodeIgniter**  _Poderoso framework PHP liviano y rápido_
-  **Django** _Framework Python que promueve el desarrollo rápido y el diseño limpio_
-  **Pylons** _Framework web para Python que enfatiza la flexibilidad y el desarrollo rápido_
-  **CakePHP**  _Basado en PHP_
-  **Zend Framework** _Basado en PHP_
-  **Yii** _Basado en PHP_

### En realidad,¿Hace falta un framework?

<div style="text-align:justify">
Una respuesta sencilla sería sí, ya que este nos ahorra muchísimo trabajo y nos ayuda a optimizar nuestro tiempo efectivo, además que nos facilita las cosas al momento de escribir código. Además, si utilizamos un framework basado en un lenguaje de programación como Python encontraremos que podremos desarrollar aplicaciones elaboradas con pocos conocimientos de programación. Ya que es un lenguaje de programación sencillo, de alto nivel, fácil de entender en cuanto a código y además con muchas librerías y una comunidad muy grande. Por eso es muy importante analizar frameworks como Django.
</div> 

## ¿Por qué usar Django?

<div style="text-align:justify">
Django está centrado en el desarrollo rápido de aplicaciones web y sobre todo usando el principio de la programación DRY (No te repitas) y es algo importante en el core de este framework.
</div> 

![Logo_Django](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/dijango-logo.png)

<div style="text-align:justify">
Django se puede ejecutar en cualquier sistema operativo. Sólo es necesario instalar Python (Mac y Linux tienen python por defecto) y gracias al gestor de paquetes de python (PIP) instalarlo es tan sencillo como ejecutar este comando
</div> 

``pip install django``

### ¿Qué hace genial a Django?

- **Administrador**: Django cuenta con un administrador que viene activo por defecto donde se pueden con un par de líneas de código mostrar los modelos de las bases de datos y poder crear, editar, ver y eliminar registros.

- **Formularios**: Crear formularios en Django es muy sencillo y se pueden crear de dos formas, un formulario definiendo uno a uno los campos o usar un modelo de la base de datos y Django crea el formulario por nosotros.

- **Rutas**: El manejo de rutas hace que crear urls complejas sea sencillo de implementar, Django usa el poder de las expresiones regulares de python para hacer este trabajo.

- **Autenticación**: Django provee un sistema de autenticación que permite que no nos preocupemos por crear un flujo de login y registro.

- **Permisos**: En Django se tiene control de los permisos a tal punto de decir que usuario puede o no crear, editar, ver y eliminar registros de un modelo especifico.

- **Bases de Datos**: Como lo mencioné Django cuenta con un ORM que nos permite preocuparnos en la lógica de nuestra aplicación dejando al ORM la responsabilidad de la comunicación con la base de datos, es compatible con los principales motores de bases de datos como PostgreSQL, MySQL, Oracle, SQLServer entre otros.

- **Extensible**: Django puede ser extendido fácilmente instalando paquetes adicionales para crear aplicaciones una tienda, un blog o un API Restful, se encuentran agrupados y ordenados en Django Packages.

- **Comunidad**: Django tiene una gran comunidad que encuentras siempre en los foros de ayuda y listas de correos.

- **Documentación**: Django tiene una documentación muy completa que te enseña con ejemplos de código como implementar o usar cada una de sus características.

### ¿Cómo funciona?

<div style="text-align:justify">
Internamente, Django sigue el patrón MVC tan al pie de la letra que puede ser llamado un framework MVC. Donde, la M, V y C se separan en Django de la siguiente manera:
</div> 

- **M**, la porción de acceso a la base de datos, es manejada por la capa de la base de datos de Django.
- **V**, la porción que selecciona qué datos mostrar y cómo mostrarlos, es manejada por la vista y las plantillas.
- **C**, la porción que delega a la vista dependiendo de la entrada del usuario, es manejada por el framework mismo siguiendo la URLconf y llamando a la función apropiada de Python para la URL obtenida.

<div style="text-align:justify">
Debido a que la "C" es manejada por el mismo framework y la parte más importante se produce en los modelos, las plantillas y las vistas, Django es conocido como un Framework MTV. En el patrón de diseño MTV:
</div> 

- **M** significa "Model" (Modelo), la capa de acceso a la base de datos. Esta capa contiene toda la información sobre los datos: cómo acceder a estos, cómo validarlos, cuál es el comportamiento que tiene, y las relaciones entre los datos.
- **T** significa "Template" (Plantilla), la capa de presentación. Esta capa contiene las decisiones relacionadas a la presentación: como algunas cosas son mostradas sobre una página web o otro tipo de documento.
- **V** significa "View" (Vista), la capa de la lógica de negocios. Esta capa contiene la lógica que accede al modelo y la delega a la plantilla apropiada: Se puede pensar en esto como un puente entre los modelos y las plantillas.

Con esta estructura, Django se rige bajo el siguiente proceso:


1. El usuario hace una petición, a través de una dirección web (URL).
2. Django realiza una consulta para saber qué hacer con la petición.
3. Una vez que sabe qué tarea realizar le envía la petición a la vista que corresponde.
4. La vista realiza las acciones necesarias en la base de datos.
5. Si lo necesita también utiliza la definición de los formularios.
6. Para después responder a la petición mostrando la página que contiene esa URL.

![Funcionamiento_de_Django](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/funcionamiento-de-django.png)

## ¿Qué es un CMS?

<div style="text-align:justify">
Un CMS o Sistema de Gestión de Contenidos es un programa que le permite al usuario un fácil manejo de información para su página de Internet.
Es decir, es una herramienta que le da la facultad al usuario para crear, editar, publicar e incluso clasificar contenidos en su sitio web sin tener que estar lidiando con lenguajes complejos de programación.
</div>

<div style="text-align:justify">
El CMS gratuito suele ser desarrollado por una comunidad de programadores que voluntariamente mejoran y lanzan nuevas ediciones del software, por lo que el soporte técnico directo es difícil de encontrar. Para solucionar cualquier problema es más fácil buscar respuestas en foros de usuarios. Los tres proyectos de código abierto y con licencia gratuita más conocidos son WordPress, Joomla y Drupal.
</div>

<div style="text-align:justify">
La utilización de un CMS facilita la vida de muchos usuarios sin conocimientos técnicos para administrar contenidos, pero también puede suponer inconvenientes que es necesario conocer en profundidad antes de decidirte por uno de ellos.
A continuación, se expone un listado con las principales ventajas y desventajas a la hora de recurrir a un gestor de contenido
</div>

#### ¿Cuáles son las ventajas de usar un CMS?

* **El desarrollo de tu sitio web será más rápido.** No es lo mismo tener que implementar funcionalidades a mano que las tareas las realice automáticamente un CMS.
* **Facilidad de uso.** Muchos CMS actuales son muy fáciles de usar, por lo que no es necesario tener un amplio conocimiento en programación para poder crear, modificar o actualizar el contenido.
* **Personalización.** Los CMS te permiten personalizar el diseño web de tu página, así como individualizar las funcionalidades de la plataforma del gestor de contenidos. Así, se puede implementar rápidamente un calendario de eventos, un formulario o una encuesta, entre otros ejemplos, tres acciones que de otra manera te costarían bastante más trabajo si no cuentas con habilidades técnicas.
* **Escalabilidad.** Es decir, puedes añadir nuevas funcionalidades a tu sitio web en cualquier momento, ya sea a través de plugins o módulos.
* **Posicionamiento SEO.** Puedes posicionar tu sitio web en Google si cuentas con un gestor de contenidos “SEO friendly”, o lo que es lo mismo, que incluya herramientas de optimización de contenidos para mejorar tu posición en los motores de búsqueda.
* **Ahorro económico.** Es mucho más barato desarrollar un sitio web con un CMS que comenzar desde cero, además de que te ahorras la asistencia técnica si aprendes por ti mismo a solucionar los pequeños problemas que te vayas encontrando.
* **Seguridad.** El servidor de un CMS cuenta con actualizaciones constantes para evitar incidencias de seguridad que afecten a sus usuarios.

#### ¿Cuáles son las desventajas de usar un CMS?

* **Requiere mantenerlo siempre actualizado.** De lo contrario, su sitio web puede sufrir fallas de seguridad, ideales para los hackers. También puedes sufrir problemas de lentitud en tu sitio, de ahí la importancia de las actualizaciones.
* **Menos elasticidad.** Los CMS de código abierto suponen una estructura más o menos rígida, donde podemos hacer lo que queramos siempre que nos atengamos a la configuración propia de la plataforma.
* **Aprendizaje.** Los usuarios deben de aprender nociones mínimas para administrar su sitio web o de lo contrario requerirán pagar personal con experiencia para que el CMS esté perfectamente actualizado.
* **Costes adicionales.** Ya sea porque quieres mejorar el sitio comprando una plantilla muy original o porque necesitas incrementar funcionalidades que suponen un precio.

## ¿Por qué utilizar Django y no un CMS?

<div style="text-align:justify">
En primer lugar, son dos cosas distintas. Básicamente, WordPress es el tablero a través del cual organiza el texto y las imágenes para mostrar en su sitio web. WordPress está construido utilizando el lenguaje de programación PHP. Django, por otro lado, es lo que se llama un marco web. Basado en el potente lenguaje de programación Python, es un conjunto de herramientas y bibliotecas que se pueden implementar rápidamente para crear aplicaciones web personalizadas. 
¿Cuándo me serviría wordpress? Cuando desee crear un sitio web basado en una funcionalidad muy explotada y utilizada en el marco del desarrollo web, ya que es muy probable que dicha herramienta tenga incorporado temas y plugins necesarios para implementar en su sitio web. WordPress es una herramienta sencilla y económica para un sitio básico. Con una gran cantidad de temas gratuitos para descargar, es una forma rápida de conectarse y comenzar a promocionar su contenido / negocio / actividad secundaria. Sin embargo, para generar una página con una funcionalidad original y particular, que se adapte a las necesidades de la aplicación, estas herramientas (CMS) son menos flexibles, por lo que Django adquiere mucha importancia, proporcionando un marco flexible para implementar soluciones web personalizadas, escalables e innovadoras.
</div>

## Servicio a implementar
<div style="text-align:justify">Teniendo presentes la finalidad del trabajo y ya justificada la elección por Django, es que se plantea el siguiente proyecto compuesto por 3 etapas, tal como se ve a continuación:</div>

![Esquema_general_del_servicio](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Servicios_Esquema_general_proyecto.jpg)

<div style="text-align:justify">Esta aplicación, como se observa en la imagen tiene la finalidad de permitir a cualquier usuario que visite la página web y mediante una consulta poder visualizar información de datos meteorológicos que se encuentran disponibles en las bases de datos y que al mismo tiempo han sido cargados por los diversos sensores con que cuenta la red simulada. Con respecto al acceso a carga de datos al sistema, como se observa a la izquierda, cada uno de los sensores debe de pasar en primera instancia una etapa de registro y/o login para poder alojar su información en la base de datos.</div>

## Composición del Servicio Django
<div style="text-align:justify">Para comprender como es que funciona el servicio encargado de generar la página web, se debe analizar cómo se encuentra la carpeta asociada al servicio y que lleva el nombre de “appTrafico”, esta carpeta se puede encontrar dentro del repositorio en la dirección “/Versiones Finales/Proyecto_con_SQlite3/appTrafico” o también dentro de “/Versiones Finales/Proyecto_con_PostgreSQL/appTrafico”, su composición es:</div>

![Composicion_directorio_appTrafico](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Contenido_servicio.png)

<div style="text-align:justify">Para realizar una descripción de la composición de los componentes fundamentales del directorio, primero se debe de observar que al estar trabajando con un esquema dockerizado, se cuenta con un archivo “dockerfile”, este archivo además de contar con los distintos comandos para poner en funcionamiento Django, necesita de un documento el cual le indica los distintos programas que se necesitan instalar para el total funcionamiento de la aplicación, en este caso el archivo en cuestión es “requerimientos.txt”. Situado arriba de este archivo, se encuentra “manage.py”, este script sirve para ejecutar y administrar las herramientas de Django necesarias para este proyecto.
Después se cuenta con 4 carpetas, estas son:  ”templates” ,”static”, “registro” y  “config”.</div>
* **Templates:** <div style="text-align:justify">Es la carpeta que contiene los html básicos para la aplicación, en donde uno de sus archivos fundamentales, es “base.html”, este contiene gran mayoría de las etiquetas html y que serán heredadas por los distintos html que utilicemos para las ventanas de la página web. Se podría interpretar que es el encargado de dar el esqueleto, donde luego cada pestaña sobre esta configuración básica, agregara el aspecto que sea requerido.</div>

![Composicion_directorio_appTrafico/templates](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Contenido_servicio_templates.png)



* **Static:** <div style="text-align:justify">Es el directorio encargado de contener los archivos estáticos, como son por ejemplo las imágenes o iconos que se utilizan en la página web o graficas que son generadas por el servicio y es el directorio de almacenamiento para este contenido</div>
* **Registro:** <div style="text-align:justify">Es el nombre que se le designo a la aplicación de Django. Que dentro contiene todos los archivos “.py” y “.html” asociados al comportamiento y para la visualización de la aplicación. Su contenido es el siguiente:</div>


![Composicion_directorio_appTrafico/registro](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Contenido_servicio_registro.png)


<div style="text-align:justify">Dentro de la carpeta “templates” es que se encuentran todos los archivos “.html”, luego están todos los scripts necesarios para el funcionamiento de la api. 
“admin.py” contiene los modelos que se definirán en el proyecto, para este caso se han definido dos, los cuales son “sensor” y “sensor_dato”. El primero contiene los datos del sensor registrado y “sensor_dato” tiene los datos, asociados al clima y ubicación, que han cargado cada uno de los sensores y que serán los datos que se entregarán ante las distintas consultas de los usuarios que accedan a la aplicación. Estos modelos se encuentran descriptos en “models.py” en donde se define los campos que solicita cada uno de ellos para realizar un correcto registro del modelo.
“views.py” contiene la lógica de la navegación por la aplicación, asociada a las url en “urls.py” definidas. Para esta implementación se han definido 4 urls, los cuales tienen asociados distintos formularios, según los requerimientos y definidos en “forms.py”. Como así también se direccionará hacia los distintos “.html” ubicados en “/templates” que tiene vinculada cada url. </div>

* **Config:** <div style="text-align:justify">Es la última carpeta y contiene todas las configuraciones asociadas al sitio web. Su composición es:
</div>

![Composicion_directorio_appTrafico/Config](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Contenido_servicio_config.png)

<div style="text-align:justify">El script “settings.py” tiene todas las configuraciones necesarias del sitio, por lo que es donde se registra todas las aplicaciones que se crean, la localización de los ficheros estáticos, los detalles de configuración de la base de datos, etc.
“urls.py” define los mapeos url-vistas. A pesar de que éste podría contener todo el código del mapeo url, es más común repartir parte del mapeo a las propias aplicaciones, como sucedió en “/registro”.
“wsgi.py” y “asgi.py” se utilizan para ayudar a la aplicación Django a comunicarse con el servidor web.
De todos estos scripts, el más importante a describir es “settings.py”, en el cual algunas de las configuraciones más importantes son:</div>
- **BASE_DIR:** <div style="text-align:justify">Es la variable que tiene como contenido la ruta a una determinada ubicación del proyecto, en este caso esta direccionado hacia la ubicación del settings.py</div>
- **SECRET_KEY:** <div style="text-align:justify">Es la contraseña asociada con el proyecto Django</div>
- **DEBUG:** <div style="text-align:justify">Es una variable booleana, que debe configurarse en True mientras el proyecto esté en desarrollo, para poder ver los posibles errores por parte de Django. En caso de llevar el proyecto a producción, el estado de esta variable debe configurarse en False.</div>
- **ALLOWED_HOSTS:** <div style="text-align:justify">Asigna los host que pueden acceder al proyecto, esta variable debe de estar bien configurada para poder hacer acceso a la aplicación desde otros host </div>
- **INSTALLED_APPS:** <div style="text-align:justify">Es en donde se establecen las aplicaciones propias y de terceros que se van a utilizar, como es el caso del debug implementado para Django o la recolección de métricas hacia InfluxDB</div>
- **MIDDLEWARE:** <div style="text-align:justify">Es un sub framework que permite modificaciones al sistema de procesamiento de request/response de Django, en donde cada componente middleware es responsable de hacer alguna función específica y suele estar acompañado con las aplicaciones que se agregan en “INSTALLED_APPS”</div> 
- **TEMPLATES:** <div style="text-align:justify">Se describe al proyecto en donde debe de buscar las plantillas para implementar en la aplicación</div>
- **DATABASES:** <div style="text-align:justify">Es la variable de configuración asociada a la base de datos a implementar, en este caso en particular se podrá ver configurado SQlite 3 o PostgreSQL según sea el caso.</div>
- **DEBUG_TOOLBAR_PANELS:** <div style="text-align:justify">Son las configuraciones para los distintos datos que nos entregara el debug añadido como aplicación en “INSTALLED_APPS” y que se visualizaran al navegar por la página web</div>
- **INFLUXDB_:** <div style="text-align:justify">Son las distintas configuraciones necesarias para que las métricas obtenidas en Django sean llevadas hacia InfluxDB, nuevamente estas configuraciones están asociadas con la aplicación añadida en “INSTALLED_APPS”
</div>

## Navegación por el servicio Django

<div style="text-align:justify">Para poder entender la navegación dentro de la aplicación, es que se presenta un diagrama de flujo el cual contiene todas las pestanas asociadas a la página web y que dan sentido a la implementación de todas las configuraciones antes mencionadas. Para comprender el funcionamiento de la navegación es que se debe tener presente que la aplicación podrá ser consultada por 2 grupos diferenciados, siendo estos Sensores y Usuarios, los cuales experimentaran una navegación diferente. Una vez mencionado este detalle, el diagrama de flujo es:</div>

![Diagrama_de_flujo_servicio_Django](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/DiagramadeFlujo_pagina.png)

<div style="text-align:justify">Para acceder a la pagina web se debe ingresar la dirección: http://127.0.0.1:8010 o http://172.2x.0.2:8010 en el caso de estar accediendo desde el mismo host, en caso de acceder de manera externa, se debe de acceder mediante el ip que tiene asignado el host que contiene el servicio y redireccionar hacia el puerto 8010, tal como se hizo en las dos direcciones anteriores. Una vez que se ha accedido a la página se podrá ver un panel superior desplegable, el cual nos puede llevar a el mismo home en el cual nos encontramos, a realizar un registro de un nuevo sensor o una carga de datos por parte de los sensores.</div>
<div style="text-align:justify">En la parte central de la página están los botones asociados a “iniciar sesión” o “consultar datos” es en esta instancia que la navegación por la página web bifurca según sea el caso de un sensor que inicie sesión o un usuario que consulte datos climatológicos. Considerando el caso de este último, se lo llevará hacia una nueva url asociada a “/registro/procUser” en donde el usuario mediante el correcto llenado de un formulario que solicita la ubicación y características climatológicas, podrá visualizar los datos solicitados a la base de datos y, si así lo desea, realizar nuevas consultas mediante la variación en el formulario antes comentado.</div>
<div style="text-align:justify">Con respecto a los sensores y en la otra rama de navegación, estos deberán iniciar sesión en donde serán llevados a “/accounts/login”, si se diera el caso de que el sensor no este registrado, debe de ingresar a “/registro/nuevo” para un posterior login. Una vez que el sensor ha iniciado sesión correctamente, es que podrá acceder a “/registro/privado” para poder cargar los datos asociados a su ubicación geográfica y los datos climatológicos obtenidos, estos datos serán cargados mediante un formulario, que en el caso de estar ingresados de manera correcta serán registrados en la base de datos. Luego el sensor podrá ver sus últimos registros cargados visualizándose mediante una tabla y distintas gráficas. 
</div>


## Fuente de Informacion 

* https://openwebinars.net/blog/que-es-django-y-por-que-usarlo/

* https://devcode.la/blog/por-que-usar-django/

* https://www.azulschool.net/que-es-django-y-para-que-sirve/

* https://platzi.com/blog/django-el-framework-para-desarrollo-web/

* https://codingornot.com/django-por-que-usar-django

* https://www.djangosites.org/

* https://djangopackages.org/

* https://www.opensourcecms.com/

* https://www.comparahosting.com/que-es-un-cms-y-para-que-sirve/

* https://elbauldelprogramador.com/los-10-mejores-frameworks-gratis-de-aplicaciones-web/

* https://www.django-cms.org/en/why-django-cms/

* https://uniwebsidad.com/libros/django-1-0/capitulo-5/el-patron-de-diseno-mtv

* https://medium.com/infeenix/django-vs-wordpress-c%C3%B3mo-me-decido-97442a76c8d2



