import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dp1 = [[0]*K for _ in range(N)]
    dp1[0][0] = 1
    for n in range(N-1):
        for k in range(K):
            if k < A[n]:
                dp1[n+1][k] = dp1[n][k]
            else:
                dp1[n+1][k] = dp1[n][k] | dp1[n][k-A[n]]

    dp2 = [[0]*K for _ in range(N)]
    dp2[N-1][0] = 1
    for n in reversed(range(1, N)):
        for k in range(K):
            if k < A[n]:
                dp2[n-1][k] = dp2[n][k]
            else:
                dp2[n-1][k] = dp2[n][k] | dp2[n][k-A[n]]

    ans = 0
    for n, a in enumerate(A):
        if K-a <= 0: continue
        need = False
        k2 = K-1
        for k1 in range(K):
            if not dp1[n][k1]: continue
            while not dp2[n][k2] or k1+k2 >= K:
                k2 -= 1
            if k1+k2 >= K-a:
                need = True
                break
        if not need: ans += 1
    print(ans)

if __name__ == "__main__":
    main()