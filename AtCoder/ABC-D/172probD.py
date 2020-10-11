import sys
input = sys.stdin.readline


N = int(input())

ans = 0
for k in range(1, N+1):
    M = N//k
    ans += k*(M*(M+1)//2)
print(ans)