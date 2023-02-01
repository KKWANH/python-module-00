# importing
import sys
from collections import Counter

# parameter
arv = sys.argv
arc = len(arv)

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


def text_analyzer(_txt=None):
    '''
    This functions prints informations about input text.
    You can only input a string.
    The types of characters that you can give:
      - upper case
      - lower case
      - punctuation
      - spaces
    '''
    if not _txt:
        _txt = input(
                f"{YEL}{BOL}{UND}[Input]{RES}   " +
                f"Input text to analyze.\n" +
                f"          : {CYA}")
        print(f"{RES}", end='')
    if isinstance(_txt, str):
        info = Counter(
            "l" if c.islower() else
            "u" if c.isupper() else
            "s" if c.isspace() else
            "p" if not c.isdigit() else
            "other" for c in _txt)
        print(
            f"{GRE}{BOL}{UND}[Info]{RES}   ",
            f"The text contains {CYA}{BOL}{len(_txt)}{RES} character(s):")
        print(
            "",
            f"         - {YEL}{BOL}{UND}{info['u']}{RES} upper letter(s)\n",
            f"         - {YEL}{BOL}{UND}{info['l']}{RES} lower letter(s)\n",
            f"         - {YEL}{BOL}{UND}{info['p']}{RES} punctuation(s)\n",
            f"         - {YEL}{BOL}{UND}{info['s']}{RES} space(s)")
    else:
        print(
            f"{RED}{BOL}{UND}[Failure]{RES}",
            f"argument is {YEL}not a string{RES}",
            file=sys.stderr)


if __name__ == "__main__":
    if arc == 1:
        text_analyzer()
    elif arc == 2:
        text_analyzer(arv[1])
    else:
        print(
            f"{RED}{BOL}{UND}[Failure]{RES}",
            f"{YEL}more than one arguments{RES} are provided.",
            file=sys.stderr)
