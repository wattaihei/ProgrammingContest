N = int(input())
S = [1 if a == 'W' else 0 for a in list(input())]
mod = int(1E9+7)

p = 0
prob = 1
even = True
ans = 1
for s in S:
    if s == 0:
        if even:
            p += prob
            even = False
        else:
            ans *= p
            #p = p-prob
            even = True
    else:
        if not even:
            p += prob
            even = True
        else:
            ans *= p
            #p = p-prob
            prob += 1
            even = False
    print(p, prob, even, ans)
    ans = ans % mod
print(ans)