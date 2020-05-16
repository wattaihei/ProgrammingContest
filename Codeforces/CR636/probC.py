import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    T = []
    sig = A[0]
    ans = 0
    for a in A:
        if a > 0:
            if sig > 0:
                T.append(a)
            else:
                ans += max(T)
                T = [a]
                sig = 1
        else:
            if sig > 0:
                ans += max(T)
                T = [a]
                sig = -1
            else:
                T.append(a)
    if T:
        ans += max(T)
    print(ans)