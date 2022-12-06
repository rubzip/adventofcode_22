def find_marker(message):
	i = 4
	while len(set(message[i-4:i]))<4:
		i += 1
	
	if len(set(message[i-4:i])) == 4:
		return i
	else:
		return None
		
with open("input") as f:
	message = f.read()

marker = find_marker(message)
print(f'The marker index is: {marker} and the sequence is: {message[marker-4:marker]}')
