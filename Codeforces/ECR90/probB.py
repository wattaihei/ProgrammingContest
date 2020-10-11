import sys
input = sys.stdin.readline

Q = int(input())
Query = [input().rstrip() for _ in range(Q)]

for S in Query:
    L = len(S)
    a = S.count("1")
    p = min(a, L-a)
    print("DA" if p%2 == 1 else "NET")