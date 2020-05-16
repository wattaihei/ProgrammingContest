import sys
input = sys.stdin.readline
from fractions import gcd

Q = int(input())
Query = []
for _ in range(Q):
    a, b, q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(q)]
    Query.append((a, b, q, LR))


def solve(lcm, m, x):
    cycle = x//lcm
    amari = x%lcm
    return (lcm-m)*cycle + max(0, amari-m+1)

for a, b, q, LR in Query:
    lcm = a*b//gcd(a,b)
    m = max(a, b)
    ans = []
    for l, r in LR:
        ans.append(solve(lcm, m, r)-solve(lcm, m, l-1))
    print(*ans)