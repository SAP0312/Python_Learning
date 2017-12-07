import sys
import re

code = sys.stdin.readline()
postalgrex = re.compile(r'^'
                        r'(?:(\d)(\d\1))'
                        r'[1-9]'
                        r'\d{5}')
if postalgrex.search(code) == None:
        sys.stdout.write('False\n')
else:
        sys.stdout.write('True\n')