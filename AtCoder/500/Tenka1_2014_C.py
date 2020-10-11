
def main():
    import sys
    input = sys.stdin.buffer.readline

    INF = 10**18

    N, M = map(int, input().split())
    Ss = [list(input().rstrip()) for _ in range(N)]

    isConnected = [[True]*N for _ in range(N)]

    # construct graph
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if Ss[i][k] != Ss[j][k] and Ss[i][k] != ord("*") and Ss[j][k] != ord("*"):
                    isConnected[i][j] = False
                    isConnected[j][i] = False
                    break

    dp = [1]*(1<<N)
    for bit in range(1<<N):
        for i in range(N):
            for j in range(i+1,N):
                if (1<<i)&bit and (1<<j)&bit and not isConnected[i][j]:
                    dp[bit] = INF
                    break
    

    for bit1 in range(1<<N):
        for bit2 in range(1<<N):
            dp[bit1|bit2] = min(dp[bit1|bit2], dp[bit1]+dp[bit2])
    
    print(dp[-1])


if __name__ == "__main__":
    main()