import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, G, B in Query:
    border = (N+1)//2
    p = border//G
    q = border%G
    if q == 0: 
        p -= 1
        q += G
    ans = p*(G+B) + q
    print(max(ans, N))