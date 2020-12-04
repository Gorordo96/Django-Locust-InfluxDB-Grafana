# Pruebas de Performance

## ¿Que es una prueba de performance?

<div style="text-align:justify">Un performance test o prueba de rendimiento apunta a indagar sobre el comportamiento de una aplicación cuando se genera una alta demanda de uso. Es una situación muy común en aplicaciones corporativas, en soluciones de e-commerce, servicios en línea para la oferta de productos en fechas especiales, asi como tambien en arquitecturas de redes correspondientes a sistemas IoT. </div><br><br>
<div style="text-align:justify">En definitiva,<em>el performance test</em> consiste en someter una aplicación a distintas pruebas para determinar su comportamiento en circunstancias de carga extrema de trabajo.</div><br><br>
<div style="text-align:justify">El objetivo principal es determinar si la aplicación se comporta como se espera, principalmente cuando el volumen de trabajo es grande. No opera sobre posibles errores en la aplicación específicamente. Lo que busca es determinar el desempeño general del sistema y detectar cuellos de botella que puedan desestabilizar la aplicación y afectar la buena experiencia del usuario.<br><br>Durante el performance test se toman en cuenta diferentes indicadores como: <strong>nivel de respuesta, velocidad, escalabilidad y estabilidad, recursos consumidos, entre otros.</strong><br><br>Para llevar a cabo un test de esta naturaleza, se simula de la manera más realista posible la aplicación, y se ejecuta de distintas maneras y en diferentes situaciones de uso. Por ejemplo, es ideal para determinar el comportamiento de una aplicación cuando ingresan en forma simultánea varios, cientos, miles de usuarios. Permite medir su rendimiento cuando se ejecutan algunas operaciones. Al finalizar las pruebas, se analizan todos los datos generados evaluando el desempeño general de la aplicación. En caso de encontrar anomalías comienza un profundo trabajo de investigación para detectar los problemas del sistema. Puede tratarse de aspectos referidos a la aplicación misma, el software de soporte como Bases de Datos, el sistema operativo, fallas en el hardware, como el servidor, servidores redundantes o la infraestructura de la red. </div>

## Distintos tipos de performance test

<div style="text-align:justify">Un performance test implica realizar varios tipos de pruebas específicas para conocer el comportamiento en distintas situaciones. Alguna de estas pruebas se describe a continuación.<br><br><strong>Test de carga</strong>, en ese caso la carga de la aplicación se va incrementando progresivamente hasta cierto punto. Por ejemplo, se van incrementando la cantidad de usuarios que utilizan la aplicación o la cantidad de transacciones que se realizan simultáneamente.
<br><br><strong>Test de Stress</strong>, se prueba la estabilidad del sistema cuando los recursos de hardware son insuficientes como la CPU, memoria o el espacio en disco duro.
<br><br><strong>Test de volumen</strong>, en este caso se somete a la aplicación a grandes volúmenes de datos a procesar para validar la eficiencia y probar así el desempeño de la Base de Datos.</div>

## Pruebas de performance de nuestro Proyecto

<div style="text-align:justify">La finalidad de toda la arquitectura de red detallada en este trabajo, consiste en servir como banco de prueba para realizar test de performance sobre diferentes aplicaciones web. En esta instancia toco django, pero podria desplegarse cualquier otra tecnologia de servicios web para realizar pruebas.</div>

![Imagen_Banco_de_Prueba](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Banco_De_Prueba_Imagen_1.png)

<div style="text-align:justify">Como en este caso se plantea una aplicacion para IoT, las pruebas de performance estaran destinadas a:</div>

<div style="text-align:justify">
<ul>

<li type="circle">Determinar la cantidad maxima de usuarios simultaneos soportados por el sistema.</li>

<li type="circle">Determinar la cantidad maxima de usuarios por segundo Iniciales que soporta el sistema.</li>

<li type="circle">Determinar el consumo de recursos (CPU y Memoria RAM) para diferentes modelos de trafico.</li>

<li type="circle">Determinar si el sistema es estable o permanecera estable para cada uno de los escenarios.</li>

<li type="circle">Gestionar diferentes pruebas para diferentes hardware (PC Escritorio y Notebook) y comparar resultados. </li>

<li type="circle">Determinar la importancia de los parametros del sistema en el rendimiento de las diferentes pruebas</li>

