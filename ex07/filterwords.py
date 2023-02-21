# --------------------------------------------------------------------------------
# : imports
import sys
import re

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
if len(sys.argv) == 3:
	if not sys.argv[2].isnumeric():
		print(
			f"{BLU}{BOL}{UND}[Filterwords]{RES}",
			f"{RED}{BOL}[Failure]{RES}",
			f"second input must be integer."
		)
		sys.exit()
	min = int(sys.argv[2])
	lst = re.sub(r'[^a-zA-Z\d\s]', '', sys.argv[1]).split()
	tst	= ['done', 'test']
	rst = [c for c in lst if len(c) > min]
	if rst:
		print(
			f"{BLU}{BOL}{UND}[Filterwords]{RES}",
			f"{RED}{BOL}[Success]{RES}",
			f"{rst}"
		)
	else:
		print(
			f"{BLU}{BOL}{UND}[Filterwords]{RES}",
			f"{RED}{BOL}[Failure]{RES}",
			f"words doesn't fit for the size {BOL}{min}{RES}"
		)
		sys.exit()
else:
	print(
		f"{BLU}{BOL}{UND}[Filterwords]{RES}",
		f"{RED}{BOL}[Failure]{RES}",
		f"input 3 arguments"
	)
	sys.exit()
