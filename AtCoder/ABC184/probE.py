import sys
input = sys.stdin.buffer.readline


def main():

    H, W = map(int, input().rstrip().split())
    state = [list(input().rstrip()) for _ in range(H)]

    al = [i for i in range(97, 97+26)]
    # aldic = {s:i for i, s in enumerate(al)}

    Color = [-1]*(H*W)
    dic = {s:[] for s in al}
    s = -1
    g = -1
    for h in range(H):
        for w in range(W):
            n = h*W + w
            if state[h][w] == ord("S"):
                s = n
            elif state[h][w] == ord("G"):
                g = n
            elif state[h][w] in dic:
                dic[state[h][w]].append(n)
                Color[n] = state[h][w]
    q = [s]
    D = [-1]*(H*W)
    D[s] = 0
    while q:
        qq = []
        for p in q:
            if p == g: break
            h, w = p//W, p%W
            for nh, nw in [(h-1, w), (h+1, w), (h, w-1), (h, w+1)]:
                if 0 <= nh < H and 0 <= nw < W and state[nh][nw] != ord("#"):
                    np = nh*W + nw
                    if D[np] == -1:
                        D[np] = D[p] + 1
                        qq.append(np)
            if Color[p] != -1:
                for np in dic[Color[p]]:
                    if D[np] == -1:
                        D[np] = D[p] + 1
                        qq.append(np)
                dic[Color[p]] = []
        q = qq

    print(D[g])


if __name__ == "__main__":
    main()