import sys
input = sys.stdin.readline

Days = int(input())
C = list(map(int, input().split())) # 満足度低下
Ss = [list(map(int, input().split())) for _ in range(Days)]
# Ss[d][i]: d日目にiを開催したときの満足度
T = [int(input()) for _ in range(Days)] # 開催するコンテスト

last = [0]*26

satisfied = 0
for d, t in enumerate(T):
    t -= 1; d += 1
    satisfied += Ss[d-1][t]
    last[t] = d
    for i, c in enumerate(C):
        satisfied -= c*(d-last[i])
    print(satisfied)