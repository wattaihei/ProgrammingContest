S = input()
K = int(input())

alp = [chr(i) for i in range(97, 97+26)]

ans = ''
for s in S:
    loc = alp.index(s)
    if s == 'a' or loc + K < 26:
        ans += s
    else:
        K -= 26 - loc
        ans += 'a'

if K > 0:
    K %= 26
    ans = ans[:-1] + alp[(alp.index(ans[-1])+K)%26]
print(ans)