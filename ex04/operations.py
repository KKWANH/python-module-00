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
def operations(_ar1, _ar2):
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
		f"")