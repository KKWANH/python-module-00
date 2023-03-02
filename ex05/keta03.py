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
def ft_keta03(_str):
	'''
	Print until the 42th letter of input string
	  - [paramter] _str
	'''
	if isinstance(_str, str):
		print(
			f"{BLU}{BOL}{UND}[Keta03]{RES}",
			f"{GRE}[Success]{RES}",
			f"{UND}{_str:->42.42}{RES}",
			end='')
	else:
		print(
			f"{BLU}{BOL}{UND}[Keta03]{RES}",
			f"{RED}[Failure]{RES}",
			f"{UND}The keta is not {YEL}{BOL}string{RES}",)

# --------------------------------------------------------------------------------
# : main
# keta variable : string
# default value : "The right format"
keta = "The right format"

ft_keta03(keta)