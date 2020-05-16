S = input()

K = ['A', 'K', 'I', 'H', 'B', 'R']

ans = 'YES'
p = 0
cont = False
for s in S:
    if not s in K:
        ans = 'NO'
    elif s == 'A':
        if (p == 0 or p == 3 or p == 4 or p == 5) and not cont:
            cont = True
        else:
            ans = 'NO'
    elif p == 5:
        ans = 'NO'
        break
    elif s == K[p+1]:
        p += 1
        cont = False
    else:
        ans = 'NO'
if p != 5:
    ans = 'NO'
print(ans)