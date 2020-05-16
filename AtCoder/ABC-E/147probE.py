import sys
input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    P = W+1
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    L = 80*80
    dp = [[False]*(L+1) for _ in range((W+1)*(H+1))]
    dp[P+1][abs(A[0][0]-B[0][0])] = True
    
    for h in range(H):
        for w in range(W):
            if h == 0 and w == 0: continue
            c = abs(A[h][w] - B[h][w])
            for l in range(L-c+1):
                b1 = abs(l-c)
                b2 = abs(l+c)
                dp[(h+1)*P+w+1][l] = dp[h*P+w+1][b1] or dp[(h+1)*P+w][b1] or dp[h*P+w+1][b2] or dp[(h+1)*P+w][b2]

    for l in range(L+1):
        if dp[H*P+W][l]:
            print(l)
            break


if __name__ == "__main__":
    main()