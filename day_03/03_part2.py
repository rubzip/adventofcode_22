def get_priority(char):
	if char.islower():
		return ord(char)-96
	elif char.isupper():
		return ord(char)-38
	else:
		pass


def make_teams(rucksacks):
	size = len(rucksacks)
	teams = list()
	for i in range(0, size, 3):
		teams.append(rucksacks[i:i+3])
		
	return teams


def total_priority(team):
	priority = 0
	
	rucksack1 = set(team[0])
	rucksack2 = set(team[1])
	rucksack3 = set(team[2])
	
	#Here we check coincidences:
	for i in rucksack1:
		if i in rucksack2 and i in rucksack3:
			priority += get_priority(i)
			
	return priority
	

with open("input") as f:
	data = f.read()
	
rucksacks = data.split('\n')[:-1]
teams = make_teams(rucksacks)

global_priority = sum(map(total_priority, teams))

print(f'The global priority is: {global_priority}')
