import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
if N <= K:
    print(0)
else:
    print(sum(A[K:]))