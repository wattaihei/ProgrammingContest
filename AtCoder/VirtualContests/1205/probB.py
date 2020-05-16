S = input()
L = len(S)

for l in range(L+1):
    T = S + S[:l][::-1]
    ok = True
    for i in range(L+l):
        if T[i] != T[-i-1]:
            ok = False
    if ok:
        print(l)
        break