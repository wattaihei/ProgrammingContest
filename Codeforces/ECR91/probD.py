import sys
input = sys.stdin.readline

N, M = map(int, input().split())
X, K, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def score(T, bmax):
    L = len(T)
    if L == 0:
        return 0
    tmax = max(T)
    if L < K:
        if tmax > bmax:
            return -1
        return L*Y
    else:
        if K*Y >= X:
            return (L//K)*X + (L%K)*Y
        elif tmax > bmax:
            return X + (L-K)*Y
        else:
            return L*Y

bind = 0
T = []
ans = 0
for a in A:
    if bind < M and B[bind] == a:
        bmax = B[bind]
        if bind > 0:
            bmax = max(B[bind-1], bmax)
        res = score(T, bmax)
        if res == -1:
            ans = -1
            break
        ans += res
        bind += 1
        T = []
        continue
    T.append(a)

if bind != M:
    ans = -1
else:
    res = score(T, B[M-1])
    if res == -1:
        ans = -1
    else:
        ans += res

print(ans)