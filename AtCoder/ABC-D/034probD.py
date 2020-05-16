import sys
input = sys.stdin.readline

N, K = map(int, input().split())
WP = [list(map(int, input().split())) for _ in range(N)]

W = []
S = []
for w, p in WP:
    W.append(w)
    S.append(w*p/100)

l = -1
r = 100
while r - l > 1E-14:
    m = (l+r)/2
    com = []
    for i in range(N):
        com.append(S[i]-m*W[i])
    com.sort(reverse=True)
    s = 0
    for i in range(K):
        s += com[i]
    if s >= 0:
        l = m
    else:
        r = m

print(m*100)