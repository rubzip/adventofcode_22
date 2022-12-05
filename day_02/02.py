def calculate_points(game):
	player_translator = {'X':'R', 'Y':'P', 'Z':'S'}
	opponent_translator = {'A':'R', 'B':'P', 'C':'S'} 
	
	opponent = opponent_translator[game[0]]
	player   = player_translator[game[2]]
	
	points = {'R':1, 'P':2, 'S':3}[player]
	
	if player==opponent: # 
		points += 3
	elif (player=='R'and opponent=='S')or(player=='P'and opponent=='R')or(player=='S'and opponent=='P'): # Victory
		points += 6
	
	return points
	
with open("input") as f:
	data = f.read()

games = data.split('\n')[:-1]

total_points = sum(map(calculate_points, games))

print(f'The total points following this strategy: {total_points}')
