import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = A[0]
ans = 0
for a in A:
    ans += max(0, M-a)
    M = max(M, a)
print(ans)