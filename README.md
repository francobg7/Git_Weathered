# GIT-WEATHERED

**GIT-WEATHERED** es una aplicación que permite obtener en tiempo real las condiciones climáticas de cualquier ciudad ingresada por el usuario, utilizando la API de [OpenWeatherMap](https://openweathermap.org/). La aplicación devuelve los datos climáticos en varios formatos como **JSON**, **CSV** y **texto plano**, según la preferencia del usuario.

## Funcionalidad

La aplicación toma el nombre de una ciudad ingresada por el usuario y consulta la API de OpenWeatherMap para obtener la siguiente información:

- Condición climática actual (descripción del clima)
- Temperatura

El usuario tiene la opción de recibir los resultados en uno de los siguientes formatos:

- JSON
- CSV
- Texto plano

## Requisitos

Para ejecutar esta aplicación, necesitas tener instalado lo siguiente:

- **Python 3.x** (versión 3.6 o superior recomendada)

### Módulos necesarios

Instala los módulos requeridos usando `pip`:

```bash
pip install requests argparse



