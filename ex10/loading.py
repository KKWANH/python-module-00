# --------------------------------------------------------------------------------
# : imports
from sys import exit
from os import get_terminal_size
from time import time, sleep

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
# : ft_progress
def ft_progress(lst: range):
	col = get_terminal_size().columns - 60
	stt = time()
	end = lst.stop - lst.start
	new = range(0, end, lst.step)

	if col < 0:
		print(
			f"{BLU}{BOL}{UND}[Loading]{RES}",
			f"{RED}{BOL}[Failure]{RES}",
			f"The terminal is too small.")
		exit()

	for idx in new:
		elp = time() - stt
		per = (abs(idx) + 1) / abs(end)

		eta = (((elp / (per * 100)) * 100) - elp)
		print(
			f"{BLU}{BOL}ETA{RES}: {BOL}{eta:5.2f}s{RES}",
			f"{YEL}[{(per * 100):3.0f}%]{RES}",
			f"[{('=' * round(per * (col))) + '>':{col}.{col}}]",
			f"{abs(idx) + 1}/{abs(end)} | elapsed time {elp:.2f}s",
			end='\r')
		yield idx

# --------------------------------------------------------------------------------
# : main
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)