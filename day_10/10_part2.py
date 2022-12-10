def sprite(x):
    if x<39:
        return list(range(x, x+3))
    else:
        return list(map(lambda y:(y-1)%40+1, range(x, x+3)))


def new_pixel(x, cycle):
    aux_cycle = (cycle-1)%40+1
    new_line = '' if aux_cycle!=40 else '\n'
    if aux_cycle in sprite(x):
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
        CRT += new_pixel(x, cycle)
        cycle += 1
    if n_of_cycles==2:
        x += int(command[1])


print(CRT)