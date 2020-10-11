import sys
input = sys.stdin.buffer.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    B = [A[0]]
    if A[1] > A[0]:
        up = True
        B.append(A[1])
    elif A[1] < A[0]:
        up = False
        B.append(A[1])
    for i in range(2, N):
        a = A[i]
        if B[-1] < a:
            if up:
                B.pop()
                B.append(a)
            else:
                B.append(a)
            up = True
        else:
            if not up:
                B.pop()
            B.append(a)
            up = False
    print(len(B))
    print(*B)