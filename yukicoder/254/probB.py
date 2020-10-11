import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i, a in enumerate(A):
    ans += a*(i+1)*(N-i)
print(ans)