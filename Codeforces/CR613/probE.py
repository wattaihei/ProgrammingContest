import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, LR))

for N, LR in Query:
    Prob = set()
    for l, r in LR:
        Prob.add(2*l)
        Prob.add(2*r+1)
    ind_to_co = sorted(list(Prob))
    co_to_ind = {}
    for i, co in enumerate(ind_to_co):
        co_to_ind[co] = i
    
    K = len(ind_to_co)
    E = [0]*(K+1)
    for l, r in LR:
        E[co_to_ind[2*l]] += 1
        E[co_to_ind[2*r+1]] -= 1
    
    F = []
    Tmp = 0
    for k in range(K):
        if E[k] == 1:
            F.append(k)
        E[k+1] += E[k]
        if E[k] > 0 and E[k+1] == 0:
            Tmp += 1

    GL = [0]*(K+1)
    GR = [0]*(K+1)
    pre = K-1
    for f in F:
        if f != pre + 1:
            GL[f] += 1
            GR[pre+1] += 1
        pre = f
    GR[pre+1] += 1

    for k in range(K):
        GR[k+1] += GR[k]
        GL[k+1] += GL[k]
    
    ans = Tmp
    for l, r in LR:
        cover = GR[co_to_ind[2*r+1]] - GL[co_to_ind[2*l]]
        ans = max(ans, Tmp+cover)
    
    print(ans)