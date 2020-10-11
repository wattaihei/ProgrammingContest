import sys
input = sys.stdin.buffer.readline

N = int(input())
S = list(input().rstrip())
T = list(input().rstrip())

def clean(P):
    if not P: return P
    pre = P[0]
    tmp = 0
    ret = []
    for p in P:
        if p * pre < 0:
            ret.append(tmp)
            tmp = p
        else:
            tmp += p
        pre = p
    if P[-1] * P[0] > 0:
        if ret:
            ret[0] += tmp
        else:
            ret.append(tmp)
    else:
        ret.append(tmp)
    return ret


P = []
for i, (s, t) in enumerate(zip(S, T)):
    if s > t:
        P.append(+1)
    elif s < t:
        P.append(-1)

if not P:
    ans = 0
elif sum(P) != 0:
    ans = -1
else:
    P = clean(P)
    ans = 0
    while P:
        ans += 1
        nP = []
        for p in P:
            if p > 1:
                nP.append(p-1)
            elif p < -1:
                nP.append(p+1)
        P = clean(nP)

print(ans)
            


