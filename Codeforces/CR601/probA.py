import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    A, B = map(int, input().split())
    Query.append((A, B))

for A, B in Query:
    delta = abs(B-A)
    ans = delta//5
    am = delta%5
    if am == 3 or am == 4:
        ans += 2
    elif am == 1 or am == 2:
        ans += 1
    print(ans)