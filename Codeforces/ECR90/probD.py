import sys
input = sys.stdin.buffer.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))


def solve(A, ans):
    nowmin = 0
    w = 0
    for p1 in A:
        w += p1
        nowmin = min(nowmin, w)
        ans = max(ans, T + w - nowmin)
    return ans


for N, A in Query:
    T = 0
    P1 = []
    P2 = []
    for i in range((N-1)//2+1):
        T += A[2*i]
        if 2*i+1 <= N-1:
            d = A[2*i+1] - A[2*i]
            P1.append(d)
        if 0 <= 2*i-1:
            d = A[2*i-1] - A[2*i]
            P2.append(d)
    
    ans = solve(P1, T)
    ans = solve(P2, ans)
    print(ans)
