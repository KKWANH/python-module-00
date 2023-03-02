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
# : function : keta
def ft_keta02(_tup):
	'''
	Display the full date from the keta tuple.
	  - [paramter] _tup
	  	: input variable must be tuple and made by integer.
	'''
	if isinstance(_tup, tuple):
		if all(isinstance(_var, int) for _var in _tup) and len(_tup):
			print(
				f"{BLU}{BOL}{UND}[Keta02]{RES}",
				f"{GRE}[Success]{RES}",
				f"{UND}{_tup[1]:02}/{_tup[2]:2}/{_tup[0]:4} {_tup[3]}:{_tup[4]}{RES}",)
		elif not len(_tup):
			print(
				f"{BLU}{BOL}{UND}[Keta02]{RES}",
				f"{RED}[Failure]{RES}",
				f"The {BOL}{UND}keta{RES} is {YEL}{BOL}empty{RES}.")
		else:
			print(
				f"{BLU}{BOL}{UND}[Keta02]{RES}",
				f"{RED}[Failure]{RES}",
				f"The {BOL}{UND}keta{RES} tuple's elements contains {YEL}{BOL}non-integers value{RES}.")
	else:
		print(
			f"{BLU}{BOL}{UND}[Keta02]{RES}",
			f"{RED}[Failure]{RES}",
			f"The {BOL}{UND}keta{RES} is not {YEL}{BOL}tuple{RES}.")

# --------------------------------------------------------------------------------
# : main
# keta variable : tuple, 3 integer.
# default value : 2019, 9, 25, 3, 30
keta = (2019, 9, 25, 3, 30)

ft_keta02(keta)