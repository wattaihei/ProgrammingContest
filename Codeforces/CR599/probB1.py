Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    S1 = list(input())
    S2 = list(input())
    Query.append((N, S1, S2))

for N, S1, S2 in Query:
    C = []
    for i in range(N):
        s1, s2 = S1[i], S2[i]
        if s1 != s2:
            C.append((s1, s2))
    if len(C) == 0:
        print('Yes')
    elif len(C) == 2:
        if C[0][0] == C[1][0] and C[0][1] == C[1][1]:
            print('Yes')
        else:
            print("No")
    else:
        print("No")