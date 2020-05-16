import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    E = []
    O = []
    for i, a in enumerate(A):
        if a%2 == 0:
            E.append(i+1)
            break
        else:
            O.append(i+1)
    if E:
        print(1)
        print(*E)
    elif len(O) > 1:
        print(2)
        print(*O[:2])
    else:
        print(-1)