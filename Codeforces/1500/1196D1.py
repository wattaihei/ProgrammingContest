import sys
input = sys.stdin.readline

def main():
    Q = int(input())
    data = []
    for _ in range(Q):
        N, K = map(int, input().split())
        S = input().rstrip()
        data.append([N, K, S])

    RGB = []
    for i in range(300000):
        if i%3 == 0:
            RGB.append('R')
        elif i%3==1:
            RGB.append('G')
        else:
            RGB.append('B')

    for N, K, S in data:
        ans = N
        dp = [[0 for _ in range(N)] for _ in range(3)]
        for j in range(3):
            for i in range(N):
                if S[i] != RGB[i+j]:
                    dp[j][i] = 1
        for j in range(3):
            p = 0
            for k in range(K):
                p += dp[j][k]
            ans = min(ans, p)
            for i in range(1, N-K+1):
                p += dp[j][K-1+i] - dp[j][i-1]
                ans = min(ans, p)
        print(ans)

if __name__ == "__main__":
    main()