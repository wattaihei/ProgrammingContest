import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    a, b, p = map(int, input().split())
    S = list(input().rstrip())
    Query.append((a, b, p, S))

for a, b, p, S in Query:
    L = len(S)
    S.pop()
    while S:
        s = S[-1]
        if s == "A":
            t = a
        else:
            t = b
        if t > p:
            break
        p -= t
        while S and S[-1] == s:
            S.pop()
    print(len(S)+1)