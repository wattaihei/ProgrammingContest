import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

A = [0]
for s in S:
    a = 1 if s == "(" else -1
    A.append(A[-1]+a)

isOK = True
ans = 0
last0 = 0
for i, a in enumerate(A):
    if a == 0:
        if not isOK:
            ans += i - last0
        last0 = i
        isOK = True
    if a < 0:
        isOK = False
if A[-1] != 0:
    print(-1)
else:
    print(ans)