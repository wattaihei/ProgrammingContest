import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = collections.Counter(A)
C = list(B.values())

C.sort(reverse=True)
print(sum(C[K:]))