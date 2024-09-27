#!/bin/bash

# Este script automatiza la instalación de dependencias y la configuración del entorno virtual

# Paso 1: Actualizar el sistema
echo "Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y
echo "Sistema actualizado."

# Paso 2: Instalar Python y pip
echo "Instalando Python y pip..."
sudo apt install python3 python3-pip -y
echo "Python y pip instalados."

# Paso 3: Crear y activar un entorno virtual
echo "Creando un entorno virtual..."
python3 -m venv .venv  # Crea un entorno virtual llamado .venv
echo "Activando el entorno virtual..."
source .venv/bin/activate  # Activa el entorno virtual
echo "Entorno virtual activado."

# Paso 4: Instalar dependencias desde requirements.txt
if [ -f requirements.txt ]; then
    echo "Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt
    echo "Dependencias instaladas."
else
    echo "No se encontró requirements.txt. Por favor, crea este archivo para listar las dependencias."
fi

# Paso 5: Mensaje final
echo "Configuración completada. ¡Listo para comenzar!"
