import sys
input = sys.stdin.readline

N = int(input())
a = 0
c = 1
for _ in range(N):
    r, b = map(str, input().split())
    if r == "+":
        a += int(b)
    elif r == "*":
        if int(b) > 0:
            c *= int(b)

print(a*c)