import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    L = 2*K
    state = [[[0, 0] for _ in range(L+1)] for _ in range(K+1)]

    for _ in range(N):
        x, y, c = map(str, input().split())
        a, b = int(x)%L, int(y)%L
        k = 0 if c == 'W' else 1
        if a >= K:
            if b >= K:
                a -= K
                b -= K
            else:
                a -= K
                b += K
        state[a+1][b+1][k] += 1


    for i in range(K):
        for j in range(L):
            for k in [0, 1]:
                state[i+1][j+1][k] += state[i+1][j][k] + state[i][j+1][k] - state[i][j][k]

    ans = 0
    for x in range(K):
        for y in range(K):
            for k in [0, 1]:
                count = 0
                count += state[x][y][k]
                count += state[x][L][k] - state[x][y+K][k]
                count += state[K][y+K][k] - state[x][y+K][k] - state[K][y][k] + state[x][y][k]

                l = k ^ 1
                count += state[K][y][l] - state[x][y][l]
                count += state[x][y+K][l] - state[x][y][l]
                count += state[K][L][l] - state[K][y+K][l] - state[x][L][l] + state[x][y+K][l]

                ans = max(ans, count)
    print(ans)

if __name__ == "__main__":
    main()