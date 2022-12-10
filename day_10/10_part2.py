def new_pixel(x, cycle):
    sprite = range(x, x+3)
    new_line = '' if cycle%40 else '\n'
    if cycle in sprite:
        return '#'+new_line
    else:
        return '.'+new_line


with open('input') as f:
	data = f.read()


commands = list(map(lambda x:x.split(' '), data.split('\n')[:-1]))

x = 1
cycle = 1
CRT = ''

for command in commands:
    n_of_cycles = 2 if command[0]=='addx' else 1
    for i in range(n_of_cycles):
        CRT += new_pixel(x, cycle%40)
        cycle += 1
    if n_of_cycles==2:
        x += int(command[1])


print(CRT)
