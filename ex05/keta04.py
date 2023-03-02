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
# : util : is_dicemal
def is_dicemal(_val):
	'''
	Return true if the input value is dicemal by checking is the value instance of int or float
	- [parameter] _val
	'''
	return	isinstance(_val, int) or isinstance(_val, float)

# --------------------------------------------------------------------------------
# : function : keta
def ft_keta04(_tup):
	'''
	Display key-value of the dictionaries.
	  - [paramter] _dic
	'''
	if isinstance(_tup, tuple):
		if	len(_tup) == 5:
			if	all(
					isinstance(_tup[_idx], int) and
					0 <= _tup[_idx] < 100
                	for _idx in range(2)) and
				is_dicemal(_tup[2]) and
				is_dicemal(_tup[4]) and
				isinstance(_tup[3], int):
				print(
					f"{BLU}{BOL}{UND}[Keta04]{RES}",
					f"{GRE}[Success]{RES}",
					f"{BOL}{UND}",
						f"{_tup[0]:02},",
						f"{_tup[1]:02},",
						f"{_tup[2]:.2f},",
						f"{_tup[3]:.2e},",
						f"{_tup[4]:.2e}",
					f"{RES}")
			else:
				print(
					f"{BLU}{BOL}{UND}[Keta04]{RES}",
					f"{RED}[Failure]{RES}",
					f"Please make sure the {CYA}{BOL}{UND}[keta]{RES}'s foramt is",
					f"{YEL}{BOL}{UND}<non-negative int>{RES},",
					f"{YEL}{BOL}{UND}<non-negative int>{RES},",
					f"{YEL}{BOL}{UND}<decimal>{RES},",
					f"{YEL}{BOL}{UND}<int>{RES},",
					f"{YEL}{BOL}{UND}<decimal>{RES}.",)
		else:
			print(
				f"{BLU}{BOL}{UND}[Keta04]{RES}",
				f"{RED}[Failure]{RES}",
				f"The {CYA}{BOL}{UND}[keta]{RES}'s {YEL}{BOL}length is not {BOL}5{RES}.",)
	else:
		print(
			f"{BLU}{BOL}{UND}[Keta04]{RES}",
			f"{RED}[Failure]{RES}",
			f"The {CYA}{BOL}{UND}[keta]{RES} is {YEL}{BOL}{BOL}not tuple{RES}.",)

# --------------------------------------------------------------------------------
# : main
# keta variable : dictionary
# default value : (0, 4, 132.42222, 10000, 12345.67)
keta = (0, 4, 132.42222, 10000, 12345.67)

ft_keta04(keta)