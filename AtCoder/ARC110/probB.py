import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())

T = "110"

ans = 0
for t in range(3):
    ok = True
    for i, s in enumerate(S):
        if T[(i+t)%3] != s:
            ok = False
            break
    if ok:
        ans += 10**10 - (N+t+2)//3 + 1
print(ans)