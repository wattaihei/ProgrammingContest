N = int(input())
D = list(map(int, input().split()))

T = [0 for _ in range(13)]

for d in D:
    if d > 12:
        T[24-d] += 1
    else:
        T[d] += 1

which = []
A = []
ans = -1
for i, t in enumerate(T):
    if t == 0:
        continue
    elif t == 1:
        which.append(i)
    elif t == 2:
        A.extend([i, 24-i])
    else:
        ans = 0
        break

def dfs(which, i, l, p):
    if i == len(which):
        p.append(l)
        return p
    t = which[i]
    p = dfs(which, i+1, l+[t], p)
    p = dfs(which, i+1, l+[24-t], p)
    return p

if ans == 0:
    print(0)
else:
    p = dfs(which, 0, [], [])
    #print(p)
    ans = 0
    for l in p:
        B = sorted(l+A)
        pre = 0
        tmp = 100
        for b in B:
            tmp = min(tmp, b-pre)
            pre = b
        tmp = min(tmp, 24-pre)
        ans = max(ans, tmp)
    print(ans)