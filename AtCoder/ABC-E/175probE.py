import sys
input = sys.stdin.buffer.readline

def main():
    R, C, K = map(int, input().split())
    State = [[0]*R for _ in range(C)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        State[c-1][r-1] += v

    dp = [[0]*4 for _ in range(C+1)]

    for r in range(R):
        ndp = [[0]*4 for _ in range(C+1)]
        for c in range(C):
            ndp[c+1][0] = max(ndp[c+1][0], max(dp[c+1]))
            ndp[c+1][1] = ndp[c+1][0] + State[c][r]
            for n in range(4):
                if ndp[c][n] > ndp[c+1][n]:
                    ndp[c+1][n] = ndp[c][n]
                if n < 3 and ndp[c][n] + State[c][r] > ndp[c+1][n+1]:
                    ndp[c+1][n+1] = ndp[c][n] + State[c][r]
        dp = ndp
        
    print(max(dp[C]))

if __name__ == "__main__":
    main()