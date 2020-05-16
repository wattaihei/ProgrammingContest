import sys
input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    state = [list(map(int, input().split())) for _ in range(H)]
    mod = 10**9 + 7

    q = []
    next = [[[] for _ in range(W)] for _ in range(H)]
    pre = [[[] for _ in range(W)] for _ in range(H)]
    for w in range(W):
        for h in range(H):
            nexts = []
            if h != 0: nexts.append((h-1, w))
            if h != H-1: nexts.append((h+1, w))
            if w != 0: nexts.append((h, w-1))
            if w != W-1: nexts.append((h, w+1))
            peak = True
            for nh, nw in nexts:
                if state[h][w] > state[nh][nw]:
                    next[h][w].append((nh, nw))
                if state[h][w] < state[nh][nw]:
                    peak = False
                    pre[h][w].append((nh, nw))
            if peak:
                q.append((h, w))

    score = [[1]*W for _ in range(H)]
    checked = [[False]*W for _ in range(H)]
    for h, w in q:
        checked[h][w] = True
    while q:
        qq = []
        for ph, pw in q:
            for nh, nw in pre[ph][pw]:
                score[ph][pw] = (score[ph][pw] + score[nh][nw]) % mod
            for nh, nw in next[ph][pw]:
                if checked[nh][nw]:
                    continue
                all_checked = True
                for qh, qw in pre[nh][nw]:
                    if not checked[qh][qw]:
                        all_checked = False
                        break
                if all_checked:
                    checked[nh][nw] = True
                    qq.append((nh, nw))
        q = qq

    ans = 0
    for h in range(H):
        for w in range(W):
            ans = (ans + score[h][w]) % mod

    print(ans)


if __name__ == "__main__":
    main()