import sys
input = sys.stdin.readline

S = input().rstrip()

tmp = 200
for s in S:
    if ord(s) > tmp:
        print("Ann")
    else:
        print("Mike")
    tmp = min(tmp, ord(s))