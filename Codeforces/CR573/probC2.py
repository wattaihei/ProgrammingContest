n, m, k = map(int, input().split()) # 横に2個
p = list(map(int, input().split()))

plist = []
for pp in p:
    plist.append([pp, pp//k, pp%k])

delta = 0
page = 0
c = 0
ans = 0
i = 0
while i < m:
    pp = p[i] - delta
    if (pp - 1) // k == page:
        c += 1
        i += 1
    elif c != 0:
        ans += 1
        delta += c
        c = 0
    page = (pp - 1) // k

if c != 0:
    ans += 1

print(ans)