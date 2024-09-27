# archivo exclusivo para la conversion de datos
from app import obtener_clima
import argparse
import json
import csv

# obtener los datos del clima
datos = obtener_clima()

def convertir_json(datos):
    return json.dumps(datos, indent=4)

def convertir_csv(datos):
    # Creando una lista de diccionarios para el formato CSV
    csv_output = []
    csv_output.append(datos)
    
    # Definir los nombres de las columnas
    columnas = datos.keys()

    # Escribir el CSV en una cadena
    output = []
    output.append(",".join(columnas))  # Encabezados
    output.append(",".join(str(datos[col]) for col in columnas))  # Valores

    return "\n".join(output)

def convertir_texto(datos):
    # Formateando el diccionario como un texto plano legible
    texto = f"Ciudad: {datos['ciudad']}\nCondición: {datos['condicion']}\nTemperatura: {datos['temperatura']}°C"
    return texto

def main():
    # Configuración de argparse para manejar los argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description="Consulta el clima de una ubicación.")
    parser.add_argument("--format", "-f", type=str, choices=["json", "csv", "texto"], 
                        help="Formato de salida: json, csv, texto", required=True)
    args = parser.parse_args()

    formato_salida = args.format

    # Condiciones para la salida del formato
    if formato_salida == "json":
        print(convertir_json(datos))
    elif formato_salida == "csv":
        print(convertir_csv(datos))
    elif formato_salida == "texto":
        print(convertir_texto(datos))
    else:
        print("Formato no válido. Intente nuevamente.")

if __name__ == "__main__":
    main()
