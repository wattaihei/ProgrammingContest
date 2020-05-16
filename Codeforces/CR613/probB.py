import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    ok = True
    S = sum(A)
    b = 0
    min_b = 0
    min_ind = -1
    for i, a in enumerate(A):
        b += a
        if i == N-1:
            if min_ind != -1:
                ok = False
                break
        elif b - min_b >= S:
            ok = False
            break
        if b <= min_b:
            min_b = b
            min_ind = i
    print("YES" if ok else "NO")