import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
for i, a in enumerate(A):
    dic[a] = i

if dic[P] < dic[Q]:
    start = N-1
else:
    start = dic[Q]+1

B = A[start:]
bmax = max(B)
for ind in reversed(range(start)):
    a = A[ind]
    if bmax > a:
        