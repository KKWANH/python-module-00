# --------------------------------------------------------------------------------
# : import
import sys

# --------------------------------------------------------------------------------
# : argument
arv = sys.argv
arc = len(arv)

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
# : main
def ft_operations(_ar1, _ar2):
	rst = {
		'[Sum]       ': _ar1 + _ar2,
		'[Diff]      ': _ar1 - _ar2,
		'[Product]   ': _ar1 * _ar2,
		'[Quotient]  ': _ar1 / _ar2
						if _ar2 else f"{RED}{BOL}[Error]{RES} division by zero",
		'[Remainder] ': _ar1 % _ar2
						if _ar2 else f"{RED}{BOL}[Error]{RES} modulo by zero"}
	return rst

if not (arc == 3):
	sys.exit(
		f"{MAG}{BOL}[Operations]{RES} " +
		f"{RED}{BOL}[Failure]{RES} " +
		f"{YEL}{BOL}[Usage]{RES}   : {UND}python operation.py <number1> <number2>\n{RES}" + 
		f"{YEL}{BOL}            {RES} " +
		f"{RED}{BOL}         {RES} " +
		f"{YEL}{BOL}[Example]{RES} : {UND}python operations.py 10 3{RES}"
	)
else:
	try:
		nm1 = int(sys.argv[1])
		nm2 = int(sys.argv[2])
		rst = ft_operations(nm1, nm2)
		print(
			f"{MAG}{BOL}[Operations]{RES}",
			f"{GRE}{BOL}[Success]{RES}",
			f"informations"
			
		)
		for key, val in rst.items():
			print(
				f"{YEL}{BOL}            {RES}",
				f"{GRE}{BOL}         {RES}",
				f"{CYA}{BOL}{key:>9}{RES} : {BOL}{val}{RES}"
			)
	except ValueError as exc:
		sys.exit(
			f"{MAG}{BOL}[Operations]{RES} " +
			f"{RED}{BOL}[Failure]{RES} " +
			f"{YEL}{BOL}[AssertionError]{RES} : {UND}{exc}{RES}"
		)