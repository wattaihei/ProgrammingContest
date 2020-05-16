import math

N, M = map(int, input().split())
R = list(map(int, input().split()))

log_p = 0
n = 0
for r in R:
    for k in range(1, r+1):
        n += 1
        log_p = log_p + math.log10(n/k/M)
print(1-int(log_p))