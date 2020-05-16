from collections import Counter

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    S1 = list(input())
    S2 = list(input())
    Query.append((N, S1, S2))

for N, S1, S2 in Query:
    C = Counter(S1+S2)
    ok = True
    for v in C.values():
        if v % 2 != 0:
            ok = False
    if not ok:
        print("No")
    else:
        print("Yes")
        ans = []
        for i in range(N):
            s1, s2 = S1[i], S2[i]
            if s1 != s2:
                for j in range(i+1, N):
                    if S1[j] == S2[j]: continue
                    if S1[j] == s1:
                        ans.append((j+1, i+1))
                        S1[j] = s2
                        break
                    elif S2[j] == s1:
                        ans.append((j+1, j+1))
                        ans.append((j+1, i+1))
                        S2[j] = S1[j]
                        S1[j] = s2
                        break
        print(len(ans))
        for a, b in ans:
            print(a, b)