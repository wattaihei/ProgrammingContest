import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))


ans = [-1]*N
for n, a in enumerate(A):
    if ans[n] != -1: continue
    t = n
    L = [t]
    while True:
        t = A[t] - 1
        if t == n:
            break
        L.append(t)
    for l in L:
        ans[l] = len(L)

print(*ans)