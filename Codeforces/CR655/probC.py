import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    ind1 = 0
    while ind1 < N and A[ind1] == ind1+1:
        ind1 += 1
    ind2 = N-1
    while ind2 >= 0 and A[ind2] == ind2+1:
        ind2 -= 1
    if ind1 == N:
        ans = 0
    else:
        p = False
        for i in range(ind1, ind2+1):
            if A[i] == i+1:
                p = True
        if p:
            ans = 2
        else:
            ans = 1
    print(ans)