import sys
input = sys.stdin.readline

INF = 10**9

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for h, c, t in Query:
    if 2*t <= h+c:
        ans = 2
    else:
        l = 0
        r = INF
        while r - l > 1:
            m = (l+r)//2
            if (h+c)*m+h > (2*m+1)*t:
                l = m
            else:
                r = m
        if 2*t*(2*r+1)*(2*l+1) - ((h+c)*r+h)*(2*l+1) >= ((h+c)*l+h)*(2*r+1):
            ans = 2*l+1
        else:
            ans = 2*r+1
    print(ans)