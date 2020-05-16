import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [0]*((N+1)*4)

    for i in range(3):
        a, b = A[i], B[i]
        for w in range(N+1):
            if w < a:
                dp[w*4+i+1] = dp[w*4+i]
            else:
                dp[w*4+i+1] = max(dp[w*4+i], dp[(w-a)*4+i+1] + b-a)

    M = dp[N*4+3] + N

    dp2 = [0]*((M+1)*4)
    for i in range(3):
        a, b = A[i], B[i]
        for w in range(M+1):
            if w < b:
                dp2[w*4+i+1] = dp2[w*4+i]
            else:
                dp2[w*4+i+1] = max(dp2[w*4+i], dp2[(w-b)*4+i+1] + a-b)

    print(dp2[M*4+3]+M)


if __name__ == "__main__":
    main()