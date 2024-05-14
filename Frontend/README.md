**Descripción**

Contiene todos los elementos gráficos del sistema gestor de base de datos jalisco, las bibliotecas empleadas para la confección de la **GUI** es **customTkinter** en conjunto de **Pillow** para la representación de las imágenes, la primordial diferencia respecto a la librería por defecto **Tkinter** es la expansión y la admisión de una mayor gama de frames como scrolls verticales, horizontales, los inputs pueden tener placeholders,  etc, además de permitir una mayor personalización, para mostrar las tablas fue contemplado una librería extra “**CTkTable**”.

La GUI esta contemplada para adaptarse a dispositivos con diferentes resoluciones, además de permitir redimensionar la pantalla al gusto del usuario.


**Funcionamiento**

**1.-** Es inicializada la pantalla de carga junto con todas las variables contenedores de las dimensiones de mis contenedores que dividen el display de la ventana, así como la paleta de colores empleada, es verificado si el usuario se encuentra logeado con el objetivo de evitar redundancia.

**1.1.-** Para crear la ilusión de la pantalla de carga es dividido el tamaño de mi screen en 2 elementos, el primero importa una imagen y la escala manteniendo sus proporciones, el segundo elemento hace uso de un **CTKProgressBar** donde es posible indicarle el color, la tasa y la velocidad de progreso.

**1.2.-** La progress bar tiene dos posibles configuraciones donde se puede establecer un tamaño definido, donde al completarse reiniciara de nuevo, la subsecuente configuración tornara la carga de un lado a otro, susceptible de ser usado cuando no se tiene contemplado un avance estimado. Para simular el avance fue sustituida su propiedad de avanzar por incluir un timer que en determinado tiempo actualice en una cantidad deseada el contenedor, ajustando ambos valores logras el tiempo y la fluides deseada. Al completarse la barra todos los elementos son destruidos y procede al menú principal.  


**2.-** El menú principal divide en 3 frames el cotenedor principal, primordialmente incorpora los botones deseados para la ejecución de análisis numérico y el botón para acceder al loggin, consecuentemente es declarado el contenedor de mis tablas de las bases de datos mediante un for que crea cada uno de los botones y el display principal que mostrara todas las instrucciones deseadas por el usuario, finalmente es incorporada una text box para simular el comportamiento de una terminal.

**2.1.-** El botón de Loggin destruye todos los widgets incorporados en la ventana principal y crea un objeto del archivo **Loggin.py** no obstante, el programa no espera inputs del usuario de manera indefinida por tal motivo es requerido transferir el **mainloop** de las ventanas en **Tkinter** que permiten mostrar la interfaz y en definitiva permite ejecutarlas en un bucle indeterminado.

**2.1.1.-** Al cargarse la pantalla de Loggin son creados dos frames el primero contiene la imagen del escudo de Jalisco y el segundo elemento el formulario necesario para obtener las credenciales de loggin no obstante, al no incorporarse una búsqueda en la base de datos de usuarios validos solo es incorporado un escenario de prueba.

**2.1.2.-** El contenedor de la clave en cada iteración censura la contraseña para una mayor privacidad, no obstante es susceptible de ser mejorado ya que por unos momentos es visible el último carácter debido a que el evento se detecta cuando la tecla es soltada debido a limitaciones de tiempo, adicionalmente persiste algunos errores al borrar el contenedor elemento por elemento y al activarse por evento al oprimir las teclas de mayúsculas y minúsculas lo incorpora como parte de la contraseña, de igual manera dispone de un output susceptible de mejor implementación al detectar un usuario no valido, en orden de evitar mostrar alertas intrusivas al usuario. 

En caso de detectar un loggin valido destruye la ventana para interrumpir su mainloop y en la función de loggin se vuelve a llamar al constructor de la ventana para que restaure los widgets de la ventana principal.

**2.2.-** El display para mostrar todas las bases de datos disponibles y el posterior frame aledaño que es actualizado cada vez que detecta un evento asociado a las tablas, para ello es eliminado todos los widgets dentro del mismo contenedor y remplazado por un CTkScrollableFrame para permitir ver registros y graficas de diferentes tamaños sin necesidad de redimensionarlas y dificultando su visibilidad, de igual manera en primera instancia fue optado el primer enfoque para mostrar las bases de datos disponibles, no obstante existen problemas al manipular las propiedades del ScrollabeFrame y requiere de un ancho mínimo del cual no se contrae y solo afecta a los elementos contenidos en este caso los botones. Fue sustituido solamente por los botones lo cual afecta la escalabilidad del proyecto, aunque funciona como versión de testeo.

