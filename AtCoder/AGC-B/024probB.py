import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

ind = [None]*N
for i, a in enumerate(A):
    ind[a-1] = i

p = 0
pre = -1
k = 0
for i in ind:
    if i > pre:
        k += 1
    else:
        k = 1
    p = max(p, k)
    pre = i

print(N-p)