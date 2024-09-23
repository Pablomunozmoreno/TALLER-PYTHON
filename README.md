# TALLER-PYTHON
Este proyecto es una aplicación web interactiva desarrollada con Streamlit que permite a los usuarios obtener el pronóstico del clima por horas para cualquier ciudad durante un rango de fechas. La aplicación utiliza la API de OpenWeather para obtener los datos del clima en tiempo real y los presenta de forma clara y visual, mostrando información como la temperatura, la descripción del clima y un ícono representativo (sol, nubes, lluvia, tormenta, etc.).

Características Principales:

  - Entrada de Usuario:
    
El usuario introduce el nombre de la ciudad que quiere consultar y selecciona una fecha de inicio y fin para el rango de días de su viaje.

  - Pronóstico Detallado:
    
El sistema hace una llamada a la API de OpenWeather para obtener el pronóstico del clima para la ciudad y el rango de fechas proporcionados.
Se muestran los datos del clima por horas, incluyendo la hora exacta, una descripción (por ejemplo, "nublado", "lluvia ligera"), la temperatura en grados Celsius y un ícono correspondiente (sol, nubes, lluvia, etc.).

  - Visualización del Clima:
    
La información de cada día y sus horas se presenta con un diseño limpio y organizado mediante bloques que contienen el pronóstico de cada hora.
Si no hay datos disponibles para un día en particular, se muestra un mensaje indicando que la información no está disponible.

  - Manejo de Errores:
    
Si la API no puede devolver la información para una ciudad dada, se muestra un mensaje de error.

(La clave de la API es personal e intransferible, de manera que cada usuario debe solicitar su propia clave)
