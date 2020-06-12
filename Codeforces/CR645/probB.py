import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    A.sort()
    ans = 1
    for i, a in enumerate(A):
        if i+1 >= a:
            ans = i+2
    print(ans)