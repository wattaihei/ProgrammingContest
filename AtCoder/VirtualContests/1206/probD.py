import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]

l = 0
r = 10**9+1
while r-l > 1:
    m = (l+r)//2
    k = 0
    for h in H:
        c = max(0, h-m*B)
        k += c // (A-B)
        if c%(A-B) != 0: k += 1
    if k <= m:
        r = m
    else:
        l = m
print(r)