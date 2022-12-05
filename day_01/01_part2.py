def sum_calories(stack_of_calories):
	"""
    Calculate the total number of calories in a stack of food items.

    Args:
        stack_of_calories (str): A string containing a list of calories,
            with each calorie separated by a newline character.

    Returns:
        int: The total number of calories in the stack of food items.

    Examples:
        >>> sum_calories("150\n100\n200")
        450

        >>> sum_calories("0\n0\n0")
        0

    """
	cast_to_int = lambda n: 0 if n=='' else int(n) # If an element is '' cast as 0
	x = map(cast_to_int, stack_of_calories.split('\n'))
	
	return sum(x)


with open("input") as f:
	data = f.read()

elves_calories = data.split('\n\n') 
total_of_calories = map(sum_calories, elves_calories)

top3_cal = sum(sorted(total_of_calories, reverse=True)[:3])

print(f"The 3 elves with more calories have: {top3_cal} cal")
