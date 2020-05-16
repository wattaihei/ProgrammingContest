N = int(input())
C = [int(input()) for _ in range(N)]

a = 0
b = 1
for i, c in enumerate(C):
    b *= (i+1)
    r = -1
    for c0 in C:
        if c % c0 == 0:
            r += 1
    if r % 2 == 0:
        a += 1-r/(r+1)/2
    else:
        a += 1/2

print(a)
