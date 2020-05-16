import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((H, N, A))


for H, N, A in Query:
    A.append(0)
    now = H
    i = 0
    c = 0
    while now > 0:
        if now - A[i+1] > 1:
            now = A[i+1]+1
        else:
            if i+2 >= N+1:
                break
            elif now - A[i+2] > 2:
                i += 1
                c += 1
                now -= 2
            else:
                i += 2
                now -= 2
    print(c)