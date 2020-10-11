import sys
input = sys.stdin.buffer.readline

mod = 10**9+7

T = int(input())
Query = [list(map(int, input().split())) for _ in range(T)]

for n, ag, bg, ac, bc, ap, bp in Query:
    pg = ag * pow(bg, mod-2, mod) % mod
    pc = ac * pow(bc, mod-2, mod) % mod
    pp = ap * pow(bp, mod-2, mod) % mod
    p1 = pow(pg+pc, n, mod) - pow(pg, n, mod) - pow(pc, n, mod)
    p2 = pow(pc+pp, n, mod) - pow(pc, n, mod) - pow(pp, n, mod)
    p3 = pow(pp+pg, n, mod) - pow(pp, n, mod) - pow(pg, n, mod)
    print((1 - p1 - p2 - p3 ) % mod)