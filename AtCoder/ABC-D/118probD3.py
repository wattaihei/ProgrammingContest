import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

COUNT = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dic = {}
for a in A:
    dic[COUNT[a]] = a

C = sorted(dic.keys(), key=lambda x: -dic[x])
min_c = min(C)
C.remove(min_c)
#print(C)

def dfs(remain, l, now, L):
    #print(remain, l, now)
    if remain == 0:
        L.append(now)
        return L
    if l == len(C):
        return L
    loop = remain//(C[l]-min_c)
    for h in reversed(range(loop+1)):
        L = dfs(remain-(C[l]-min_c)*h, l+1, now+[dic[C[l]]]*h, L)
    return L


k = 0
while True:
    r = N%min_c + k*min_c
    p = N//min_c - k
    if r == 0:
        ans = {dic[min_c]: p}
        break
    L = dfs(r, 0, [], [])
    #print(L)
    ans = []
    for now in L:
        l = len(now)
        if l > p: continue
        P = sorted(now+[dic[min_c]]*(p-l), reverse=True)
        #print(P)
        if not ans:
            ans = P
            continue
        ok = True
        for i in range(p):
            if P[i] < ans[i]:
                ok = False
                break
            elif P[i] > ans[i]:
                ok = True
                break
        if ok:
            ans = P

    if ans: break
    k += 1

ans.sort(reverse=True)
print("".join([str(a) for a in ans]))