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
# : global variable : morse code
_mores = {
	"A":	".-",
	"B":	"-...",
	"C":	"-.-.",
	"D":	"-..",
	"E":	".",
	"F":	"..-.",
	"G":	"--.",
	"H":	"....",
	"I":	"..",
	"J":	".---",
	"K":	"-.-",
	"L":	".-..",
	"M":	"--",
	"N":	"-.",
	"O":	"---",
	"P":	".--.",
	"Q":	"--.-",
	"R":	".-.",
	"S":	"...",
	"T":	"-",
	"U":	"..-",
	"V":	"...-",
	"W":	".--",
	"X":	"-..-",
	"Y":	"-.--",
	"Z":	"--..",
	"0":	"-----",
	"1":	".----",
	"2":	"..---",
	"3":	"...--",
	"4":	"....-",
	"5":	".....",
	"6":	"-....",
	"7":	"--...",
	"8":	"---..",
	"9":	"----.",
	" ":	"/",
}

# --------------------------------------------------------------------------------
# : main
arc = len(sys.argv)
if arc >= 2:
	str = ' '.join(sys.argv[1:])
	if re.search(r'[^a-zA-Z\d\s]', str):
		sys.exit('Error')
	for chr in str:
		print(
			_mores[chr.upper()],
			end=' ')
	print()
