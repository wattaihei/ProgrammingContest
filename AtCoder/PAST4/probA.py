import sys
input = sys.stdin.buffer.readline

A = list(map(int, input().rstrip().split()))

P = []
for i, a in enumerate(A):
    P.append((a, i))

P.sort()

I = "ABC"
ind = P[1][1]
print(I[ind])