N, K = map(int, input().split())
S = list(input())

c = 0
p = 0
for i, s in enumerate(S):
    if i == 0:
        pres = s
        continue
    elif s != pres:
        c += 1
    else:
        p += 1
    pres = s

if c == 0 or c == 1 or c <= 2*K:
    ans = N-1
else:
    ans = p+2*K
print(ans)