def calculate_points(game):
	opponent_translator = {'A':'R', 'B':'P', 'C':'S'}
	win = {'R':'P', 'P':'S', 'S':'R'}
	lose ={'P':'R', 'S':'P', 'R':'S'} 
	points_dict = {'R':1, 'P':2, 'S':3}
	
	opponent = opponent_translator[game[0]]
	
	if game[2]=='X': # lose
		points = 0
		player = lose[opponent]
	elif game[2]=='Y': # draw
		points = 3
		player = opponent
	else: # win
		points = 6
		player = win[opponent]
	
	points += points_dict[player]
	
	return points	

	
with open("input") as f:
	data = f.read()

games = data.split('\n')[:-1]

total_points = sum(map(calculate_points, games))

print(f'The total points following this strategy: {total_points}')
