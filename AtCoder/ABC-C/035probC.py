N, Q = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(Q)]

A = [0 for _ in range(N+1)]

for l, r in LR:
    A[l-1] += 1
    A[r] += 1

B = []
k = 0
for a in A:
    k = (k+a)%2
    B.append(k)
B.pop()
print(''.join([str(b) for b in B]))