S = input()
L = len(S)
if L % 2 == 0:
    ans = L // 2
    print(ans)
else:
    ans = L // 2
    ok = False
    for i in range(1, L):
        if S[i] == '1':
            ok = True
    if ok:
        ans += 1
    print(ans)