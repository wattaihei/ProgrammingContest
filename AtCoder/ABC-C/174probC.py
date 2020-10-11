import sys
input = sys.stdin.readline

K = int(input())

A = [-1]*(K+1)

ans = -1
t = 7 % K
for s in range(K+1):
    if t == 0:
        ans = s + 1
        break
    if A[t] != -1:
        break
    A[t] = 1
    t = (t*10 + 7) % K

print(ans)