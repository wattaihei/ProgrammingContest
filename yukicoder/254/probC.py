import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Query = [int(input()) for _ in range(Q)]


D = [-1]*N

P = []
x = 0
j = 0
while D[x%N] == -1:
    D[x%N] = j
    P.append(x)
    x = (x + A[x%N])
    j += 1

cycle = j - D[x%N]
init = D[x%N]
cyclesum = x - P[D[x%N]]

for K in Query:
    if K < init:
        ans = P[K]
    else:
        ans = P[(K-init)%cycle+init] + ((K-init)//cycle)*cyclesum
    print(ans)