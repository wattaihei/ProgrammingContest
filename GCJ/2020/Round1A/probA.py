import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    Ss = [input().rstrip() for _ in range(N)]
    Query.append((N, Ss))

for qnum, (N, Ss) in enumerate(Query):
    sta1 = set()
    sta2 = set()
    others = ""
    for S in Ss:
        A = list(S.split("*"))
        start = 0
        end = len(A)
        if S[0] != "*":
            sta2.add(A[0])
            start += 1
        if S[-1] != "*":
            sta1.add(A[-1])
            end -= 1
        others += "".join(A[start:end])
    
    ok = True
    ans1 = ""
    while sta2 and ok:
        l = len(ans1)
        cha = ""
        R = []
        for S in sta2:
            if len(S) <= l:
                R.append(S)
            elif not cha:
                cha = S[l]
            elif S[l] != cha:
                ok = False
                break
        for r in R:
            sta2.remove(r)
        ans1 += cha

    ans2 = ""
    while sta1 and ok:
        l = len(ans2)
        cha = ""
        R = []
        for S in sta1:
            if len(S) <= l:
                R.append(S)
            elif not cha:
                cha = S[-1-l]
            elif S[-1-l] != cha:
                ok = False
                break
        for r in R:
            sta1.remove(r)
        ans2 += cha
    
    if not ok:
        print("Case #{0}: {1}".format(qnum+1, "*"))
    else:
        print("Case #{0}: {1}".format(qnum+1, ans1 + others + ans2[::-1]))
        
    