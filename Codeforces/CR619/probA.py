import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    A = input().rstrip()
    B = input().rstrip()
    C = input().rstrip()
    Query.append((A, B, C))

for A, B, C in Query:
    ok = True
    for i in range(len(C)):
        if C[i] == A[i] or C[i] == B[i]:
            continue
        ok = False
        break
    print("YES" if ok else "NO")