import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

g = 0
gmax = 0
tmp_x = 0
ans = 0
for a in A:
    g += a
    gmax = max(g, gmax)
    ans = max(ans, tmp_x + gmax)
    tmp_x += g
    
print(ans)