import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort()
if N%2 == 0:
    ans = sum(A[:N//2])**2 + sum(A[N//2:])**2
else:
    ans = max(sum(A[:N//2])**2 + sum(A[N//2:])**2, sum(A[:N//2+1])**2 + sum(A[N//2+1:])**2)

print(ans)