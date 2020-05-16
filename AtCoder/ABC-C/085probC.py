N, Y = map(int, input().split())

Y = Y // 1000
if Y >= N:
    K = Y - N
    z = 0
    while True:
        if 9*z > K:
            x, y, z = -1, -1, -1
            break
        if (K - 9*z) % 4 == 0:
            y = (K - 9*z) // 4
            if N >= y + z:
                x = N - y - z
                break
        z += 1
else:
    x, y, z = -1, -1, -1

print(z, y, x)