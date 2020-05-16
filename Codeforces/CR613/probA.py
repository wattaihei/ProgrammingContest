import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

l = 0
r = 0
for s in S:
    if s == "L":
        l -= 1
    else:
        r += 1
print(r-l+1)