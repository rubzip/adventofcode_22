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
  if num_of_zeros==2: # If there is no difference between tail and head => There is no movement. Example (0,0)
      return 0
  elif num_of_two: # If in a direction the distance is 2
      if num_of_zeros==1: # perpendicular movement among the direction. Example (2,0), (-2,0), (0,2), (0,-2)
          return difference // 2
      else: # diagonal movement. Example (2,1), (-2,1), (-1,2), (1,-2)...
          return np.where(difference>0, 1, -1)
  else: # If in no direction the distance is 2, then there will be no movement. Example (1,0), (-1,1)...
      return 0


def make_a_move(tail, head, direction):
    head_move = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    head2 = head + np.array(head_move[direction])
    tail2 = tail + move_tail(head2-tail)
    
    return tail2, head2
        

with open('input') as f:
	data = f.read()

moves = list(map(lambda x: x.split(' '), data.split('\n')[:-1]))

head = np.array((0,0))
tail = np.array((0,0))
all_positions = set()
all_positions.add(tuple(tail))
for move in moves:
    direction, steps = move
    for i in range(int(steps)):
        tail, head = make_a_move(tail, head, direction)
        all_positions.add(tuple(tail))

total_positions = len(all_positions)
print(f'The total of positions: {total_positions}')