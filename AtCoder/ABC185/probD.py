import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
A.sort()
A.append(N+1)

block = []
pre = 0
for a in A:
    d = a-pre-1
    if d > 0:
        block.append(d)
    pre = a


ans = 0
if block:
    k = min(block)
    for b in block:
        ans += (b+k-1)//k

print(ans)