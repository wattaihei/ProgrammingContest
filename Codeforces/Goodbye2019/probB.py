import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    ans = []
    for i in range(N-1):
        if abs(A[i]-A[i+1]) > 1:
            ans = [i+1, i+2]
    if ans:
        print("YES")
        print(*ans)
    else:
        print("NO")