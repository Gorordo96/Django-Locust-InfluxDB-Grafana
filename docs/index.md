# Documentación Trabajo Final de Tráfico

<div style="text-align:justify">La siguiente documentación tiene como propósito exponer los conceptos que dan origen y sustento al trabajo final de Gerónimo Passini y Lucas Gorordo para la asignatura "Tráfico" de la carrera ingeniería de Telecomunicaciones.
</div> 

## ¿En qué se basa el proyecto?
<div style="text-align:justify">Antes de comenzar a dar detalles del proyecto, es importante tener en cuenta el concepto de Internet de las Cosas o también conocido como IoT, este se refiere a un gran número de “cosas” u objetos que se conectan a Internet para que puedan compartir datos con otras cosas – aplicaciones para IoT, dispositivos conectados, máquinas industriales y más. Los dispositivos conectados a Internet utilizan sensores integrados para reunir datos y, en algunos casos, realizar acciones con ellos. Los dispositivos y máquinas conectados a Internet pueden mejorar nuestra forma de trabajar y de vivir. Algunos ejemplos reales de IoT van desde un hogar inteligente que ajusta automáticamente la calefacción y las luces hasta una fábrica inteligente que monitorea máquinas industriales para buscar problemas y luego hace ajustes automáticos para evitar fallos.
Los sistemas embebidos en este contexto son muy importantes, siempre y cuando estén muy bien acompañados con una infraestructura de red que permita dar soporte a cientos de sensores y construir una aplicación destinada al usuario final. En este sentido, es muy importante analizar el comportamiento de redes de sensores para una aplicación en particular, en la que la cantidad de dispositivos inteligentes y su comportamiento juegan un rol fundamental.
El presente trabajo tiene como finalidad poder crear un entorno de simulación orientado a esquematizar una implementación típica, como suele suceder en el área de los sistemas embebidos, en búsqueda de poder realizar análisis de tráfico en la etapa posterior a que ya se encuentre estable la etapa de adquisición de datos por los diversos sensores o periféricos que componen al proyecto. </div> 
![Esquema_IoT](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/IoT.png)

## Estructura del proyecto
 Todo el material expuesto en esta instancia, ronda a partir de la siguiente estructura:

* Servicio a implementar
* Generador de trafico 
* Adquisición de métricas
* Visualización de métricas

La misma pretende ser implementada en Docker para crear un _esquema de trabajo portable_ sobre el cual realizar **pruebas de performance**.

## Docker como estructura de trabajo

<div style="text-align:justify">Dada la estructura del trabajo a realizar, la tecnología que mejor se adapta a la modalidad de desarrollo es Docker ¿Por qué? porque permite tener control sobre cada una de las fases de vida de un producto. Una aplicación incluye no solo la aplicación como tal, sino que tenemos un motor, un conjunto de librerías y el kernel o software. Docker permite agrupar todo esto en un contenedor y almacenarlo en nuestro disco duro. De forma que copia todo lo que pertenece a un mismo sistema operativo y lo almacena en una zona de nuestro disco duro para luego ejecutarla independientemente del sistema operativo. Esto permite que se pueda transportar la aplicación y ejecutarla donde se desee, sin preocuparse por el software o si tienes todos los componentes de la aplicación para iniciarla. La portabilidad es la gran característica que permite una evolución continua y rápida en el desarrollo de un programa y es precisamente lo que se necesita en este momento para la realización de trabajos grupales de manera remota.</div> A nivel general, _¿Qué ventajas adicionales aporta esta tecnología al desarrollo de software?_ 

→  Facilita el testing, facilita la tarea, puesto que si tenemos instalado Docker en nuestro ordenador y nos pasan un contenedor con una App a testear. Da igual cual sea el software que tengamos, docker nos permitirá abrir la app y poder probarla.

→  Ahorra tiempo, al no obligarnos a instalar diferentes softwares para poder ejecutar una App.

→  Es muy sencillo crear y eliminar contenedores.

→  Son muy ligeros, lo que nos permite manejar diferentes contenedores dentro de una misma máquina.

→  Es open source.

→  Nos proporcionan autonomía, a partir de que en cada contenedor tenemos todo lo necesario para ejecutar una aplicación.

→  Portabilidad: Al almacenar los contenedores en discos duros, estos se pueden transportar de un lugar a otro sin problemas.

→  Imágenes Docker: Podríamos definir estas imágenes como sistemas operativos con aplicaciones instaladas. En este SO, podremos incluir nuestras imágenes para su posterior visualización en un equipo.

→  Repositorios Docker: “Banco de imágenes docker” creadas por usuarios a las cuales podemos tener acceso.

→  Con Docker, tenemos capacidad de ejecutar prácticamente todas las aplicaciones facilitando el compartir las aplicaciones a través de los contenedores.

→  Se acelera el proceso de mantenimiento y desarrollo gracias a las facilidades para generar copias.

→  Las aplicaciones se ejecutan sin variaciones. Sin importar el equipo ni el ambiente.

→  Es un entorno seguro y no ofrece variaciones.

### ¿Qué sistemas operativos admiten docker?

