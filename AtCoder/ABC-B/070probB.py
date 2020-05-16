A, B, C, D = map(int, input().split())

a = 0
for t in range(100):
    if A <= t < B and C <= t < D:
        a += 1
print(a)