Q = int(input())
Query = []
for _ in range(Q):
    S = input()
    Query.append(S)

for S in Query:
    L = len(S)
    OK = set()
    pa = False
    for i in range(L):
        if pa:
            pa = False
            continue
        if i == L-1:
            OK.add(S[i])
            break
        if S[i] != S[i+1]:
            OK.add(S[i])
        else:
            pa = True
    ans = sorted(list(OK))
    print(''.join(ans))
