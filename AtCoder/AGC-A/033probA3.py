import sys
input = sys.stdin.readline

B = int(1E8)

def main():

    H, W = map(int, input().split())
    
    l = 0
    q = []
    checked = []
    for h in range(H):
        S = input()
        L = []
        for w in range(W):
            if S[w] == '#':
                l += 1
                L.append(True)
                q.append(B*h+w)
            else:
                L.append(False)
        checked.append(L)

    Next = [[[] for _ in range(W)] for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if h != 0:
                Next[h][w].append(B*(h-1) + w)
            if h != H-1:
                Next[h][w].append(B*(h+1) + w)
            if w != 0:
                Next[h][w].append(B*h + w-1)
            if w != W-1:
                Next[h][w].append(B*h + w+1)

    c = -1
    for _ in range(H+W+2):
        qq = []
        if len(q) == 0:
            break
        for hw in q:
            h, w = hw//B, hw%B
            for nhw in Next[h][w]:
                nh, nw = nhw//B, nhw%B
                if not checked[nh][nw]:
                    qq.append(B*nh + nw)
                    checked[nh][nw] = True
        q = qq
        c += 1

    print(c)


if __name__ == "__main__":
    main()