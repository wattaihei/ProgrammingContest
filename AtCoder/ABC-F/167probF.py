import sys
input = sys.stdin.readline

MAX = 10**6
N = int(input())
Ss = [input().rstrip() for _ in range(N)]

def calc(S):
    stack = []
    for s in S:
        if s == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(s)
    le = 0
    ri = 0
    for s in stack:
        if s == ")":
            le += 1
        else:
            ri += 1
    return le, ri

Ps = [[] for _ in range(MAX+1)]
Qs = [[] for _ in range(MAX+1)]
for S in Ss:
    le, ri = calc(S)
    if ri >= le:
        Ps[le].append(ri-le)
    else:
        Qs[ri].append(le-ri)

T = 0
ok = True
for le, P in enumerate(Ps):
    if P and T < le:
        ok = False
        break
    else:
        T += sum(P)

U = 0
for ri, Q in enumerate(Qs):
    if Q and U < ri:
        ok = False
        break
    else:
        U += sum(Q)

if T != U:
    ok = False
print("Yes" if ok else "No")