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

    in_black = [[-1]*W for _ in range(H)]
    b = []

    goal = False
    ans = 0
    while not goal:
        ans += 1
        for _ in range(K):
            qq = []
            for h, w in q:
                if h == 0 or h == H-1 or w == 0 or w == W-1:
                    goal = True
                    break
                nexts = [(h, w-1), (h, w+1), (h-1, w), (h+1, w)]
                for nh, nw in nexts:
                    if state[nh][nw] == "#":
                        if in_black[nh][nw] == -1:
                            in_black[nh][nw] = 0
                            b.append((nh, nw))
                        elif in_black[nh][nw] == 1 and not checked[nh][nw]:
                            checked[nh][nw] = True
                            qq.append((nh, nw))
                    elif not checked[nh][nw]:
                        checked[nh][nw] = True
                        qq.append((nh, nw))
            q = qq
        
        if goal: break
        
        for h, w in q:
            if h == 0 or h == H-1 or w == 0 or w == W-1:
                goal = True
                break
            nexts = [(h, w-1), (h, w+1), (h-1, w), (h+1, w)]
            for nh, nw in nexts:
                if state[nh][nw] == "#" and in_black[nh][nw] == -1:
                    in_black[nh][nw] = 0
                    b.append((nh, nw))
        
        if goal: break
        
        for i in range(K):
            bb = []
            for h, w in b:
                in_black[h][w] = 1
                if i == 0:
                    checked[h][w] = True
                    q.append((h, w))
                nexts = []
                if h != 0: nexts.append((h-1, w))
                if h != H-1: nexts.append((h+1, w))
                if w != 0: nexts.append((h, w-1))
                if w != W-1: nexts.append((h, w+1))
                for nh, nw in nexts:
                    if state[nh][nw] == "#" and in_black[nh][nw] == -1:
                        in_black[nh][nw] = 0
                        bb.append((nh, nw))
            b = bb

    print(ans)


if __name__ == "__main__":
    main()