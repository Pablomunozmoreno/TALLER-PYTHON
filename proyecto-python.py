iajeimport streamlit as st
import json
import requests
from datetime import datetime, timedelta

# Cargar las claves desde el archivo JSON
with open('claves.json') as claves_file:
    claves = json.load(claves_file)

# Configuración de tus claves API
openweather_api_key = claves['openweather_api_key']

# Funciones auxiliares para obtener íconos
def obtener_icono(descripcion, hora):
    if 'clear' in descripcion:
        return "🌞"  # Sol
    elif 'cloud' in descripcion:
        return "☁️"  # Nubes
    elif 'rain' in descripcion:
        return "🌧️"  # Lluvia
    elif 'storm' in descripcion:
        return "⛈️"  # Tormenta
    else:
        return "🌈"  # Desconocido

st.title('Clima por Horas Durante el Viaje')

# Entrada de usuario
ciudad = st.text_input("Introduce la ciudad de tu viaje:")
fecha_inicio = st.date_input("Selecciona la fecha de inicio de viaje:", datetime.now())
fecha_fin = st.date_input("Selecciona la fecha de fin de viaje:", datetime.now() + timedelta(days=5))

# Función para obtener el clima
def obtener_clima(ciudad, fecha_inicio, fecha_fin):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={openweather_api_key}&units=metric'
    respuesta = requests.get(url).json()
    
    if respuesta.get('cod') != '200':
        return f"No se ha podido recoger información para la ciudad: {ciudad}"

    resultados = []
    for dia in range((fecha_fin - fecha_inicio).days + 1):
        fecha = (fecha_inicio + timedelta(days=dia)).strftime("%Y-%m-%d")
        dia_clima = f"<div style='text-align: center; padding: 10px; border: 2px solid #4CAF50; border-radius: 10px; margin: 10px;'><strong>FECHA:</strong> {fecha}</div>"
        clima_encontrado = False
        
        horas_clima = ""
        for clima in respuesta['list']:
            if fecha in clima['dt_txt']:
                hora = clima['dt_txt'].split(" ")[1]
                descripcion = clima['weather'][0]['description']
                temperatura = clima['main']['temp']
                icono_clima = obtener_icono(descripcion, hora)
                horas_clima += f"<div style='display: inline-block; margin: 5px; padding: 10px; border: 1px solid #2196F3; border-radius: 5px;'><strong>HORA:</strong> {hora} &nbsp;&nbsp;&nbsp;&nbsp; <strong>DESCRIPCIÓN:</strong> {descripcion} {icono_clima} &nbsp;&nbsp;&nbsp;&nbsp; <strong>TEMPERATURA:</strong> {temperatura}°C</div>"
                clima_encontrado = True
        
        if not clima_encontrado:
            horas_clima += f"<div style='display: inline-block; margin: 5px; padding: 10px; border: 1px solid #FF5722; border-radius: 5px;'>No se ha podido recoger información de ese día de momento.</div>"
        
        dia_clima += f"<div style='text-align: center; display: flex; flex-wrap: wrap; justify-content: center;'>{horas_clima}</div>"
        resultados.append(dia_clima)

    return resultados

if st.button('Obtener clima'):
    resultados_clima = obtener_clima(ciudad, fecha_inicio, fecha_fin)
    
    for resultado in resultados_clima:
        st.markdown("<hr>", unsafe_allow_html=True)  # Separador
        st.markdown(resultado, unsafe_allow_html=True)  # Mostrar resultados

    st.markdown("<hr>", unsafe_allow_html=True)  # Separador final
