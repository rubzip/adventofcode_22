def find_marker(message):
	i = 14
	while len(set(message[i-14:i]))<14:
		i += 1
	
	if len(set(message[i-14:i])) == 14:
		return i
	else:
		return None
		
with open("input") as f:
	message = f.read()

marker = find_marker(message)
if marker:
	print(f'The marker index is: {marker} and the sequence is: {message[marker-14:marker]}')
else:
	print('Marker not Found')
