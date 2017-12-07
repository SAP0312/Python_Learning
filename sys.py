import sys
import re
count = int(sys.stdin.readline())
rex = re.compile(r'(?<!^)(#[0-9A-F]{6})|(?<!^)(#[0-9A-F]{3})', re.I)
for i in range(0,count):
    search = sys.stdin.readline()
    for j,k in rex.findall(search):
        print(j , k)