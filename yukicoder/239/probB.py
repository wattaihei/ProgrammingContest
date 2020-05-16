import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

B = [0]
for i in range(N):
    b = A[2*i]-A[2*i+1]
    B.append(B[-1]+b)


S = B[-1]
ans = -10**15
for b in B:
    ans = max(ans, 2*b - S)
print(ans)