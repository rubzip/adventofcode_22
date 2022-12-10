def signal_strength(cycle, x):
    if cycle%40==20 and cycle<221:
        return cycle*x
    else:
        return 0


with open('input') as f:
	data = f.read()
	

commands = list(map(lambda x:x.split(' '), data.split('\n')[:-1]))

x = 1
cycle = 1
solution = 0

for command in commands:
    n_of_cycles = 2 if command[0]=='addx' else 1
    for i in range(n_of_cycles):
        solution += signal_strength(cycle, x)
        cycle += 1
    if n_of_cycles==2:
        x += int(command[1])


print(f'total signal strength is {solution}')
