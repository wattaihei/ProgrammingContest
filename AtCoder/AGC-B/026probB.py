import sys
input = sys.stdin.readline
from fractions import gcd

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

def solve(A, B, C, D):
    if A < B or D < B:
        return False
    if C < B-1:
        if D%B != 0:
            cycle = gcd(D, B)
            if C < B-cycle:
                return False
            if A%cycle < (C+1)%cycle:
                return True
            else:
                return False
        else:
            if A%B <= C:
                return True
            else:
                return False
    else:
        return True

for A, B, C, D in Query:
    ans = "Yes" if solve(A, B, C, D) else "No"
    print(ans)