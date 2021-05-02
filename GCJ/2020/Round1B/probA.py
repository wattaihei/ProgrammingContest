import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

# Q = 9*9
# Query = []
# for n in range(-4, 5):
#     for m in range(-4, 5):
#         Query.append((n, m))


def probs(n, sg, nowL, ret):
    if n == 0:
        ret.append(nowL)
        return ret
    l = n.bit_length()
    if n-(1<<(l-1)) == 0:
        ret.append(nowL+[((l-1), sg)])
        return ret
    ret = probs(n-(1<<(l-1)), sg, nowL+[((l-1), sg)], ret)
    ret = probs((1<<l)-n, sg*(-1), nowL+[(l, sg)], ret)
    return ret

for qnum, (a, b) in enumerate(Query):
    p1s = probs(abs(a), a//abs(a) if a != 0 else 0, [], [])
    p2s = probs(abs(b), b//abs(b) if b != 0 else 0, [], [])
    L = max(abs(a), abs(b)).bit_length()
    #print(p1s)
    #print(p2s)
    ans = []
    for p1 in p1s:
        for p2 in p2s:
            use = [-1]*(L+2)
            ok = True
            for p, sg in p2:
                if sg > 0:
                    use[p] = "N"
                else:
                    use[p] = "S"
            for p, sg in p1:
                if sg > 0:
                    if use[p] != -1:
                        ok = False
                        break
                    use[p] = "E"
                else:
                    if use[p] != -1:
                        ok = False
                        break
                    use[p] = "W"
            
            for l in range(L+1):
                if use[l] == -1 and use[l+1] != -1:
                    ok = False
                    break
            if ok:
                tmp = []
                for u in use:
                    if u != -1:
                        tmp.append(u)
                if ans and len(tmp) < len(ans):
                    ans = tmp
                elif not ans:
                    ans = tmp
    # print(a, b)
    if ans:
        print("Case #{0}: {1}".format(qnum+1, "".join(ans)))
    else:
        print("Case #{0}: {1}".format(qnum+1, "IMPOSSIBLE"))