import sys
input = sys.stdin.readline

def main():
    K = int(input())
    N = 2**K
    A = [int(input()) for _ in range(N)]

    dp = [[1 for _ in range(K+1)] for _ in range(N)]

    for k in range(1, K+1):
        for i in range(N):
            a = 0
            for j in range(N):
                if i//(2**k) == j//(2**k) and i//(2**(k-1)) != j//(2**(k-1)):
                    a += dp[j][k-1] * 1/(1+10**((A[j]-A[i])/400))
            dp[i][k] = dp[i][k-1] * a

    for i in range(N):
        print(dp[i][K])

if __name__ == "__main__":
    main()