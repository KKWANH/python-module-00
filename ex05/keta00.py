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
	This functions prints informations about input text.
	You can only input a string.
	The types of characters that you can give:
		- upper case
		- lower case
		- punctuation
		- spaces
	'''
	if isinstance(_tup, tuple):
		if all(isinstance(_var, int) for _var in _tup) and len(_tup):
			print(
				f"{BLU}{BOL}{UND}[Keta00]{RES}",
				f"The {len(_tup)} numbers are:",
				f"{CYA}{BOL}{UND}{', '.join([str(_var) for _var in _tup])}{RES}."
			)

# --------------------------------------------------------------------------------
# : main
# keta variable : tuple, 3 values
keta = (19, 42, 21)

ft_keta00(keta)