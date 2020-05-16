import sys
input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    state = [list(map(int, input().split())) for _ in range(H)]

    black = [[[0, 0] for _ in range(W+1)] for _ in range(H+1)]
    for h in range(H):
        for w in range(W):
            black[h+1][w+1][(h+w)%2] = state[h][w]
    for h in range(1, H+1):
        for w in range(1, W+1):
            black[h][w][0] += black[h-1][w][0] + black[h][w-1][0] - black[h-1][w-1][0]
            black[h][w][1] += black[h-1][w][1] + black[h][w-1][1] - black[h-1][w-1][1]

    ans = 0
    for lh in range(H):
        for rh in range(lh+1, H+1):
            for lw in range(W):
                for rw in range(lw+1, W+1):
                    a0 = black[rh][rw][0] - black[rh][lw][0] - black[lh][rw][0] + black[lh][lw][0]
                    a1 = black[rh][rw][1] - black[rh][lw][1] - black[lh][rw][1] + black[lh][lw][1]
                    if a0 == a1:
                        ans = max(ans, (rh-lh)*(rw-lw))
    print(ans)

if __name__ == "__main__":
    main()