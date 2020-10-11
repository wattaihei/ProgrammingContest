import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

if N%2 == 0:
    ans = sum(A[1:(N-2)//2+1])*2
else:
    ans = sum(A[1:(N-2)//2+1])*2 + A[(N-2)//2+1]
ans += A[0]
print(ans)