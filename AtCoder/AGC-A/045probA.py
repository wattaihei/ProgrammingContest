import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    S = input().rstrip()
    Query.append((N, A, S))



def solve(N, A, S):
    Base = []
    for i in reversed(range(N)):
        s = S[i]
        a = A[i]
        if s == "0":
            for b in Base:
                a = min(a, a^b)
            if a:
                Base.append(a)
        else:
            for b in Base:
                a = min(a, a^b)
            if a:
                return False
                
    return True

for N, A, S in Query:
    print(0 if solve(N, A, S) else 1)