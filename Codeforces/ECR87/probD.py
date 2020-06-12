import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Query = list(map(int, input().split()))

Num = [0]*(N+1)
for a in A:
    Num[a] += 1

for n in Query:
    if n > 0:
        Num[n] += 1
    else:
        n *= 2
        l1 = 0
        l2 = math.pi/2
        while 