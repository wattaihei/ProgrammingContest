import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    S = list(input().rstrip())
    T = list(input().rstrip())
    Query.append((S, T))

for S, T in Query:
    S.sort()
    l = len(S)
    p = len(T)
    ok = False
    for i in range(p-l+1):
        if sorted(T[i:i+l]) == S:
            ok = True
            break
    print("YES" if ok else "NO")