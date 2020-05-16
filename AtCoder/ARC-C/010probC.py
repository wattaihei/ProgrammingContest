import sys
input = sys.stdin.readline

INF = 10**14

N, M, Y, Z = map(int, input().split())
col_to_num = {}
P = []
for i in range(M):
    s, str_p = map(str, input().rstrip().split())
    col_to_num[s] = i
    P.append(int(str_p))

Query = []
for s in input().rstrip():
    num = col_to_num[s]
    Query.append((num, P[num]))

ans = 0
Last = [0]*M
dp = [[-INF]*(1<<M) for _ in range(N+1)]
dp[0][0] = 0
ans = 0
for i, (num, point) in enumerate(Query):
    dp[i+1][0] = 0
    last = Last[num]
    for bit in range(1<<M):
        if last == 0:
            score = max(dp[i+1][bit|(1<<num)], dp[i][bit]+point)            
        else:
            score = max([dp[i+1][bit|(1<<num)], dp[i][bit]+point, dp[last][bit|(1<<num)]+point+Y])
        dp[i+1][bit|(1<<num)] = score
        if (bit|(1<<num)) == ((1<<M)-1):
            score += Z
        if score > ans:
            ans = score
    Last[num] = i+1

print(ans)