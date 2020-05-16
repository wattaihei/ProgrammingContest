S = {}
for i, s in enumerate(input()):
    if not s in S.keys():
        S[s] = [i]
    else:
        S[s].append(i)

T = {}
for i, t in enumerate(input()):
    if not t in T.keys():
        T[t] = [i]
    else:
        T[t].append(i)

Sa = sorted(S.values())
Ta = sorted(T.values())

if Sa == Ta:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)