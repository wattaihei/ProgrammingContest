import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
mod = 10**9+7

decided = [False for _ in range(N)]
H = [0 for _ in range(N)]

pre = -1
for i, t in enumerate(T):
    if t != pre:
        decided[i] = True
    H[i] = t
    pre = t

ok = True
pre = -1
for i in reversed(range(N)):
    a = A[i]
    if a != pre:
        if decided[i] and H[i] != a:
            ok = False
            break
        decided[i] = True
    elif decided[i]:
        if H[i] > a:
            ok = False
            break
    if not decided[i]:
        H[i] = min(H[i], a)
    pre = a

if ok:
    ans = 1
    for i in range(N):
        if not decided[i]:
            ans = ans * H[i] % mod
    print(ans)
else:
    print(0)