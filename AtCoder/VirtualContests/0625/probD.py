import sys
input = sys.stdin.readline

N, P = map(int, input().split())
S = list(input().rstrip())

if P in {2, 5}:
    ans = 0
    for i, s in enumerate(S):
        if int(s) % P == 0:
            ans += i+1
else:
    ans = 0
    T = [0]*P
    T[0] = 1
    tmp = 0
    k = 1
    for s in reversed(S):
        tmp = (tmp + k * int(s)) % P
        k = k * 10 % P
        ans += T[tmp]
        T[tmp] += 1

print(ans)