<div style="text-align:justify">Docker puede instalarse tanto en Linux como en Windows, pero es necesario agregar algunas particularidades al análisis. Con respecto a el mundo de Linux, Docker es una plataforma de código abierto (en su mayoría) que funciona con cualquier distribución de Linux de cualquier proveedor. En sus inicios, Docker no trabajó en estrecha colaboración con ninguna empresa en particular en el espacio de Linux para desarrollar contenedores o hacer que funcionen con Linux. Pero no ocurre lo mismo con Windows, para este caso, Docker y Microsoft trabajaron en estrecha colaboración para llevar contenedores a Windows. Esta diferencia puede ser importante para el usuario si se piensa en la longevidad o flexibilidad de los contenedores en Windows. Ya que, si Microsoft decidiera en el futuro dejar de admitir contenedores, probablemente será el final de los contenedores en Windows.
En Linux, estos riesgos no existen. Incluso si Docker decidiera detener el desarrollo, el ecosistema de contenedores ahora es tan dinámico y grande que otros proyectos de código abierto probablemente tomarían el relevo y garantizarían que los contenedores de Linux sigan siendo viables.
Para decirlo de otra manera: Se podrá utilizar contenedores en Windows dentro de 10 años depende en gran medida de lo que Microsoft decida hacer. En Linux, es una apuesta mucho más segura que los contenedores seguirán funcionando en una década, independientemente de las elecciones que tome un proveedor en particular. 
Pese a esta independencia entre Linux y Docker, hay que destacar que la arquitectura de Docker es muy eficiente dentro de un sistema operativo Linux. ¿Pero qué ocurre con Windows?
El primer enfoque para admitir Docker en Windows fue Docker Toolbox, que es básicamente una máquina virtual que utiliza Virtual Box con una imagen de Linux. Entonces, como sugiere el nombre, es solo una herramienta para aprender Docker, pero no es muy útil ya que es una VM normal.
Con Windows 10 Pro, Microsoft presentó Hyper-V, que es una herramienta de virtualización súper rápida, Docker para Windows se lanzó para Windows 10 Pro, para ejecutar contenedores mucho más rápido y más fácil, pero en un principio se necesitaba Windows 10 “Pro”, por lo que en “Home” no funcionaba. 
Cuando se lanzó Windows Server 2016, fue una nueva arquitectura para admitir una especie de proceso aislado, de modo que pueda ejecutar Docker de forma nativa sin Hyper-V ni ninguna virtualización. A día de hoy, Windows Server 2016 es el único sistema de Windows que admite contenedores nativos, sin embargo, la imagen más básica es de 5 GB, lo que no es muy eficiente. El servidor de Windows ejecuta contenedores de Windows de forma nativa y usa Hyper-V para Linux. Además, cuando ejecuta contenedores de Windows, no puede ejecutar los de Linux, por lo que debe elegir uno u otro. Dado que el 99% de las imágenes están basadas en Linux y .NET puede ejecutarse en Linux, los contenedores de Windows no son tan útiles.
Sin embargo, actualmente Windows 10 Home es compatible con Docker. Utilizando WLS 2, que bajo el capó es una máquina virtual, muy similar a Docker Toolbox pero mucho más eficiente. Nuevamente, para el desarrollo local debería estar bien, pero Linux será el sistema operativo que ejecutará el Docker de forma óptima.
En síntesis, muchos portales web sugieren la implementación de dicha tecnología en un sistema operativo Linux. ¿Qué ocurre con aquellas personas que no tienen sistema operativo Linux de forma nativa? Una solución podría ser recurrir a la virtualización mediante máquinas virtuales de Virtual Box.</div>

_¿Funciona Docker en la implementación de una virtualización?_

<div style="text-align:justify">Si la máquina virtual es Linux, puede hacer esto sin ningún problema; en Linux, el Docker es esencialmente un chroot bien trabajado. Por lo tanto, la ventana acoplable de Linux no es virtualización.
En el caso de Windows, no es tan fácil. El sistema operativo Windows utiliza Hyper-V internamente para emular los contenedores. Lo que significa que solo puede ejecutar, si puede utilizar la virtualización anidada. Lo que finalmente permite deducir que tampoco es posible implementar docker en un entorno virtualizado de Windows.
En definitiva, la solución para implementar esta tecnología pasa por instalar docker en un Linux nativo o virtualizado. Siempre y cuando la virtualización tenga todas las configuraciones óptimas de virtualbox como plantea el tutorial presentado por Grzegorz Gajos en el portal de Medium. 
</div> 
**Conclusión**, como ambos estudiantes poseen windows de forma nativa se **recurrirá a una virtualización de Ubuntu Bionic 18.04 sobre virtualbox para implementar Docker**.


### Fuente de Información

* https://containerjournal.com/topics/container-ecosystems/the-differences-between-linux-and-windows-containers/
* https://apiumhub.com/es/tech-blog-barcelona/usar-docker/
* https://www.toolboxtve.com/es/por-que-usar-docker-cuando-la-infraestructura-se-vuelve-codigo/
* https://medium.com/@javier.ramos1/docker-windows-vs-linux-1bb26d8090b3
* https://stackoverrun.com/es/q/10941362
* https://medium.com/faun/hey-docker-why-you-hate-windows-so-much-de7a7aa4dd7



