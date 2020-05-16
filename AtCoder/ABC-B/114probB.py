S = input()
L = len(S)

for i in range(L-2):
    x = int(S[i:i+3])
    d = abs(x - 753)
    if i == 0:
        ans = d
        continue
    ans = min(ans, d)

print(ans)