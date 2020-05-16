
def main():
    H, W = map(int, input().split()) # 横に2個
    checked = [[False if a == '.' else True for a in list(input()+'#')] for i in range(H)]
    checked.extend([[True]*(W+1)])
    qs = [(h, w) for h in range(H) for w in range(W) if checked[h][w]]

    c = 0
    for _ in range(2000):
        qqs = []
        for h,w in qs:
            checked[h][w] = True
            if not checked[h-1][w]:
                qqs.append((h-1, w))
            if not checked[h+1][w]:
                qqs.append((h+1, w))
            if not checked[h][w-1]:
                qqs.append((h, w-1))
            if not checked[h][w+1]:
                qqs.append((h, w+1))
        if not qqs:
            break
        c += 1
        qs = qqs

    print(c)

if __name__=='__main__':
    main()