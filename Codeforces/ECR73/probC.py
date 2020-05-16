Q = int(input())
data = []
for _ in range(Q):
    c, m, x = map(int, input().split())
    data.append([c, m, x])

for c, m, x in data:
    if c < m:
        if (m+x)//2 < c:
            ans = (m+x+c)//3
        else:
            ans = c
    else:
        if (c+x)//2 < m:
            ans = (m+x+c)//3
        else:
            ans = m
    print(ans)
