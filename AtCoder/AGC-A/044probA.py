import sys
input = sys.stdin.readline
INF = 10**64

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, A, B, C, D in Query:
    # ans = INF
    P = {}
    def solve(n):
        # print(n)
        if n == 0:
            return INF
        if n in P:
            return P[n]
        if n == 1:
            return D
        S = n*D
        if n%2 == 0:
            S = min(S, solve(n//2)+A)
        else:
            S = min(S, solve(n//2)+A+D)
            S = min(S, solve((n+1)//2)+A+D)
        if n%3 == 0:
            S = min(S, solve(n//3)+B)
        else:
            S = min(S, solve(n//3)+B+D*(n%3))
            S = min(S, solve(n//3+1)+B+D*(3-n%3))
        if n%5 == 0:
            S = min(S, solve(n//5)+C)
        else:
            S = min(S, solve(n//5)+C+D*(n%5))
            S = min(S, solve(n//5+1)+C+D*(5-n%5))
        P[n] = S
        # print(n, P)
        return S
    # print(P)
    print(solve(N))