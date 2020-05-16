S = list(input())
L = len(S)

ans = 0
for i, s in enumerate(S):
    if s == 'U':
        ans += 2*i + (L-1-i)
    else:
        ans += i + (L-1-i)*2
print(ans)