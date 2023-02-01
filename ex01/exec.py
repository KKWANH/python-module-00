# importing
import sys

# getting paramter
strs = sys.argv

# main
if	len(strs) > 1:
	print(
		' '.join(
        	filter(
				None,
				[str.swapcase()[::-1] for str in strs[::-1][:-1]]
			)
		)
	)