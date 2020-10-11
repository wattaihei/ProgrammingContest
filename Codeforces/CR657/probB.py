import sys
input = sys.stdin.readline

def solve(l, r, m):
    for a in range(l, r+1):
        p = m % a
        if m // a > 0 and p <= (r-l):
            return a, l+p, l
        q = a - p
        if q <= (r-l):
            return a, l, l+q

Q = int(input())
for _ in range(Q):
    l, r, m = map(int, input().split())
    print(*solve(l, r, m))