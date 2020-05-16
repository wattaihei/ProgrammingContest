
def main():
    H, W = map(int, input().split())
    state = [list(input()) for _ in range(H)]
    checked = [[False]*W for _ in range(H)]

    ans = 0
    for h in range(H):
        for w in range(W):
            if checked[h][w]:   continue
            q = [(h, w)]
            score = [0, 0]
            checked[h][w] = True
            c = 0
            while q:
                score[c%2] += len(q)
                qq = []
                for ph, pw in q:
                    nexts = []
                    if ph != 0: nexts.append((ph-1, pw))
                    if ph != H-1: nexts.append((ph+1, pw))
                    if pw != 0: nexts.append((ph, pw-1))
                    if pw != W-1: nexts.append((ph, pw+1))
                    for nh, nw in nexts:
                        if state[nh][nw] != state[ph][pw] and not checked[nh][nw]:
                            checked[nh][nw] = True
                            qq.append((nh, nw))
                c += 1
                q = qq
            ans += score[0]*score[1]
    print(ans)


if __name__ == "__main__":
    main()