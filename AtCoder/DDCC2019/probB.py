import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

B = []
b = 0
for a in A:
    b += a
    B.append(b)

ans = 10**14
for i in range(N):
    ans = min(abs(B[-1]-2*B[i]), ans)
print(ans)