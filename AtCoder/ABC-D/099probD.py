N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(int, input().split())) for _ in range(N)]

def main():
    state = [[0 for _ in range(C)] for _ in range(3)]
    for c in range(C):
        for w in range(N):
            for h in range(N):
                cost = D[grid[h][w]-1][c]
                state[(h+w)%3][c] += cost

    for c1 in range(C):
        for c2 in range(C):
            if c1 == c2:
                continue
            for c3 in range(C):
                if c3 == c1 or c3 == c2:
                    continue
                cost = state[0][c1] + state[1][c2] + state[2][c3]
                if c1 == 0 and c2 == 1 and c3 == 2:
                    ans = cost
                    continue
                ans = min(cost, ans)
    print(ans)

if __name__ == "__main__":
    main()