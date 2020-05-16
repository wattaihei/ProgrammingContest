import sys
input = sys.stdin.readline


N, M, V, P = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
l = -1
r = N
while r - l > 1:
    m = (l+r)//2
    if m+1+P > N:
        r = m
        continue
    if V <= m+P:
        if A[m]+M >= A[-P]:
            r = m
        else:
            l = m
        continue
    if A[m]+M < A[-P]:
        l = m
        continue
    limit = A[m] + M
    can = 0
    for i in range(m+1, N-P+1):
        can += limit-A[i]
    if can >= (V-P-m)*M:
        r = m
    else:
        l = m

print(N-r)