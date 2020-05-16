import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())

dic = {}
for i, s in enumerate(S):
    if s in dic:
        dic[s].append(i)
    else:
        dic[s] = [i]

Alp = [chr(i) for i in range(97, 97+26)]
Ind = []
for s in Alp:
    if s in dic:
        for ind in dic[s]:
            Ind.append(ind)

P = [None]*N
for i, ind in enumerate(Ind):
    P[ind] = i

maxInd = [0]
for ind in Ind:
    maxInd.append(max(maxInd[-1], ind))

maxP = [0]
for p in P:
    maxP.append(max(maxP[-1], p))

ans = [-1]*N
l = 0
ok = True
while l < N:
    num = P[l]
    while True:
        r = maxInd[num]
        newn = maxP[r+1]
        if num >= newn:
            break
        num = newn
    if r <= l:
        ans[l] = 0
        l += 1
        continue
    L1 = []
    R1 = []
    for i in range(l, r+1):
        if P[i] >= num:
            L1.append(i)
        else:
            R1.append(i)
    pre = -1
    for l1 in L1:
        if P[l1] < pre:
            ok = False
        ans[l1] = 0
        pre = P[l1]
    pre = -1
    for r1 in R1:
        if P[r1] < pre:
            ok = False
        ans[r1] = 1
        pre = P[r1]
    if not ok:
        break
    l = r+1
if ok:
    print("YES")
    print(*ans, sep="")
else:
    print("NO")