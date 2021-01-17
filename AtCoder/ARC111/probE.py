import sys
input = sys.stdin.buffer.readline

def solve():
    a, b, c, d = map(int, input().rstrip().split())
    ok = 0
    ng = 10**10
    while (ng-ok) > 1:
        m = (ok+ng)//2
        a0 = a + b*m
        a1 = a + c*m
        if a0//d != a1//d or a0%d == 0:
            ng = m
        else:
            ok = m
    print(ok+1)


Q = int(input())
for _ in range(Q):
    solve()