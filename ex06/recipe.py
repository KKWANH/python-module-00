# --------------------------------------------------------------------------------
# : color code
RED = '\033[91m'
GRE = '\033[92m'
YEL = '\033[93m'
BLU = '\033[94m'
MAG = '\033[95m'
CYA = '\033[96m'
RES = '\033[0m'
BOL = '\033[1m'
UND = '\033[4m'

# --------------------------------------------------------------------------------
# : global variable : cookbook
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
		"meal":			"lunch",
		"prep_time":	15,
	},
}

# --------------------------------------------------------------------------------
# : function : input
def ft_input(_menu, _str):
	print(
		f"{BOL}{UND}{_menu}{RES}    ",
		f"{_str}\n",
		f"             : {CYA}",
		end='')
	key = input()
	print(
		f"{RES}",
		end='')
	return key

# --------------------------------------------------------------------------------
# : function : getter
def ft_get_recipe():
	print(
		f"{GRE}{BOL}{UND}[Recipes]{RES}    ",
		f"{BOL}Available recipes:{RES}")
	for key, _ in _cookbook.items():
		print(
			f"              {GRE}{key}{RES}")

# --------------------------------------------------------------------------------
# : function : getter - detail
def ft_get_recipe_details():
	key = ft_input(f"{GRE}[Recipes]", "Please input the recipe name.")
	val = _cookbook.get(key)
	if val:
		print(
			f"{GRE}[Ingredients]{RES}",
			f"{val['ingredients']}")
		print(
			f"{GRE}[Meal Type]{RES}  ",
			f"{val['meal']}")
		print(
			f"{GRE}[Preparation]{RES}",
			f"{val['prep_time']} minutes")
	else:
		print(
			f"{RED}{BOL}{UND}[Error]{RES}      ",
			f"{YEL}{BOL}Sorry, it doesn't exist.{RES} To see the list of recipes, press 4 in the option menu.")

# --------------------------------------------------------------------------------
# : function : add_recipe
def ft_add_recipe():
	name = ft_input(f"{GRE}[Recipe]", " Enter a name")
	if not len(name):
		print(
			f"{RED}{BOL}{UND}[Error]{RES}      ",
			f"{YEL}{BOL}The name is mandatory.{RES}")
		return

	ings = []
	print(
		f"{BOL}{UND}{GRE}Recipe{RES}       ",
		f"Now start to enter ingredients, press 'enter' to stop.\n",
		end='')
	while True:
		ingr = input(f"              : {CYA}")
		print(
			f"{RES}",
			end='')
		if len(ingr):
			ings.append(ingr)
		else:
			break
	meal = ft_input(f"{GRE}[Recipe]", " Enter a meal type")
	if not len(meal):
		print(
			f"{RED}{BOL}{UND}[Error]{RES}      ",
			f"{YEL}{BOL}The meal type is mandatory.{RES}")
		return

	prep = ft_input(f"{GRE}[Recipe]", " Enter a preparation time")
	if prep.isnumeric():
		prep = int(prep)
		if prep < 0:
			print(
				f"{RED}{BOL}{UND}[Error]{RES}      ",
				f"{YEL}{BOL}The input must be non-negative.{RES}")
			return
	else:
		print(
			f"{RED}{BOL}{UND}[Error]{RES}      ",
			f"{YEL}{BOL}The preparation time is mandatory.{RES}")
		return	

	_cookbook[name] = {
		'ingredients':	ings,
		'meal':			meal,
		'prep_time':	prep
	}

# --------------------------------------------------------------------------------
# : function : delete_recipe
def ft_delete_recipe():
	key = ft_input(f"{GRE}[Recipe]", " Please input an recipe name to delete.")
	val = _cookbook.get(key)
	if val:
		print(
			f"{GRE}{BOL}{UND}{RES}             ",
			f"{GRE}{BOL}Deleted successfully.{RES}")
		_cookbook.pop(key)
	else:
		print(
			f"{RED}{BOL}{UND}[Error]{RES}      ",
			f"{YEL}{BOL}Sorry, this recipe doesn't exist.{RES} To see the list of recipes, press 4 in the option menu.")

# --------------------------------------------------------------------------------
# : function : quit
def ft_quit():
	print(
		f"{BLU}{YEL}{UND}[Quit]{RES}       ",
		f"{BOL}The program will be closed soon. Good bye 😭{RES}")
	quit()

# --------------------------------------------------------------------------------
# : function : help
def ft_help():
	print(
		f"{YEL}{BOL}{UND}[Help]{RES}       ",
		f"{BOL}{UND}Available options{RES} :")
	for key, val in _options.items():
		print(
			f"{YEL}{BOL}{UND}{RES}             ",
			f"{CYA}{BOL}{UND}[{key}]{RES}",
			f"{MAG}{val['description']}{RES}")

# --------------------------------------------------------------------------------
# : global variables : options
_options = {
	'1': {
		'description':	'Add a recipe',
		'action':		ft_add_recipe
	},
	'2': {
		'description':	'Delete a recipe',
		'action':		ft_delete_recipe
	},
	'3': {
		"description":	'Recipe Details',
		"action":		ft_get_recipe_details
	},
	'4': {
		"description":	'List of Recipes',
		"action":		ft_get_recipe
	},
	'5': {
		"description":	'Quit',
		"action":		ft_quit
	},
	'6': {
		"description":	'Help',
		"action":		ft_help
	}
}

# --------------------------------------------------------------------------------
# : functions : main entrypoint
def ft_cookbook():
	print(
		f"{GRE}{BOL}{UND}[Entrypoint]{RES} ",
		f"Welcome to the {BOL}{UND}Cookbook controller{RES}!")

	ft_help()

	while True:
		opt = ft_input(
			f"{MAG}[Options]",
			f"Please select an option. To see the list of options, press 6.")
		sel = _options.get(opt)

		if sel:
			sel['action']()
		else:
			print(
				f"{RED}{BOL}{UND}[Error]{RES}      ",
				f"{YEL}{BOL}Sorry, it doesn't exist.{RES}")

# --------------------------------------------------------------------------------
# : main 
ft_cookbook()
