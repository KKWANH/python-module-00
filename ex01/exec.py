# --------------------------------------------------------------------------------
# : import
import sys

# --------------------------------------------------------------------------------
# : getting paramter
arv = sys.argv

# --------------------------------------------------------------------------------
# : main
if len(arv) > 1:
	print(
		' '.join(arv[1:])[::-1].swapcase())
