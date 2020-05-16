K, N = map(int, input().split())
S = [list(map(str, input().split())) for _ in range(N)]

def show(i, l, L):
    if i == K:
        L.append(l)
        return L
    for k in range(1, 4):
        L = show(i+1, l+[k], L)
    return L

Ls = show(0, [], [])
for L in Ls:
    dic = {}
    ok = True
    for nums, ss in S:
        l = 0
        for num in nums:
            n = int(num)-1
            l += L[n]
        if l == len(ss):
            i = 0
            for num in nums:
                n = int(num)-1
                if not n in dic.keys():
                    dic[n] = ss[i:i+L[n]]
                    i += L[n]
                else:
                    if ss[i:i+L[n]] != dic[n]:
                        ok = False
                    else:
                        i += L[n]
        else:
            ok = False
        if not ok: break
    if ok: break

for k in range(K):
    print(dic[k])