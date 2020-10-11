import sys
input = sys.stdin.readline

MAX = 3*10**5+1

H, W, M = map(int, input().split())

A = [set() for _ in range(MAX)]
B = [set() for _ in range(MAX)]
for _ in range(M):
    h, w = map(int, input().split())
    A[h].add(w)
    B[w].add(h)

B.sort(key=lambda x : len(x), reverse=True)
L = len(B[0])
P = []
for b in B:
    if len(b) == L:
        P.append(b)

ans = 0
for h in range(MAX):
    score = len(A[h]) + L - 1
    for p in P:
        if not h in p:
            score += 1
            break
    ans = max(ans, score)

print(ans)