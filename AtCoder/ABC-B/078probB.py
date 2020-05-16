X, Y, Z = map(int, input().split())

A = X//(Y+Z)
if X%(Y+Z) < Z:
    A -= 1
print(A)