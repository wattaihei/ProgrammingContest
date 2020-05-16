S = input()
N = len(S)
ans = ''
for n in range(0, N, 2):
    ans += S[n]
print(ans)