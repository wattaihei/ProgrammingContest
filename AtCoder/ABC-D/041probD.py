N, M = map(int, input().split())
XY = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]

bits = [i for i in range(1<<N)]
bits.sort(key=lambda x: x.bit_length())

dp = [0 for _ in range(1<<N)]
for n in range(N):
    dp[1<<n] = 1

for bit in bits:
    skip = False
    for x, y in XY:
        if (bit & (1 << y)) and not (bit & (1 << x)):
            skip = True
    if skip: continue
    for n in range(N):
        if not (bit & (1 << n)):
            dp[bit|(1<<n)] += dp[bit]
print(dp[-1])