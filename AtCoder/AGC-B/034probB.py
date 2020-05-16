S = input()
N = len(S)

a = 0
ans = 0
nowB = False
for i in range(N):
    if S[i] == 'A':
        if nowB:
            a = 0
        a += 1
        nowB = False
    elif S[i] == 'B':
        if nowB:
            a = 0
        nowB = True
    else:
        if nowB:
            ans += a
            nowB = False
        else:
            a = 0
print(ans)