N = int(input())
S = [0 if a == 'E' else 1 for a in input()]
Sp = [S[0]]
for i in range(1, N):
    Sp.append(Sp[-1]+S[i])

max = Sp[-1]
ans = N - max
for i in range(1, N):
    ans = min(abs(Sp[i-1]) + abs(N-(i+1)-max+Sp[i]), ans)

print(ans)