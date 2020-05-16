import sys
input = sys.stdin.readline

N, Z = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

l = 0
r = N//2+1
while r - l > 1:
    m = (l+r)//2
    ok = True
    for i in range(m):
        if A[i+N-m] - A[i] < Z:
            ok = False
    if ok:
        l = m
    else:
        r = m
print(l)