import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans = max(ans, A[i]^A[j])
print(ans)