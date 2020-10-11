import sys
input = sys.stdin.readline

Days = int(input())
C = list(map(int, input().split())) # 満足度低下
Ss = [list(map(int, input().split())) for _ in range(Days)]
# Ss[d][i]: d日目にiを開催したときの満足度
T = [int(input()) for _ in range(Days)] # 開催するコンテスト
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

INF = 10**18

def outputToScore(T):
    last = [0]*26
    used = [[] for _ in range(26)]
    satisfied = 0
    for d, t in enumerate(T):
        t -= 1; d += 1
        satisfied += Ss[d-1][t]
        used[t].append(d)
        last[t] = d
        for i, c in enumerate(C):
            satisfied -= c*(d-last[i])
        # print(satisfied)
    return satisfied, used

Satisfied, Used = outputToScore(T)
for d, aft in Query:
    aft -= 1
    bef = T[d-1]-1
    deltaSatis = Ss[d-1][aft] - Ss[d-1][bef]
    # d日目のコンテストをbefからaftに変える

    # bi-1 -> bi -> bi+1 を bi-1 -> bi+1
    befind = Used[bef].index(d)
    befday0 = 0 if befind == 0 else Used[bef][befind-1]
    befday2 = Days+1 if befind == len(Used[bef])-1 else Used[bef][befind+1]
    
    befd01 = d - befday0
    befd12 = befday2 - d
    befd02 = befday2-befday0
    deltaSatis -= C[bef]*(befd02*(befd02-1)//2) - C[bef]*(befd01*(befd01-1)//2 + befd12*(befd12-1)//2)

    # ai -> ai+1 を ai -> (insert) -> ai+1
    if len(Used[aft]) > 0:
        aftday0 = 0
        aftday2 = Days+1
        newaft = []
        for i,a in enumerate(Used[aft]):
            if a < d:
                aftday0 = a
            elif aftday2 == Days+1:
                newaft.append(d)
                aftday2 = a
            newaft.append(a)
        if aftday2 == Days+1:
            newaft.append(d)
        aftd01 = d - aftday0
        aftd12 = aftday2 - d
        aftd02 = aftd01 + aftd12
        deltaSatis += C[aft]*(aftd02*(aftd02-1)//2) - C[aft]*(aftd01*(aftd01-1)//2 + aftd12*(aftd12-1)//2)
    else:
        newaft = [d]
        d01 = d
        d12 = Days+1 - d
        deltaSatis += C[aft] * Days*(Days+1)//2 - C[aft]*(d01*(d01-1)//2 + d12*(d12-1)//2)

    Used[bef].remove(d)
    Used[aft] = newaft
    T[d-1] = aft+1
    Satisfied += deltaSatis
    print(Satisfied)

