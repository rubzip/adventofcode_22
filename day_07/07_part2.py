def clean_commands(commands):
	if commands[0][:2]=='cd': # cd
		return commands[0].split(' ')
	elif commands[0][:2]=='ls': # ls
		size = 0
		dirs = []
		for doc in commands[1:]:
			if doc[:3] == 'dir':
				dirs.append(doc.split(' ')[1])
			else:
				size += int(doc.split(' ')[0])
				
		return ['ls', size, dirs]
	else:
		print('ERROR')


def cd(path, folder):
	if folder == '/':
		return ''
	elif folder == '..':
		return '/'.join(path.split('/')[:-1])
	else:
		return path + '/' + folder


with open("input") as f:
	data = f.read()

raw_lines = data.split('$ ')
lines = list(map(lambda x: x.split('\n')[:-1], raw_lines))[1:]

commands = list(map(clean_commands, lines))

path = ''
directories = dict()
for command in commands:
	if command[0] == 'cd':
		path = cd(path, command[1])
	elif command[0] == 'ls':
		directories[path] = command[1]
	else:
		print('ERROR')

dirs = sorted(list(map(list, directories.items())), key=lambda x: x[0]) #Directories sorted by name

for i, dir1 in enumerate(dirs):
	for dir2 in dirs[i+1:]:
		if dir1[0] in dir2[0]:
			directories[dir1[0]] += dir2[1]
			
TOTAL_SPACE  = 70000000
used_space   = directories['']
needed_space = 30000000 - (TOTAL_SPACE - used_space)

for dir3 in sorted(list(map(list, directories.items())), key=lambda x: x[1]): #Directories sorted by size
	if dir3[1] >= needed_space:
		print(f'We need to delete {dir3[0]} with a size of {dir3[1]}')
		break




































