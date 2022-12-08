def count_visible_trees(selected_tree, trees):
    for i, tree in enumerate(trees):
        if tree >= selected_tree:
            return i+1
    
    return len(trees)
    
def tree_score(forrest, pos):
    i, j = pos
    element = forrest[i,j]
    
    right = count_visible_trees(element, forrest[i, j+1:])
    down = count_visible_trees(element, forrest[i+1:, j])
    left = count_visible_trees(element, forrest[i, :j][::-1])
    up = count_visible_trees(element, forrest[:i, j][::-1])
    
    return right * down * left * up

import numpy as np

with open('input') as f:
	data = f.read()

lines = data.split('\n')[:-1]
forrest = np.array(tuple(map(tuple, lines)), dtype=np.int32)

n, m = forrest.shape

best_score, i_best, j_best = 0, 0, 0
for i in range(1, n-1):
    for j in range(1, m-1):
        score = tree_score(forrest, (i,j))
        if best_score <= score:
            best_score, i_best, j_best = score, i, j

print(f'The best position is: {(i_best, j_best)} with a score: {best_score}')
