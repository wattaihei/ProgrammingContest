import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

D = [0]*M
s = 0
ans = []
for i, a in enumerate(A):
    D[i%M] += a
    s += D[i%M]
    ans.append(s)

print(" ".join([str(a) for a in ans]))