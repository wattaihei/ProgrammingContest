from bisect import bisect_left, bisect_right

INF = int(1E18)
A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]
S.insert(0, -INF)
T.insert(0, -INF)
S.append(INF)
T.append(INF)

for x in X:
    i = bisect_left(S, x)
    j = bisect_left(T, x)
    s1, s2 = S[i-1], S[i]
    t1, t2 = T[j-1], T[j]
    s1 = abs(s1-x)
    s2 = abs(s2-x)
    t1 = abs(t1-x)
    t2 = abs(t2-x)
    l1 = max(s1, t1)
    l2 = min(s1, t1)
    r1 = max(s2, t2)
    r2 = min(s2, t2)
    E = [l1, r1]
    if (s1-t1)*(s2-t2) < 0:
        E.extend([2*l2+r2, 2*r2+l2])
    print(min(E))