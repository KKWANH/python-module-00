_cookbook = {
	"sandwich": {
		"ingredients":	['ham', 'bread', 'cheese', 'tomatoes'],
		"meal":			"lunch",
		"prep_time":	10,
	},
	"cake": {
		"ingredients":	['flour', 'sugar', 'eggs'],
		"meal":			"dessert",
		"prep_time":	60,
	},
	"salad": {
		"ingredients":	['avocado', 'arugula', 'tomatoes', 'spinach'],
		"meal":			lunch",
		"prep_time":	15,
	},
}


def get_all_recipe():
	for key, val in _cookbook.items():
		print('{}: {}'.format(key, val))

def get_recipe_details():
	key = input('Please enter a recipe name to get its details:\n')
	val = _cookbook.get(key)
	if val:
		print('Recip for {}:\nIngredients list: {}\nTo be eaten for {}.\n\
				Takes {} minutes of cooking.'.format(key,
													 val['ingredients'],
													 val['meal'],
													 val['prep_time']))
	else:
		print('Sorry, this recipe does not exist.')


def delete_recipe():
	key = input("Please enter recipe name:\n")
	val = _cookbook.get(key)
	if val:
		print('success deleted')
		_cookbook.pop(key)
	else:
		print('Sorry, this recipe does not exist')


def add_new_recip():
	name = input('Enter a name:\n')
	if not len(name):
		print('The name is requered')
		return

	ings = []
	print('Enter ingredients:')
	while True:
		ingr = input('')
		if len(ingr):
			ings.append(ingr)
		else:
			break
	meal = input('Enter a meal type:\n')
	if not len(meal):
		print('The Type is requered')
		return

	prep = input('Enter a preparation time:\n')
	if prep.isnumeric():
		prep = int(prep)
		if prep < 0:
			print('Invalid input the preparation  time is non-negative')
			return
	else:
		print("The preparation time is requered")
		return
	_cookbook[name] = {
		'ingredients':	ings,
		'meal':			meal,
		'prep_time':	prep
	}

def quit_app():
	print('cookbook closed. Goodbye !')
	quit()

_options = {
	'1': {
		'description':	'Add a recipe',
		'action':		add_new_recip
	},
	'2': {
		'description':	'Delete a recipe',
		'action':		delete_recipe
	},
	'3': {
		"description":	'Print a recipe',
		"action":		get_recipe_details
	},
	'4': {
		"description":	'Print the _cookbook',
		"action":		get_all_recipe
	},
	'5': {
		"description":	'Quit',
		"action":		quit_app
	}
}


def ft_options():
	print('List of available option:')
	for k, v in _options.items():
		print('  {}: {}'.format(k, v['description']))


def ft_cookbook():
	print('Welcome to the Python _cookbook !')
	ft_options()
	while True:
		selcet = _options.get(input('Please select an option:\n'))
		if selcet:
			selcet['action']()
		else:
			print('Sorry, this option does not exist.')
			ft_options()
		print()


ft_cookbook()
