# importing
import sys

# color code
RED = '\033[91m'
GRE = '\033[92m'
YEL = '\033[93m'
BLU = '\033[94m'
MAG = '\033[95m'
CYA = '\033[96m'
RES = '\033[0m'
BOL = '\033[1m'
UND = '\033[4m'

# parameter
arv = sys.argv
arc = len(arv) - 1

# main
if arc == 1:
    try:
        num = int(arv[1])
        msg = ""
        if not num:
            # in fact, 0 is even too.
            print(
                f"{GRE}{BOL}{UND}[Success]{RES}",
                f"the number is {CYA}{BOL}0{RES},",
                f"and also {MAG}{BOL}[EVEN]{RES}")
            sys.exit()
        if num % 2 == 0:
            msg = "[Even]"
        else:
            msg = "[Odd]"
        print(
            f"{GRE}{BOL}{UND}[Success]{RES}",
            f"the number is {CYA}{BOL}{num}{RES},",
            f"and also {MAG}{BOL}{msg}{RES}")
        sys.exit()

    except ValueError:
        print(
            f"{RED}{BOL}{UND}[Failure]{RES}",
            f"argument is {YEL}not an integer.{RES}")
        sys.exit()
elif not arc:
    sys.exit()
else:
    print(
        f"{RED}{BOL}{UND}[Failure]{RES}",
        f"{YEL}more than one arguments{RES} are provided.")
    sys.exit()
