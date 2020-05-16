import math

N, K = map(int, input().split())

prob = 0
for n in range(1, N+1):
    i = int(math.log2(K/n))
    if n > K:
        i = 0
    elif not n * 2**i == K:
        i += 1
    prob += 1 / N / (2**i)

print(prob)