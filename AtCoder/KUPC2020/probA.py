import sys
input = sys.stdin.buffer.readline

N = int(input())
ans = 0
px, py = map(int, input().split())
for _ in range(N-1):
    x, y = map(int, input().split())
    ans += abs(x-px) + abs(y-py)
    px, py = x, y
print(ans)