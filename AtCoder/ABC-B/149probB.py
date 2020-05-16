A, B, K = map(int, input().split())

if A > K:
    A -= K
elif B > (K-A):
    B -= (K-A)
    A = 0
else:
    B = 0
    A = 0
print(A, B)
