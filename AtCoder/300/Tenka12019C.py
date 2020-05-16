N = int(input())
S = list(input())

T = [0 for _ in range(N+1)]
a = 0
for i, s in enumerate(S):
    if s == '#':
        a += 1
    T[i+1] = a

ans = N
for l in range(N+1):
    a = T[l] + (N-l)-(T[-1]-T[l])
    ans = min(ans, a)


print(ans)