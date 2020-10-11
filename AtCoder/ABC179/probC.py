import sys
input = sys.stdin.buffer.readline

N = int(input())

ans = 0
for a in range(1, N+1):
    maxb = (N-1)//a
    ans += maxb

print(ans)