**2.2.1.-** Las tablas son generadas a partir de la librería extra CTkTable donde solo es requerido indicar el numero de columnas, filas y los valores en una matriz, este widget es contenido dentro del widget con scroll, permitiendo la visibilidad de todos los registros.

**2.3.-** El último elemento incorporado es una terminal en una caja de texto, para incrustar texto es necesario tener una variable auxiliar que indique la posición donde es deseado mostrar el texto, por lo tanto en cada incorporación esa variable es actualizada para el siguiente dato, consecuentemente la lectura de los datos del usuario se ejecuta en una línea aparte, ya que no fue encontrada una solución satisfactoria para redireccionar el cursor del usuario la n cantidad de veces necesarias para ajustarse al texto, al detectar la tecla de enter se auxilia de la tecla return para en conjunto de la variable auxiliar contenedora de mi posición leer solamente esa línea que será posteriormente interpretada.

**2.3.1.-** Para interpretar el comando se adecua un menú donde se iteran todos los comandos disponibles en sentencias if al concordar ejecuta lo deseado, en el caso de estar logeado permite el acceso a comandos administrativos relacionados a la base de datos por ende en última instancia es comprobado el estado del loggin para brindar acceso a dichos comandos.

Por malas prácticas derivadas del desarrollo del backend brinda comandos de actualización, edición y eliminación de registros en cada una de las tablas haciendo inviable la construcción eficiente de un buen menú ya que tendría que realizar una comprobación por cada tabla, creando 3 funciones por cada tabla en lugar de 1 general donde solo sea pasado como argumento el nombre de la tabla en conjunto con elementos extras marcados en none por si es requerida sobrecargar el método y hacerlo general. De igual manera comprende un gran rango de mejora la terminal ya que es susceptible de generar errores y el menú de navegación dispone de demasiadas estructuras de control anidadas, las cuales pueden ser suplantadas por funciones.

Adicionalmente el comando help guarda en un diccionario todos los comandos disponibles para mostrarlos subsecuentemente y brindar retroalimentación al usuario de la sintaxis requerida y la manera de operar de cada sentencia.


**Aprendizaje**

**- Grid:** Es una manera de gestionar la posición de los frames dentro de una ventana, para ello requiere la columna y fila deseada, para configurar esto último es indispensable escribir:

Frame.rowconfigure({posicion}, weight = {valor númerico})

Esto permitira indicar el numero de filas y columnas, es posible incorporar elementos sin emplearlo no obstante al momento de modificar el tamaño de la tabla los elementos permanecerán estáticos, por lo tanto, simula el comportamiento de mostrar cosas en display por el método pack. El valor numérico de weight indica si es deseado la expansión del elemento en caso de detectar una redimensión de la pantalla reposicionando el contenido interno, si no es deseado dicho comportamiento incorporas un 0, el resto rango de valores indica en que proporción es requerido.

La sentencia “**sticky = {Posicones (n = norte, s = sur, e = este, w = oeste}**” indica si es deseado expandir el contenedor en una dirección, por lo tanto, al incrementar su tamaño redimensionará los elementos incorporados, al incorporarlo con un weight en su fila o columna este permitirá al elemento actualizar su posición en el display el argumento sticky expandirlo.

**- Dimensiones:** Con el objetivo de adaptar los elementos gráficos a cualquier pantalla es optada calcular proporciones, no obstante, se presenta un problema si ejecutamos funciones auxiliares para obtener el tamaño de los elementos padres brindan tamaños superiores como lo son winfo_req y winfo, la primera muestra las dimensión del eje deseado que requiere el objeto para ser mostrado y el segundo permite conocer el mismo parámetro pero solo cuando el elemento se encuentre dibujado en la ventana. Para solventar este problema se opto por crear variables contenedoras de la primera sentencia de la ventana en orden de solamente pasar dicho valor y el porcentaje deseado para obtener el valor esperado.

**- Mainloop:** Es la función que permite a las ventanas permanecer presentas y esperar de carácter indefinido inputs del usuario, por lo tanto, si es requerido llamar a otro objeto para alterar la ventana es requerido al crear el objeto transferir la función mainloop, ya que en caso contrario persistirá en la ejecución de la función de la ventana original ignorando el comportamiento deseado.
