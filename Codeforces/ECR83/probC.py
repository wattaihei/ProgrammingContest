import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

L = 100
for N, K, A in Query:
    ok = True
    B = [0]*L
    for a in A:
        ind = 0
        while a:
            if a%K == 1:
                B[ind] += 1
            elif a%K != 0:
                ok = False
                break
            ind += 1
            a //= K
    for b in B:
        if b > 1:
            ok = False
            break
    print("YES" if ok else "NO")