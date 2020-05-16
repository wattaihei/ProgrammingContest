import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
if A[0] < 0:
    ans = A[0]
else:
    ans = 0
    for i in range(K):
        if A[i] > 0:
            ans += A[i]
print(ans)