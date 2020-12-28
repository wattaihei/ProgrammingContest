import sys
input = sys.stdin.buffer.readline


def main():
    H, W, N, M = map(int, input().rstrip().split())
    Lights = [list(map(int, input().rstrip().split())) for _ in range(N)]
    Blocks = [list(map(int, input().rstrip().split())) for _ in range(M)]

    state = [[0]*W  for _ in range(H)]

    # 0: none
    # 1: light
    # 2: block
    # 3: got light

    for h, w in Lights:
        state[h-1][w-1] = 1

    for h, w in Blocks:
        state[h-1][w-1] = 2

    for h in range(H):
        g = False
        for w in range(W):
            if state[h][w] == 2:
                g = False
            elif state[h][w] == 1:
                g = True
            else:
                if g:
                    state[h][w] = 3

    for h in range(H):
        g = False
        for w in reversed(range(W)):
            if state[h][w] == 2:
                g = False
            elif state[h][w] == 1:
                g = True
            else:
                if g:
                    state[h][w] = 3

    for w in range(W):
        g = False
        for h in range(H):
            if state[h][w] == 2:
                g = False
            elif state[h][w] == 1:
                g = True
            else:
                if g:
                    state[h][w] = 3

    ans = 0
    for w in range(W):
        g = False
        for h in reversed(range(H)):
            if state[h][w] == 2:
                g = False
            elif state[h][w] == 1:
                g = True
            else:
                if g:
                    state[h][w] = 3
            if state[h][w] == 1 or state[h][w] == 3:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()