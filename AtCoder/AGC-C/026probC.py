# その3
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

N = int(input())
S = input()

dic = {}
for i in range(2*N):
    s = S[i]
    if not s in dic.keys():
        dic[s] = [i]
    else:
        dic[s].append(i)

INDs = []
INVs = []
ok = True
for alp, L in dic.items():
    l = len(L)
    if l % 2 != 0:
        ok = False
        break
    for i in range(l//2):
        INVs.append(L[l-1-i])
        INDs.append(L[i])

INVs.sort(reverse=True)
for i in reversed(range(N)):
    if S[INVs[i]] == S[INVs[-1]]:
        samepoint = i
    else:
        break

def window(i, P, L):
    if i == N:
        L.append(P)
        return L
    L = window(i+1, P+[0], L)
    L = window(i+1, P+[1], L)
    return L


if not ok:
    print(0)
else:
    ans = 0
    L = window(0, [], [])
    for mask in L:
        ok = True
        j = 0
        C = {}
        for k, l in dic.items():
            C[k] = 0
        decided_color = [-1]*N
        rb = [0, 0]
        for i in range(N):
            l_ind = INDs[i]
            color = mask[i]
            rb[color] += 1
            if dic[S[l_ind]][C[S[l_ind]]] > j:
                if decided_color[dic[S[l_ind]][C[S[l_ind]]]] == color:
                    ok = False
                    break
            elif j == N:
                ok = False
                break
            else:
                r_ind = INVs[j]
                while S[l_ind] != S[r_ind]:
                    decided_color[j] = color
                    C[S[r_ind]] += 1
                    rb[color] += 1
                    j += 1
                    if j == N:
                        break
                    r_ind = INVs[j]
                if S[l_ind] == S[INVs[samepoint]] and j == samepoint:
                    continue
                else:
                    decided_color[j] = color^1
                    rb[color^1] += 1
                    j += 1
        if not ok:
            continue
        else:
            r = N - rb[0]
            b = N - rb[1]
            if r < 0 or b < 0:
                continue
            elif r+b == 0:
                ans += 1
            else:
                ans += cmb(r+b, r)
    print(ans)



