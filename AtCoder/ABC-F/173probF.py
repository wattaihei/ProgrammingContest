import sys
input = sys.stdin.buffer.readline

N = int(input())
Edges = [list(map(int, input().split())) for _ in range(N-1)]

ans = 0
for l in range(1, N+1):
    ans += (N-l+2)*(N-l+1)//2


for a, b in Edges:
    if a > b:
        b, a = a, b
    ans -= a * (N-b+1)

print(ans)