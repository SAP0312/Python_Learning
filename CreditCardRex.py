import sys
import re

count = int(sys.stdin.readline())
creditrex = re.compile(r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for i in range(0, count):
    number = sys.stdin.readline()
    print(creditrex.search(number))