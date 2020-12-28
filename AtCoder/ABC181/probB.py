import sys
input = sys.stdin.buffer.readline


N = int(input())
AB = [list(map(int, input().rstrip().split())) for _ in range(N)]

ans = 0
for a, b in AB:
    ans += b*(b+1)//2 - a*(a-1)//2
print(ans)