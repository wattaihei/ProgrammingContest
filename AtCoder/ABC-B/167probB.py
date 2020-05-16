import sys
input = sys.stdin.readline

A, B, C, K = map(int, input().split())
if A >= K:
    ans = K
elif A+B >= K:
    ans = A
else:
    rem = K-(A+B)
    ans = A-rem
print(ans)