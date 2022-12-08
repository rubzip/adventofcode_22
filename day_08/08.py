def is_visible_among_direction(selected_tree, trees):
    visible_trees = 0
    for i, tree in enumerate(trees):
        if tree >= selected_tree:
            return False
    
    return True
    
def is_visible_tree(forrest, pos):
    i, j = pos
    element = forrest[i,j]
    
    right = is_visible_among_direction(element, forrest[i, j+1:])
    down  = is_visible_among_direction(element, forrest[i+1:, j])
    left  = is_visible_among_direction(element, forrest[i, :j][::-1])
    up    = is_visible_among_direction(element, forrest[:i, j][::-1])
    
    return right or down or left or up

import numpy as np

with open('input') as f:
	data = f.read()

lines = data.split('\n')[:-1]
forrest = np.array(tuple(map(tuple, lines)), dtype=np.int32)

n, m = forrest.shape

num_visible = 2*(n+m)-4 #The border is visible
for i in range(1, n-1):
	for j in range(1, m-1):
		num_visible += is_visible_tree(forrest, [i,j])

print(f'The number of visible trees is: {num_visible}')
