import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    a1 = False
    a2 = False
    for a in A:
        if a%2 == 0:
            a1 = True
        else:
            a2 = True
    print("YES" if (not a1 or not a2) else "NO")