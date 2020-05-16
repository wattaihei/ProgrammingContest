import sys
input = sys.stdin.readline

N, M = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(N)]

l = 0
r = N+1

while r - l > 1:
    m = (l+r)//2
    ok = True
    canuse = [True]*(M+1)
    pri = [0]*N
    while ok:
        sport = [0]*(M+1)
        for i in range(N):
            while not canuse[state[i][pri[i]]]:
                pri[i] += 1
                if pri[i] > M-1:
                    ok = False
                    break
            if not ok:
                break
            sport[state[i][pri[i]]] += 1
        update = False
        for j in range(1, M+1):
            if sport[j] > m:
                update = True
                canuse[j] = False
        if not update:
            break
    
    if ok:
        r = m
    else:
        l = m
                
    
print(r)