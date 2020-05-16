import sys
input = sys.stdin.readline

INF = 10**14

def main():
    N, M = map(int, input().split())
    dp = [INF for _ in range(N*N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        dp[(a-1)*N+b-1] = min(c, dp[(a-1)*N+b-1])
        dp[(b-1)*N+a-1] = min(c, dp[(b-1)*N+a-1])
    K = int(input())
    XYZ = [list(map(int, input().split())) for _ in range(K)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i*N+j] = min(dp[i*N+j], dp[i*N+k]+dp[k*N+j])

    for i in range(N):
        dp[i*N+i] = 0

    for x, y, z in XYZ:
        for i in range(N):
            for j in range(N):
                dp[i*N+j] = min((dp[i*N+j], dp[i*N+x-1]+z+dp[(y-1)*N+j], dp[i*N+y-1]+z+dp[(x-1)*N+j]))
        s = 0
        for i in range(N-1):
            for j in range(i+1, N):
                s += dp[i*N+j]
        print(s)
    

if __name__ == "__main__":
    main()