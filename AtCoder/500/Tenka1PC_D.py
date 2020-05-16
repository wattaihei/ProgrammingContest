import sys
input = sys.stdin.readline

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

L = len(bin(K))-2

ans = 0
for a, b in AB:
    if (K | a) == K:
        ans += b

for n in reversed(range(L)):
    if (1 << n) & K:
        score = 0
        mask = (((1<<L)-(1<<n)) & K) - 1
        for a, b in AB:
            if (mask | a) == mask:
                score += b
        ans = max(ans, score)
print(ans)
