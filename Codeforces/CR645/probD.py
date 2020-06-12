import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
A = list(map(int, input().split()))

B = A + A
C = [0]*(2*N)
C[0] = A[0]*(A[0]+1)//2
for i in range(1, 2*N):
    C[i] = C[i-1] + B[i]*(B[i]+1)//2
    B[i] += B[i-1]


ans = 0
# Biまで読んだときの最大
for i in range(N, 2*N):
    b = B[i]
    ind = bisect_left(B, b-x)
    a = A[ind-N]
    d = a-(B[ind]-(b-x))
    score = C[i] - C[ind] + (a*(a+1)//2 - d*(d+1)//2)
    if score > ans:
        ans = score
print(ans)