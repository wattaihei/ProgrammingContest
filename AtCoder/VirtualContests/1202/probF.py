import sys
input = sys.stdin.readline

N, M = map(int, input().split())
LRS = [list(map(int, input().split())) for _ in range(N)]

score = [0]*(M+2)
for l, r, s in LRS:
    score[0] += s
    score[l] -= s
    score[r+1] += s
    score[-1] -= s
for i in range(M+1):
    score[i+1] += score[i]
    
print(max(score[1:M+1]))