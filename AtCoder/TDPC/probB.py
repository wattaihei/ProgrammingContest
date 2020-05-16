import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = A[::-1]
    B = B[::-1]

    S = [[0 for _ in range(b+1)] for _ in range(a+1)]
    for i in range(1, a+1):
        S[i][0] = S[i-1][0] + A[i-1]
    for j in range(1, b+1):
        S[0][j] = S[0][j-1] + B[j-1]
    for i in range(1, a+1):
        for j in range(1, b+1):
            S[i][j] = S[i][0] + S[0][j]

    dp = [[0 for _ in range(b+1)] for _ in range(a+1)]
    for i in range(a+1):
        for j in range(b+1):
            if i == 0:
                if j == 0:
                    continue
                dp[i][j] = B[j-1]+S[i][j-1]-dp[i][j-1]
            elif j == 0:
                dp[i][j] = A[i-1]+S[i-1][j]-dp[i-1][j]
            else:
                dp[i][j] = max(A[i-1]+S[i-1][j]-dp[i-1][j], B[j-1]+S[i][j-1]-dp[i][j-1])

    print(dp[a][b])


if __name__ == "__main__":
    main()