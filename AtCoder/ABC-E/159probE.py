import sys
input = sys.stdin.readline
INF = 10**16

H, W, K = map(int, input().split())
state = [list(map(int, list(input().rstrip()))) for _ in range(H)]

ans = INF
for bit in range(1<<(H-1)):
    zones = []
    tmp = [0]
    for h in range(H-1):
        if bit&(1<<h):
            zones.append(tmp)
            tmp = [h+1]
        else:
            tmp.append(h+1)
    zones.append(tmp)
    L = len(zones)
    Scores = [0]*L
    tmp_point = L-1
    for w in range(W):
        out = False
        C = []
        for l, z in enumerate(zones):
            p = 0
            for i in z:
                if state[i][w]:
                    p += 1
            C.append(p)
            if p + Scores[l] > K:
                out = True
            Scores[l] += p
        if max(C) > K:
            tmp_point = INF
            break
        if out:
            tmp_point += 1
            Scores = C[:]
    if tmp_point < ans:
        ans = tmp_point

print(ans)