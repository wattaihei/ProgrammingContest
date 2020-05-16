
def main():    
    H, W, K = map(int, input().split())
    HW = [list(map(int, input().split())) for _ in range(K)]

    Aw = [H for _ in range(W)]
    Ah = [W for _ in range(H)]
    for h, w in HW:
        Aw[w-1] -= 1
        Ah[h-1] -= 1
    
    s = 0
    for w in range(W):
        s += Aw[w]
        if 2*s >= H*W-K:
            pw = w
            break
    
    s = 0
    for h in range(H):
        s += Ah[h]
        if 2*s >= H*W-K:
            ph = h
            break
    #print(pw, ph)
    ans = 0
    for w in range(W):
        ans += abs(w - pw)*Aw[w]
    for h in range(H):
        ans += abs(h - ph)*Ah[h]
    print(ans)

if __name__ == "__main__":
    main()