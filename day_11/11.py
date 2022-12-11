def new_value(old, operator, value):
    if value=='old':
        val = old
    else:
        val = int(value)
    if operator=='+':
        return (old+val)//3
    elif operator=='*':
        return (old*val)//3
    else:
        print(f'ERROR {operator}')


with open('input') as f:
	data = f.read()
	
	
"""
Monkey {3}:
  Starting items: {71, 64, 75}
  Operation: new = old {+} {2}
  Test: divisible by {17}
    If true: throw to monkey {6}
    If false: throw to monkey {2}
"""
monkeys = list()
raw_monkeys = data.split('\n\n')
for raw_monkey in raw_monkeys:
    monkey = raw_monkey.split('\n')
    monkey_dict = dict()
    
    num_monkey = int(monkey[0].split(' ')[-1][:-1])
    monkey_dict['starting_items'] = list(map(int, monkey[1][17:].split(',')))
    monkey_dict['operation'] = monkey[2].split(' ')[-2:]
    monkey_dict['test'] = int(monkey[3].split(' ')[-1])
    monkey_dict['if_true']  = int(monkey[4].split(' ')[-1])
    monkey_dict['if_false'] = int(monkey[5].split(' ')[-1])
    
    monkeys.append(monkey_dict)

rounds = 20
num_of_monkeys = len(monkeys)

inspected_objects = dict()
for i in range(num_of_monkeys):
    inspected_objects[i] = 0

for _ in range(rounds):
    for i in range(num_of_monkeys):
        inspected_objects[i] += len(monkeys[i]['starting_items'])
        for item in monkeys[i]['starting_items']:
            new = new_value(item, monkeys[i]['operation'][0], monkeys[i]['operation'][1])
            if new % monkeys[i]['test']==0:
                monkeys[monkeys[i]['if_true']]['starting_items'].append(new)
            else:
                monkeys[monkeys[i]['if_false']]['starting_items'].append(new)
        monkeys[i]['starting_items'] = []
            

sorted_values = sorted(inspected_objects.values())
monkey_business = sorted_values[-1]*sorted_values[-2]

print(f'monkey business {monkey_business}')