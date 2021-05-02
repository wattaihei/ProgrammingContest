import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

M = 60
INF = 10**20

a0 = A[0]
a1 = A[1]
X = 0
for i in range(2,N):
    X ^= A[i]

s0 = a0+a1
select = []
for j in range(M):
    if X&(1<<j):
        s0 -= (1<<j)
        select.append(1<<j)

b0 = 0
for j in range(1,M):
    if s0&(1<<j) and not X&(1<<(j-1)):
        b0 |= 1<<(j-1)

ok = True
if s0 < 0 or sum(select) + 2*b0 != a0+a1:
    ok = False

S = select[::-1]
d = a0 - b0
for s in S:
    if d > s:
        d -= s

if d < 0 or d >= a0 or not ok:
    print(-1)
else:
    print(d)