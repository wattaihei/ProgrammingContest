import sys
input = sys.stdin.readline

N, M = map(int, input().split()) 
A = list(map(int, input().split()))

seg = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

B = {}
for a in A:
    ind = seg[a]
    if not ind in B.keys():
        B[ind] = a
    else:
        if B[ind] < a:
            B[ind] = a

I = sorted(list(B.keys()))
#print(I)
Ap = []
def search(ind, remain, ret, l, maxl):
    if ind >= len(I):
        return False, ret, l
    #print(I[ind], remain, ret)
    a = I[ind]
    p = remain // a
    r = remain % a 
    if p == 0:
        return False, ret, l
    if r == 0:
        ret.append((a, p))
        l += p
        return True, ret, l
    for q in range(p-1, -1, -1):
        nowl = l
        r += a
        oldr = ret[:]
        ok, newr, newl = search(ind+1, r, oldr, nowl, maxl)
        if ok:
            newl += q
            newr.append((a, q))
            if ind == 0:
                if newl >= maxl:
                    maxl = newl
                    Ap.append(newr)
                continue
            return True, newr, newl
    if ind == 0:
        return False, Ap, l
    return False, ret, l

def main():

    only, Ls, l = search(0, N, [], 0, 0)
    #print(Ls)
    if only:
        Q = []
        for k, v in Ls:
            Q.extend([B[k]]*v)
        Q.sort(reverse=True)
        print(''.join([str(q) for q in Q]))
    else:
        anss = []
        for i, L in enumerate(Ls):
            P = []
            for k, v in L:
                P.append((B[k], v))
            P.sort(reverse=True)
            if i == 0:
                maxp = P[0][1]
            elif P[0][1] >= maxp:
                maxp = P[0][1]
            else:
                continue
            Q = ''
            for p, v in P:
                Q = Q + str(p)*v
            num = int(Q)
            anss.append(num)

        print(max(anss))

if __name__ == "__main__":
    main()