N = int(input())
C = []
S = []
F = []
for _ in range(N-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N):
    if i == N-1:
        print(0)
        break
    t = C[i] + S[i]
    for j in range(i+1, N-1):
        k = t % F[j]
        arrive = t + F[j] - k if k != 0 else t
        t = max(S[j], arrive) + C[j]
    print(t)