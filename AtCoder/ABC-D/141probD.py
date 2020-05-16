from math import log2

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

B = []
for a in A:
    B.append(int(log2(a)))

a = 0
for i, b in enumerate(B):
    if i == 0:
        pre = b
        continue
    a += (pre-b)*i
    if a >= M:
        min_rem = b
        break

C = []
change = 0
for i in range(N):
    c = B[i]-min_rem
    if change + c <= M:
        C.append(c)
        change += c
    

ans = 0
for i, a in enumerate(A):
    ans += a//(2**B[i])