<li type="circle">Determinar las diferencias que existen entre diferentes bases de datos (SQLite3 y PostgreSQL) en cuestiones de rendimiento.</li>

</ul>

</div>

<div style="text-align:justify">Para ello, se realizaron tres modelos de trafico que ejecutaran diferentes pruebas, considerando que el recurso destinado a RAM ira desde 4GB a 11GB y la cantidad de CPU desde 2 CPU a 4 CPU. Cada modelo de trafico esta rotulado como : <em>Trafico Pesado</em>, <em>Trafico Intermedio</em> y <em>Trafico Liviano</em> dependiendo de las caracteristicas de los sensores.<br><br>
El trafico denominado como <strong>pesado</strong> tiene las siguientes caracteristicas: </div>

<div style="text-align:justify">

<ul>

<li type="circle">Tiempo entre tareas asociadas a un mismo sensor : <strong>15 min</strong> </li>

<li type="circle">Tiempo entre tareas asociadas a un usuario: <strong>2 a 6 min</strong></li>

</ul>

</div>

![Trafico_Pesado](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/PruebasPerformance_prueba_Pesada.png)

<div style="text-align:justify">El <strong>trafico intermedio</strong> se caracteriza por los siguientes parametros:</div>

<div style="text-align:justify">

<ul>

<li type="circle">Tiempo entre tareas asociadas a un mismo sensor: <strong>30 min</strong></li>

<li type="circle">Tiempo entre tareas asociadas a un usuario: <strong>4 a 12 min</strong></li>

</ul>

</div>

![Trafico_Intermedio](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/PruebasPerformance_prueba_Intermedia.png)

<div style="text-align:justify">En ultima instancia, el <strong>trafico liviano</strong> se caracteriza por los siguientes parametros:</div>

<div style="text-align:justify">

<ul>

<li type="circle">Tiempo entre tareas asociadas a un mismo sensor: <strong>60 min</strong></li>

<li type="circle">Tiempo entre tareas asociadas a un usuario: <strong>10 a 15 min</strong></li>

</ul>

</div>

![Trafico_Liviano](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/PruebasPerformance_prueba_liviana.png)

<div style="text-align:justify">Todas los modelos comparten ciertas caracteristicas en comun:</div>

<div style="text-align:justify">

<ul>

<li type="circle">Probabilidad de Ocurrencia de un sensor <strong> 1/3 </strong></li>

<li type="circle">Probabilidad de Ocurrencia de un consumidor <strong> 2/3 </strong></li>

<li type="circle">Cada modelo sera puesto a prueba con una cantidad de usuarios de <em>300-600-900</em></li>

<li type="circle">La combinacion entre modelo y cantidad de usuarios, permite generar un set de <strong>lambda</strong><em>(Cantidad de usuarios por segundo que se hacen presentes en el sitio web de forma simultanea)</em> donde el valor minimo en todos los casos sera <strong>1</strong> y el valor maximo <strong>25%</strong> de la cantidad maxima de usuarios.</li>

<li type="circle">Estas combinaciones (Modelo-Cantidad de usuarios - Lambda) se encuadran dentro de las diferentes categorias de acuerdo a la cantidad de recursos con los que cuenta el servidor. Se crearon 3 categorias: <strong>2 CPU - 4 GB RAM</strong><em>(recursos bajos)</em>,<strong>2 CPU - 6 GB RAM</strong><em>(recursos intermedios)</em>,<strong>4 CPU - 11 GB RAM</strong><em>(recursos altos)</em> </li>

</ul>

</div>

<div style="text-align:justify">De esta forma, es posible generar un total de 27 pruebas de performance por cada combinacion de recurso que sea asignado al servidor. Como se realizaran 3 combinaciones diferentes, habria en total una cantidad de 81 pruebas diferentes. A continuacion, se muestra una imagen que resume los puntos tratados anteriormente:</div>

