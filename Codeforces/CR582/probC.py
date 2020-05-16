import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, M in Query:
    used = set()
    loop = []
    c = 0
    while True:
        c = (c+M)%10
        if c in used:
            break
        loop.append(c)
        used.add(c)
    
    times = N//M
    L = len(loop)
    ans = sum(loop)*(times//L) + sum(loop[:times%L])
    print(ans)