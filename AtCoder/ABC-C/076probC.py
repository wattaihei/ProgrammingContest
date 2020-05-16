S = list(input())
T = list(input())


ans = 0
for j in range(len(S)-len(T)+1):
    can = True
    SS = S[:]
    for i, t in enumerate(T):
        s = S[j+i]
        if s != '?' and s != t:
            can = False
            break
        elif s == '?':
            SS[j+i] = t
    if can:
        ans = SS

if ans == 0:
    print('UNRESTORABLE')
else:
    Ans = ans[:]
    for i, a in enumerate(ans):
        if a == '?':
            Ans[i] = 'a'
    print(''.join(Ans))