#This solution is longer but more efficent
def translate_direction(direction, dims):
    n, m = dims
    directions = {
        'down': (range(1, n), range(m), -1, 0),
        'right': (range(n), range(1, m), 0, -1),
        'up': (range(n - 2, -1, -1), range(m), 1, 0),
        'left': (range(n), range(m - 2, -1, -1), 0, 1)}
    
    if direction not in directions:
        return None
    
    return directions[direction]
               
def is_visible_among_direction(forrest, direction):
    n, m = forrest.shape
    is_visible_matrix = np.ones(forrest.shape, dtype=bool)
    max_matrix = forrest.copy()
    
    range_x, range_y, step_x, step_y = translate_direction(direction, (n,m))
    for i in range_x:
        for j in range_y:
            if max_matrix[i+step_x,j+step_y]<forrest[i,j]: # If the tree is the tallest in a direction then it's visible
                is_visible_matrix[i,j] = True
                max_matrix[i,j] = forrest[i,j]
            else:
                is_visible_matrix[i,j] = False
                max_matrix[i,j] = max_matrix[i+step_x,j+step_y]
    
    return is_visible_matrix

def is_visible(forrest):    
    n, m = forrest.shape
    
    right = is_visible_among_direction(forrest, 'right')
    down  = is_visible_among_direction(forrest, 'down')
    left  = is_visible_among_direction(forrest, 'left')
    up    = is_visible_among_direction(forrest, 'up')
	
    return right | down | left | up # If a tree is visible in any direction, then in visible

import numpy as np

with open('input') as f:
	data = f.read()

lines = data.split('\n')[:-1]
forrest = np.array(tuple(map(tuple, lines)), dtype=np.int32)

visible_trees = is_visible(forrest)
num_visible = visible_trees.sum()

print(f'The number of visible trees is: {num_visible}')
