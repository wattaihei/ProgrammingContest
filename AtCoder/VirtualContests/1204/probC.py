C, D = map(int, input().split())
l = 140
r = 170

ans = 0
while True:
    if D <= l: break
    ans += max(min(r, D) - max(l, C), 0)
    l *= 2
    r *= 2
print(ans)