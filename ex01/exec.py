# importing
import sys

# getting paramter
arv = sys.argv

# main
if len(arv) > 1:
    print(
        ' '.join(
            filter(
                None,
                [str.swapcase()[::-1] for str in arv[::-1][:-1]]
            )
        )
    )
