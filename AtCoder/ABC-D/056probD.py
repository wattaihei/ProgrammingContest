import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dp1 = [set() for _ in range(N)]
    dp1[0].add(0)
    for n in range(N-1):
        for pm in dp1[n]:
            dp1[n+1].add(pm)
            if pm + A[n] < K:
                dp1[n+1].add(pm+A[n])

    dp2 = [set() for _ in range(N)]
    dp2[N-1].add(0)
    for n in reversed(range(1, N)):
        for pm in dp2[n]:
            dp2[n-1].add(pm)
            if pm+A[n] < K:
                dp2[n-1].add(pm+A[n])

    ans = 0
    for n, a in enumerate(A):
        b = K - a
        if b <= 0: continue
        need = False
        B1 = sorted(dp1[n])
        B2 = sorted(dp2[n], reverse=True)
        i2 = 0
        for b1 in B1:
            while B2[i2] + b1 >= K:
                i2 += 1
                if i2 == len(B2): break
            if i2 == len(B2): break
            if b1+B2[i2] < b:
                continue
            else:
                need = True
                break
        if not need: ans += 1
    print(ans)


if __name__ == "__main__":
    main()