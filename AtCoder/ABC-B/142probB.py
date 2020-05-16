N, K = map(int, input().split())
A = list(map(int, input().split()))

c = 0
for a in A:
    if a >= K:
        c += 1
print(c)