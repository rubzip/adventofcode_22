import re

def import_stacks():
	with open("stacks") as f:
		data = f.read()
	
	rows = data.split('\n')[:-2]
	stacks = dict()
	
	for i in range(1, 10):
		stacks[i] = []
	
	for row in rows:
		for i in range(1, 10):
			val = row[4*i - 3]
			if val.isalpha():
				stacks[i].append(val)
	
	for i in stacks:
		stacks[i] = stacks[i][-1::-1] # Reversed
		
	return stacks
	

def regular_expresion(move):
	return tuple(map(int, re.findall(r'\d+', move)))


def import_moves():
	with open("input") as f:
		data = f.read()
	
	raw_moves = data.split('\n')[:-1]
	moves = tuple(map(regular_expresion, raw_moves))
	
	return moves
	
		
def make_a_move(move, stacks):
	n, initial_pos, final_pos = move
	stacks[final_pos] += stacks[initial_pos][-n:][-1::-1]
	stacks[initial_pos] = stacks[initial_pos][:-n]


stacks = import_stacks()
moves = import_moves()

for move in moves:
	make_a_move(move, stacks)

solution = ''
for i in range(1,10):
	try:
		solution += stacks[i][-1]
	except:
		pass
		
print(f'After all movements the solution is: {solution}')
