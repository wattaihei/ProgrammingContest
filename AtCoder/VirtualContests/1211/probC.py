import sys
input = sys.stdin.readline


H, W, K = map(int, input().split())
RC = [list(map(int, input().split())) for _ in range(K)]

Hs = [W]*H
Ws = [H]*W

for r, c in RC:
    Hs[r-1] -= 1
    Ws[c-1] -= 1

center = (H*W-K+1)//2
C = [0, 0]

p = 0
for iw, h in enumerate(Hs):
    if p < center <= p+h:
        C[0] = iw
        break
    p += h

q = 0
for ih, w in enumerate(Ws):
    if q < center <= q+w:
        C[1] = ih
        break
    q += w

S = 0
for ih, w in enumerate(Hs):
    S += abs(ih-C[0])*w
for iw, h in enumerate(Ws):
    S += abs(iw-C[1])*h

print(S)