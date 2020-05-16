N = int(input())
S = input()

T1 = S[:N]
T2 = S[N:][::-1]

def window(i, P, L):
    if i == N:
        L.append(P)
        return L
    L = window(i+1, P+[0], L)
    L = window(i+1, P+[1], L)
    return L

L = window(0, [], [])
dic1 = {}
dic2 = {}
for mask in L:
    k1 = ''
    k2 = ''
    r1 = ''
    r2 = ''
    for i in range(N):
        if mask[i]:
            k1 += T1[i]
            k2 += T2[i]
        else:
            r1 += T1[i]
            r2 += T2[i]
    c1 = k1 + '_' + r1
    c2 = k2 + '_' + r2
    if not c1 in dic1.keys():
        dic1[c1] = 1
    else:
        dic1[c1] += 1
    if not c2 in dic2.keys():
        dic2[c2] = 1
    else:
        dic2[c2] += 1

ans = 0
for k1, v1 in dic1.items():
    if k1 in dic2.keys():
        ans += dic2[k1]*v1
print(ans)