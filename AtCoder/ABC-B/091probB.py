from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

A = Counter(S)
B = Counter(T)

ans = 0
for k, v in A.items():
    if k in B.keys():
        v -= B[k]
    ans = max(v, ans)
print(ans)