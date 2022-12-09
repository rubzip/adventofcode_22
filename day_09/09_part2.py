import numpy as np

def move_tail(difference):
  """
  This is how we should move the tail:
  head-tail -> move    |  head-tail -> move
     (2,1)  -> (1,1)   |     (2,-1) -> (1,-1)
     (1,2)  -> (1,1)   |     (1,-2) -> (1,-1)
     (-1,2) -> (-1,1)  |     (-1,-2)-> (-1,-1)
     (-2,1) -> (-1,1)  |     (-2,-1)-> (-1,-1)
     (2,0)  -> (1,0)   |     (-2,0) -> (-1,0)
     (0,2)  -> (0,1)   |     (0,-2) -> (0,-1)
  """
  num_of_zeros = (difference==0).sum()
  num_of_two = (abs(difference)==2).sum()
  if num_of_zeros==2:
      return 0
  elif num_of_two:
      if num_of_zeros==1:
          return difference // 2
      else:
          return np.where(difference>0, 1, -1)
  else:
      return 0


def make_a_move(rope, direction):
    head_move = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    new_rope = list()
    new_rope.append(rope[0] + np.array(head_move[direction])) # head
    for i in range(1,len(rope)):
        new_knot = rope[i] + move_tail(new_rope[i-1]-rope[i])
        new_rope.append(new_knot)
    
    return new_rope
        

with open('input') as f:
	data = f.read()

moves = list(map(lambda x: x.split(' '), data.split('\n')[:-1]))

rope = list()
for i in range(10):
    rope.append(np.array((0,0)))

all_positions = set()
all_positions.add(tuple(rope[-1]))
for move in moves:
    direction, steps = move
    for i in range(int(steps)):
        rope = make_a_move(rope, direction)
        all_positions.add(tuple(rope[-1]))

total_positions = len(set(all_positions))
print(f'The total of positions: {total_positions}')
