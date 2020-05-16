from fractions import gcd

N, M = map(int, input().split()) # 横に2個
S = input()
T = input()
Gcd = gcd(N, M)
Np = N // Gcd
Mp = M // Gcd

ans = Gcd * Mp * Np
for g in range(Gcd):
    if S[g*Np] != T[g*Mp]:
        ans = -1
        break

print(ans)