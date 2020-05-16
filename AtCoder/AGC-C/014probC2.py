import sys
input = sys.stdin.readline


def main():
    H, W, K = map(int, input().split())
    state = [list(input()) for _ in range(H)]


    q = []
    checked = [[False]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if state[h][w] == "S":
                q.append((h, w))
                checked[h][w] = True

    goal = False
    for _ in range(K):
        qq = []
        for h, w in q:
            if h == 0 or h == H-1 or w == 0 or w == W-1:
                goal = True
                break
            nexts = [(h, w-1), (h, w+1), (h-1, w), (h+1, w)]
            for nh, nw in nexts:
                if state[nh][nw] == "." and not checked[nh][nw]:
                    checked[nh][nw] = True
                    qq.append((nh, nw))
        q = qq
    if goal:
        print(1)
    else:
        ans = 10**14
        for h in range(H):
            for w in range(W):
                if checked[h][w]:
                    d1 = min(h, H-1-h)
                    d2 = min(w, W-1-w)
                    D = min(d1//K + min(d1%K, 1), d2//K + min(d2%K, 1))
                    ans = min(D+1, ans)
        print(ans)


if __name__ == "__main__":
    main()