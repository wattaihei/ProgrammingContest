import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

s = 0
B = []
for i in reversed(range(N)):
    s += A[i]
    B.append(s)

ans = B.pop()
B.sort(reverse=True)
for i in range(K-1):
    ans += B[i]
print(ans)