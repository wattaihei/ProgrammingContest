N = int(input())
Al = ['M', 'A', 'R', 'C', 'H']
S = {}
for _ in range(N):
    s = input()[0]
    if s in Al:
        if not s in S.keys():
            S[s] = 1
        else:
            S[s] += 1
L = S.values()
if len(L) == 3:
    a, b, c = L
    ans = a*b*c
elif len(L) == 4:
    a, b, c ,d = L
    ans = a*b*c + a*b*d + a*c*d + b*c*d
elif len(L) == 5:
    a, b, c, d, e = L
    ans = a*b*c + a*b*d + a*c*d + b*c*d + a*b*e + a*c*e + a*d*e + b*c*e + b*d*e + c*d*e
else:
    ans = 0

print(ans)