![Imagen_Pruebas_de_performance](https://gitlab.com/unrc/trafico/tabajos-finales/lucas_gorordo-ger-nimo_passini-2020/desarrollo/-/raw/master/docs/Img/Imagen_representacion_Pruebas.png)

## Resultados

<div style="text-align:justify">Antes de presentar los resultados es necesario mencionar que todo el set de pruebas fue elaborado entre dos maquinas Host diferentes. Cada una de ellas, efectuo aquellas pruebas de performance que fueran adecuadas respecto a sus recursos, ya que no tienen la misma cantidad de memoria RAM, ni los mismos procesadores y por sobre todas las cosas, difieren en tamaño, ya que estamos frente a una maquina de escritorio y una notebook, por lo que es un detalle a no perder de vista. </div><br>
<div style="text-align:justify">Las caracteristicas tecnicas de la PC de escritorio son:<br>
<ul>
<li type="circle"><strong>Procesador: </strong><em>AMD FX(tm)-4300 Quad Core Processor 3,80 Ghz</em></li>
<li type="circle"><strong>Memoria RAM: </strong><em>8 GB</em></li>
</ul>

</div><br>
<div style="text-align:justify">Las caracteristicas tecnicas de la Notebook son:<br>
<ul>
<li type="circle"><strong>Procesador:  </strong><em>Intel Core i7 – 7700HQ CPU a 2.8Ghz</em></li>
<li type="circle"><strong>Memoria RAM: </strong><em>16 GB </em></li>
</ul>
</div>
<br><br><br>
<figure class="video_container">
<iframe width="560" height="315" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRlZcWHTs_ZivihAtkyK8wZznov--nhw_tO1OhcxvPLr8CsUGe3y_gw6vDskIRzDplK02uRp_fWNzdP/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false"></iframe>
</figure>
<br><br><br>
<div style="text-align:justify">Los resultados dejan en evidencia rápidamente que independientemente del modelo de tráfico aplicado, el funcionamiento del sitio web es óptimo para 300 usuarios. Esto quedó totalmente demostrado al realizar y superar las pruebas de performance más críticas dentro de todo el set. Lo que significa que se utilizó la menor cantidad de CPU, la menor cantidad de memoria RAM y el modelado más exigente (tráfico pesado) y aun así el servidor fue capaz de responder a cada consulta en tiempo y forma y optimizar el uso de recursos.<br><br>
¿Qué significa responder en tiempo y forma? Que el servidor logró dos cuestiones fundamentales en cuanto a la carga de datos y consulta de los mismos:<br><br>
<ul>
<li style="circle">Las respuestas a las diferentes cargas iniciales tardaron menos de 15 min. por lo tanto los sensores pudieron generar su flujo de información periódica sin ningún compromiso. El sistema soporto el pico de tráfico inicial y supo responder frente a ello.</li> 
<li style="circle">Las consultas para observar datos a pesar de generarse cada 2 a 4 min. no superaron el periodo de 15 min en cuanto al tiempo de respuesta, lo que significa que quien realizaba las consultas pudo observar correctamente los datos en su momento y actualizados.</li>
</ul><br><br>
Es notable la dificultad que presenta el sistema frente a las escrituras sobre la base de datos, ya que cuando existen cargas de sensores los tiempos de respuesta se disparan y generan picos, lo que significa que todo el sistema se vuelve más lento. Además, depende del gestor de base de datos utilizado para la aplicación. En el caso de SQLite3 existen grandes problemas de concurrencia, que pueden observarse en las pruebas de performance con 38 usuarios/seg y 75 usuarios/seg, lo que genera una gran cantidad de bloqueos (errores 500 server) y demoras para resolver las diferentes solicitudes de escritura sobre la base de datos. Distinto de lo que ocurre al aplicar PostgreSQL. Con este último, las conexiones activas aumentan pero sobreviven al bloqueo, lo que da mayor probabilidad de éxito a una consulta aunque los tiempos de respuesta aumentan. Es necesario mencionar que es posible configurar la cantidad máxima de conexiones simultáneas, lo que significa un cambio importante y fundamental entre SQLite3 y postgreSQL. Sin embargo, si se decide mantener un número pequeño de conexiones activas simultáneas, el sistema funciona de forma eficiente de todos modos, ya que cuando la base de datos está colapsada de solicitudes, rechaza rápidamente las nuevas solicitudes entrantes y no pierde tiempo tratando de resolverlas a diferencia de SQLite3 que si espera y da oportunidades a todas las solicitudes.<br><br>
Las lecturas sobre la base de datos parecen ser más sencillas de resolver para el sistema, ya que a pesar de ser la mayor masa de tráfico, pueden observarse tiempos de respuesta muy buenos una vez superada la carga inicial.<br><br>
¿Qué ocurre con el consumo de recursos? Respecto al consumo de CPU parecería ser un enigma, ya que se esperaría que mientras mayor es el nivel de concurrencia, mayor trabajo por parte del hardware y niveles máximos de CPU cada vez más grandes. Pero esto no es necesariamente así, ya que simulación a simulación los comportamientos tienden a ser variables y no siempre muestran una clara tendencia. Respecto al consumo de RAM puede verse una clara diferencia entre simulaciones con y sin concurrencia. Para aquellas pruebas donde la concurrencia es alta, si el sistema soporta la carga de tráfico, presenta una curva de consumo de RAM muy particular. Primero crece rápidamente hasta alcanzar un máximo y luego decrece rápidamente para establecerse en un valor constante. Si el sistema presenta poca concurrencia, la curva de consumo de ram parece escalonada en muchos casos o una exponencial positiva de crecimiento lento tendiendo a un valor máximo fijo. En aquellos casos donde el sistema no soporta la carga de tráfico, consume toda la RAM y genera microcortes muy marcados o cortes totales en el funcionamiento hasta dejar al servidor fuera de servicio. Estas son algunas de las características de las simulaciones de tráfico pesado con 300 usuarios. <br><br>
Respecto a las simulaciones de 600 usuarios, los resultados mostraron un claro comportamiento. En el caso de tráfico pesado, el sistema no funciona para ningún caso diferente al de 1 usuario/seg (sin concurrencia)  de los planteados. Lo que genera una gran sospecha, ya que cuando se observan los tiempos de respuesta y comportamientos para la prueba que si funciona, el sistema es muy estable. El agotamiento de RAM lleva a que el servidor sea cada vez más lento o directamente se paralice, lo que genera que el tráfico pendiente se le acumule cada vez más y los tiempos de respuesta se disparen. Esta situación no tendría solución alguna, ya que si el servidor no es capaz de responder más rápido, la situación de colapso por RAM no es posible de evitar. 
Si se sigue aumentando la cantidad de usuarios en este modelo de tráfico, los resultados son desalentadores. El sistema no soporta ninguna de las pruebas. En poco tiempo iniciada la simulación se agota la memoria RAM por lo que el servidor colapsa.
<br><br>
Al migrar el modelo de tráfico a una carga intermedia, el único logro fue incorporar como pruebas exitosas a las de 900 usuarios con una concurrencia de 1 usuario /seg. Sin embargo, el resto de pruebas que fallaron en el modelo de tráfico pesado, fallaron nuevamente en este modelo.<br><br> 
Finalmente, al incorporar al análisis el modelo de tráfico liviano, puede observarse la notable mejora en las pruebas de rendimiento para 600 usuarios con concurrencias desde 75 usuarios/seg a 150 usuarios/seg a partir de un nivel mínimo de recursos (2 CPU y 6 GB RAM), dando la pauta que cuando el modelo de tráfico es más relajado, la cantidad de usuarios simultánea y la concurrencia pueden ser mucho más elevadas.<br><br>
Sin embargo, en este modelo las pruebas de 900 usuarios con concurrencia fallaron nuevamente, lo que nos dice que bajo cualquier modelo, las pruebas de 900 usuarios representa un límite superior muy marcado para las prestaciones y servicios/contenedores implementados. A pesar de esto, los 600 usuarios simultáneos es un factor posible de alcanzar dependiendo el nivel de tráfico y los 300 usuarios representa el uso real que puede soportar este esquema.<br><br>
En caso de querer observar particularidades de las diversas pruebas, se puede acceder a los siguientes documentos:</div>
- [Pruebas Livianas](https://docs.google.com/document/d/1054xHaCpdEkEvL91FSPpw_0ZYvjk-pJ-aFr2WkFHxiw/ "Pruebas Livianas")

- [Pruebas Intermedias](https://docs.google.com/document/d/1RAyYIkGaa-I_qs1cL9wrTSl26cfH0Rj6sdGBFuIQwhA/ "Pruebas Intermedias")

- [Pruebas Pesadas](https://docs.google.com/document/d/1ANx6QmoHKnll6V4i3bxyuKNAwHI_Pw_Ra--VDwgjp7w/ "Pruebas Pesadas") 
