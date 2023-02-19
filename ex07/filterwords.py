import sys
import re

if len(sys.argv) == 3:
    if not sys.argv[2].isnumeric():
        sys.exit('Error')
    min_len = int(sys.argv[2])
    new_lst = re.sub(r'[^a-zA-Z\d\s]', '', sys.argv[1]).split()
    tst		= ['done', 'test']
    print([c for c in new_list if len(c) > minLen])
else:
    sys.exit('Error')
