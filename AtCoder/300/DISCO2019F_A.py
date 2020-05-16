N = int(input())
S = list(input())

a = 0
ans = 0
A = []
for i, s in enumerate(S):
    if i == 0:
        ans += 1
        continue
    if s == '>':
        if S[i-1] == '>':
            a += 1
        else:
            a = 1
    else:
        if a > 0:
            A.append(a)
            a = 0
        ans += 1
#print(ans, A)
A.sort(reverse=True)
if not A:
    ans -= 1/2
else:
    for i, a in enumerate(A):
        if i == 0:
            for k in range(1, a+2):
                ans += 1/(k+1)
            ans -= 1
        else:
            for k in range(1, a+1):
                ans += 1/(k+1)
print(ans)