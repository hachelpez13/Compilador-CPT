#!/bin/bash

# Comprobar si se han pasado los dos parámetros
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <palabra_a_buscar> <directorio>"
    exit 1
fi

PALABRA=$1
DIRECTORIO=$2

# Comprobar si el directorio existe
if [ ! -d "$DIRECTORIO" ]; then
    echo "Error: El directorio '$DIRECTORIO' no existe."
    exit 1
fi

echo "Buscando '$PALABRA' en el directorio '$DIRECTORIO'..."
echo "----------------------------------------------------"

# -r: recursivo, -n: muestra número de línea, -w: palabra completa, -i: ignora mayúsculas
grep -rnwi "$DIRECTORIO" -e "$PALABRA"

if [ $? -ne 0 ]; then
    echo "No se encontraron coincidencias."
fi