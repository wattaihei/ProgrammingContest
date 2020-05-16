import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    S = input().rstrip()
    Query.append((N, S))

for N, S in Query:
    la = []
    sm = []
    dif = False
    for s in S:
        if not dif:
            if s == "0":
                la.append(str(0))
                sm.append(str(0))
            elif s == "1":
                la.append(str(1))
                sm.append(str(0))
                dif = True
            else:
                la.append(str(1))
                sm.append(str(1))
        else:
            if s == "0":
                la.append(str(0))
                sm.append(str(0))
            elif s == "1":
                la.append(str(0))
                sm.append(str(1))
            else:
                la.append(str(0))
                sm.append(str(2))
    print("".join(la))
    print("".join(sm))