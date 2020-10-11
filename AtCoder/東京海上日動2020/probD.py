import sys
input = sys.stdin.buffer.readline

MAX = (1<<10)

def main():
    N = int(input())
    VW = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    M = 0
    for _, L in Query:
        if L > M:
            M = L

    dp = [[0]*(M+1) for _ in range(MAX+1)]
    for k in range(min(MAX, N)):
        nv, nw = VW[k]
        k += 1
        for w in range(M+1):
            if w >= nw and dp[k][w] < dp[k//2][w-nw] + nv:
                dp[k][w] = dp[k//2][w-nw] + nv
            if dp[k][w] < dp[k//2][w]:
                dp[k][w] = dp[k//2][w]
        

    for s, L in Query:
        dp2 = []
        # make new dp
        while s >= MAX:
            dp2.append(VW[s-1])
            s = s//2
        
        T = len(dp2)
        ans = dp[s][L]
        dp3 = [(0, 0)]
        for nv, nw in dp2:
            ndp = []
            for v, w in dp3:
                if w + nw <= L:
                    ndp.append((v+nv, w+nw))
                    score = dp[s][L-(w+nw)] + v + nv
                    if score > ans:
                        ans = score
            dp3 += ndp
        print(ans)

if __name__ == "__main__":
    main()