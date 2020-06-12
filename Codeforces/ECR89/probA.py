import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b in Query:
    ans = 0
    if a > b:
        d = a - b
        c= min(d, b)
        a -= 2*c
        b -= c
        ans += c
    else:
        d = b - a
        c = min(d, a)
        a -= c
        b -= 2*c
        ans += c
    p = min(a, b)
    ans += (p//3)*2
    if p % 3 > 0 and max(a, b) % 3 > 1:
        ans += 1
    print(ans)