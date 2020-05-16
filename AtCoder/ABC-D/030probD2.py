import sys
input = sys.stdin.readline

N, a = map(int, input().split())
K = input().rstrip()
B = [0] + list(map(int, input().split()))

seq = [-1]*(N+1)
b = a
for c in range(1, N+2):
    b = B[b]
    if seq[b] > 0:
        cycle = c - seq[b]
        break
    seq[b] = c

def solve(start, cycle):
    L = len(K)
    digit = 1
    p = 0
    for l in range(L):
        n = int(K[-l-1])
        p += n*digit % cycle
        p %= cycle
        digit = digit*10 % cycle
    while p < start:
        p += cycle
    d = a
    for _ in range(p):
        d = B[d]
    return d

if len(K) <= 18:
    k = int(K)
    if seq[b] >= k:
        d = a
        for _ in range(k):
            d = B[d]
    else:
        d = solve(seq[b], cycle)
else:
    d = solve(seq[b], cycle)

print(d)