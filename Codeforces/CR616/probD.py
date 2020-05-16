import sys
input = sys.stdin.readline

S = list(input().rstrip())
Q = int(input())
Query = []
for _ in range(Q):
    l, r = map(int, input().split())
    Query.append((l-1, r-1))

Alp = [chr(i) for i in range(97, 97+26)]

dic = {}
for alp in Alp:
    dic[alp] = [0]

for i, s in enumerate(S):
    for alp in Alp:
        if s == alp:
            dic[alp].append(dic[alp][-1]+1)
        else:
            dic[alp].append(dic[alp][-1])

for l, r in Query:
    P = []
    for alp in Alp:
        d = dic[alp][r+1] - dic[alp][l]
        if d > 0:
            P.append(alp)
    if len(P) == 1:
        ok = True if l == r else False
    elif len(P) > 2:
        ok = True
    else:
        ok = True if S[l] != S[r] else False
    print("Yes" if ok else "No")