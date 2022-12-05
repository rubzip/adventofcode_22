def is_fully_contained(raw_pair):
    x, y = create_pair(raw_pair)
    if x[0] <= y[0] and y[1] <= x[1]:
        return True
    elif y[0] <= x[0] and x[1] <= y[1]:
        return True
    else:
        return False

def create_pair(raw_pair):
	return tuple(map(lambda x: tuple(map(int, x.split('-'))), raw_pair.split(',')))

with open("input") as f:
	data = f.read()

pairs = data.split('\n')[:-1]

total_incongruent_pairs = sum(map(is_fully_contained, pairs))

print(f'The number of useless pairs is: {total_incongruent_pairs}')
