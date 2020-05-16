N = int(input())
A = list(map(int, input().split()))

rate = [0 for _ in range(8)]
free = 0
for a in A:
    r = a // 400
    if r >= 8:
        free += 1
    else:
        rate[r] += 1

a1 = 0
for r in rate:
    if r != 0:
        a1 += 1
a2 = free + a1
if a1 == 0:
    a1 = 1
print(a1, a2)

