N = 100

Dig = [[0]*200 for _ in range(N+1)]
Dig[0][0] = 1

for n in range(N):
    for i in range(200):
        Dig[n+1][i] = Dig[n][i]*(n+1)
    for i in range(200-1):
        Dig[n+1][i+1] += Dig[n+1][i] // 10
        Dig[n+1][i] = Dig[n+1][i] % 10

print(sum(Dig[N]))