day=$(date +"%d")

mkdir "day_$day"

touch "day_$day/$day.py"
echo "with open('input') as f:" >> "day_$day/$day.py"
echo "\tdata = f.read()" >> "day_$day/$day.py"
