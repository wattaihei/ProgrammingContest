import sys
input = sys.stdin.buffer.readline

from bisect import bisect_left

INF = 10**18

N, M = map(int, input().rstrip().split())
H = list(map(int, input().rstrip().split()))
W = list(map(int, input().rstrip().split()))

H.sort()

s = 0
for i in range(N//2):
    s += H[2*i+2] - H[2*i+1]

Score = [0]*N
Score[0] = s

for i in range(1, N):
    pres = Score[-1]
    if i%2 == 0:
        Score[i] = Score[i-2] + (H[i-1] - H[i-2]) - (H[i] - H[i-1])
    else:
        Score[i] = Score[i-1] + (H[i+1] - H[i-1]) - (H[i+1] - H[i])
    
ans = INF
for w in W:
    ind = bisect_left(H, w)
    if ind != N:
        ans = min(ans, abs(H[ind]-w) + Score[ind])
    if ind != 0:
        ans = min(ans, abs(H[ind-1]-w) + Score[ind-1])
    
print(ans)