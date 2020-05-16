N = int(input())
S = input()

l = 0
r = 0
for s in S:
    if s == '(':
        l += 1
    elif s == ')':
        r += 1
if N%2 == 1:
    ans = ':('
else:
    lim = N//2
    ok = True
    if l > lim or r > lim:
        ok = False
    ans = ''
    for s in S:
        if s == '(' or s == ')':
            ans += s
        elif l < lim:
            ans += '('
            l += 1
        else:
            ans += ')'

    d = 0
    for i in range(N-1):
        a = ans[i]
        if a == '(':
            d += 1
        elif d > 1:
            d -= 1
        else:
            ok = False

    if not ok:
        ans = ':('

print(ans)