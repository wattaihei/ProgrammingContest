import sys
input = sys.stdin.buffer.readline

N = int(input())

p = 3
a = 1
a1 = -1
a2 = -1
while p < N:
    q = N-p
    b = 0
    while q >= 5:
        if q%5 != 0:
            b = -1
            break
        else:
            q //= 5
            b += 1
    if b >= 1:
        a1 = a
        a2 = b
    a += 1
    p *= 3

if a1 != -1:
    print(a1, a2)
else:
    print(-1)
    