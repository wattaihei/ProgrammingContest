from collections import Counter

M, N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for m in range(1, M+1):
    B = []
    for a in A:
        B.append(abs(a-m))
    C = Counter(B)
    c = 0
    for k, v in C.items():
        if k == 0:
            c += v
        elif k <= K:
            c += 1
    ans = max(ans, c)

print(ans)