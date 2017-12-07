import sys
import re

postalcode = int(sys.stdin.readline())
starttagrex = re.compile(r'(<[a-z]+>)(</[a-z]+)(<[a-z]+\s/>)')

if starttagrex.search(postalcode) == None:
    sys.stdout.write('NO\n')
else:
    sys.stdout.write('YES\n')


