# proyecto_colegio

Tipo de Aplicación: Aplicación web Educativa



Dirigida: A toda la Comunidad Educativa 



Roles del equipo:

Dueño del producto - Product Owner: Nayibe Carolina Gómez Flórez

SCRUM Master - Líder: Arnol Espitaleta Sierra

Desarrolladores - Developers: Grupo 3

Integrantes Grupo 3: Emerson Gutierrez, Nayibe Carolina Gómez Flórez, Arnol Espitaleta Sierra, Eilin Bellahana Hernández Gómez.

 
Justificación y/o pertinencia de la temática:
El presente proyecto nace de la evidencia de falencias en algunas plataformas educativas actualmente usadas en instituciones educativas públicas, que ahora debido al trabajo virtual que se viene desarrollando desde marzo del 2020 en toda la comunidad educativa por la pandemia del covid 19 desgastan al maestro, directivos, estudiantes y acudientes, generando confusiones en especial a los acudientes y estudiantes.
En vista de lo anterior deseamos hacer una aplicación web educativa que supla algunas de las necesidades existentes y así ayudar a organizar y optimizar el tiempo de trabajo de profesores y estudiantes.
Algunas soluciones que aportará este proyecto es: La implementación de correos organizados en carpetas que lleguen a profesores, clasificando su bandeja de entrada por curso y asignatura; mensajes con avisos, recordatorios y alertas de tareas las cuales mostrarán sus respectivas fechas de inicio y fin.
Se hará uso de la API del sistema de conferencias Open Source llamado Jitsi Meet, esto pues, para permitir que no haya límite de tiempo en el uso de un sistema de conferencias y permita realizar la respectiva grabación una vez se necesite. Por otro lado se pretende flexibilizar el ingreso a un aula centralizada donde los recursos de esa clase puedan mantenerse estables, similarmente a un repositorio.


Mundo del problema


Necesidad:


Actualmente las plataformas virtuales han venido ganando espacios demasiado significativos en las instituciones educativas, lo cual les ha convertido en herramientas de transferencia y gestión de conocimiento, en cada una las diferentes áreas del saber, permitiendo a los diferentes actores de la comunidad educativa, tales como: administrativos, docentes, estudiantes y padres de familia logren centralizar información apalancando los procesos institucionales, transformándose en recursos que dinamizan la función de cada integrante.
Lo anterior se ha visto evidenciado ampliamente con la llegada de la pandemia, la cual generó que los procesos que se llevaban a cabo dentro del establecimiento educativo fueron trasladados a los hogares de docentes como estudiantes, allí los recursos digitales se convirtieron en herramientas que lograron flexibilizar los procesos escolares y así como permitió la continuidad de dichas labores, también se observan falencias en dichas plataformas, ya que no todas integran funcionalidades que permitan adaptación de acuerdo al contexto de cada institución educativa. 
Competencias: https://quid.pw/, http://www.servinotas.com/ www.edupage.org, https://www.sisga.com.co/  https://edusysltda.com/responsive/index.php/page/content/plataforma-academica-integra
https://tomi.digital/es?utm_source=google&utm_medium=seo
Factor diferenciador:
Crearemos una plataforma educativa con un conjunto de herramientas tecnológicas que no tienen otras plataformas educativas existentes como correos organizados en carpetas para profesores y directivos, mensajes, recordatorios y alertas de vencimiento de tareas y evaluaciones, uso de la API del sistema de conferencias Open Source llamado Jitsi Meet.
Objetivos del proyecto:
General: 
Diseñar y desarrollar un sistema de información web responsivo que permita la gestión escolar multiplataforma mediante una API REST con el framework Django en lenguaje Python e interfaz de usuario con el framework Bootstrap y comunicación de la interfaz a través de lenguaje TypeScript en el framework Angular js.
 
Específicos: (verbo , que, como , para que)
Gestionar los usuarios de la comunidad educativa donde se implemente el sistema de información (Docentes, directivos, alumnos y padres de familia) para comunicarse ágil y eficientemente.
Gestionar la información a través de una base de datos relacional Mysql.
Generar mediante el framework Django en lenguaje back-end; python el envío de correos electrónicos ordenados por grado, docente y curso.
Integrar mediante un repositorio en común las funcionalidades del sistema de información educativo (Git y Github)
Integrar plataforma open source Jitsi Meet para crear reuniones en tiempo real sin limite de tiempo y opción de grabación a través de la API de esa aplicación.
Gestionar las notas de los estudiantes dentro del sistema.
Generación de alertas en vencimiento de tareas y evaluaciones.
Generar reportes del observador de uno o varios estudiantes.
 
 
 
Requerimientos funcionales y no funcionales: 

Los requerimientos funcionales entendidos como lo que necesita el software para ser funcional:
La aplicación debe enviar un e-mail en el correo de la plataforma, direcciona este a una carpeta en la bandeja de entrada del destinatario (si es docente) según una clasificación acordada (el grado y la asignatura).
Al oprimir enviar una asignación o tarea se publica visiblemente y con recordatorios periódicos las fechas de inicio y fin de la misma.
Desarrollar usuarios de tipo maestro, alumnos, padres y directivos.
Generar un reporte que notifique al correo de padres, permitiendo un seguimiento continuo de la asistencia y participación por parte del alumnado.
Construir un cronograma con fechas, horarios y alertas donde se puedan generar recordatorios o programar las clases.
La aplicación debe mantener un espacio colaborativo con recursos permanentes que permita un acceso sencillo y actualizado.



Los requerimientos no funcionales:

Verificación de usuarios
Seguridad.(especificar)
Un programa intuitivo que pueda manejar cualquiera desde el maestro hasta el padre de familia.
Velocidad.(especificar)
Responsive.
Datos de la comunidad educativa.
Atención al usuario.


