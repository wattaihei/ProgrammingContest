from math import log2

N, K = map(int, input().split())
A = list(map(int, input().split()))

Bits = [0 for _ in range(41)]
for i, a in enumerate(A):
    b = bin(a)[2:]
    for i in range(len(b)-1, -1, -1):
        Bits[len(b)-i-1] += int(b[i])

P = 0
for i in range(40, -1, -1):
    b = Bits[i]
    if b <= N-b and P + 2**i <= K:
        P += 2**i
#print(P)
ans = 0
for a in A:
    ans += P^a
print(ans)