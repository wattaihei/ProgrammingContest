N = int(input())
TA = [list(map(int, input().split())) for _ in range(N)]

pa = 1
pt = 1
for t, a in TA:
    k = max(pt//t, pa//a)
    if a*k < pa or t*k < pt:
        k += 1
    pa = a*k
    pt = t*k

print(pa+pt)