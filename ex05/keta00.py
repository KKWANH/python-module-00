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
def ft_keta00(_tup):
	'''
	Display about the format of tuple.
	  - [paramter] _tup
	  	: input variable must be tuple and made by integer.
	'''
	if isinstance(_tup, tuple):
		if all(isinstance(_var, int) for _var in _tup) and len(_tup):
			print(
				f"{BLU}{BOL}{UND}[Keta00]{RES}",
				f"{GRE}[Success]{RES}",
				f"The {len(_tup)} numbers are:",
				f"{CYA}{BOL}{UND}{', '.join([str(_var) for _var in _tup])}{RES}.")
		elif not len(_tup):
			print(
				f"{BLU}{BOL}{UND}[Keta00]{RES}",
				f"{RED}[Failure]{RES}",
				f"The {BOL}{UND}keta{RES} is {YEL}{BOL}empty{RES}.")
		else:
			print(
				f"{BLU}{BOL}{UND}[Keta00]{RES}",
				f"{RED}[Failure]{RES}",
				f"The {BOL}{UND}keta{RES} tuple's elements contains {YEL}{BOL}non-integers value{RES}.")
	else:
		print(
			f"{BLU}{BOL}{UND}[Keta00]{RES}",
			f"{RED}[Failure]{RES}",
			f"The {BOL}{UND}keta{RES} is not {YEL}{BOL}tuple{RES}.")

# --------------------------------------------------------------------------------
# : main
# keta variable : tuple, 3 integer.
# default value : 19, 42, 21
keta = (19, 42, 21)

ft_keta00(keta)