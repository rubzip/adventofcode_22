day=$(date +"%d")

# Crear la carpeta "day_08"
mkdir "day_$day"

# Crear el archivo "08.py" dentro de la carpeta "day_08" y agregar contenido
touch "day_$day/08.py"
echo "with open('input') as f:" >> "day_$day/08.py"
echo "\tdata = f.read()" >> "day_$day/08.py"
