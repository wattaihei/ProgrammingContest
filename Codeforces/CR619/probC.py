import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, M in Query:
    Z = N - M
    s = M+1
    m1 = Z//s
    m2 = m1+1
    ans = N*(N+1)//2 - m1*(m1+1)//2*(s-Z%s) - m2*(m2+1)//2*(Z%s)
    print(ans)