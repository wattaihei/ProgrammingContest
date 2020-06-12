import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]

Par = [~i for i in range(N)] # コンテナiの親
Table = [i for i in range(N)] # table i の一番上のコンテナ

for f, t, x in Query:
    x -= 1; f -= 1; t -= 1
    par = Par[x]
    nowtop = Table[f]
    gotop = Table[t]
    
    Table[f] = par
    Table[t] = nowtop
    Par[x] = gotop

ans = [0]*N
for table in range(N):
    cont = Table[table]
    while cont >= 0:
        ans[cont] = table+1
        cont = Par[cont]

print(*ans, sep="\n")