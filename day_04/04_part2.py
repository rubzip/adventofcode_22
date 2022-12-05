def overlaps(raw_pair):
    x, y = create_pair(raw_pair)
    return min(x[1], y[1]) >= max(x[0], y[0])

def create_pair(raw_pair):
	return tuple(map(lambda x: tuple(map(int, x.split('-'))), raw_pair.split(',')))

with open("input") as f:
	data = f.read()

pairs = data.split('\n')[:-1]

total_incongruent_pairs = sum(map(overlaps, pairs))

print(f'The number of useless pairs is: {total_incongruent_pairs}')
