def get_priority(char):
	if char.islower():
		return ord(char)-96
	elif char.isupper():
		return ord(char)-38
	else:
		pass


def split_rucksack(rucksack):
	size = len(rucksack)
	
	first_compartment = set(rucksack[:size//2]) 
	second_compartment = set(rucksack[size//2:])
	#Compartments are converted to sets because we dont care about repeated elements
	return first_compartment, second_compartment


def total_priority(rucksack):
	first_compartment, second_compartment = split_rucksack(rucksack)
	priority = 0
	
	#Here we check coincidences:
	for i in first_compartment:
		if i in second_compartment:
			priority += get_priority(i)
			
	return priority
	

with open("input") as f:
	data = f.read()
	
rucksacks = data.split('\n')[:-1]
global_priority = sum(map(total_priority, rucksacks))

print(f'The global priority is: {global_priority}')
