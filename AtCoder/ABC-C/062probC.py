H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    ans = 0
else:
    hp = [H//3, H//3+1]
    ans = H*W
    for h in hp:
        S1 = h*W
        if ((H-h)*W) % 2 == 0:
            ans = min(abs((H-h)*W//2 - S1), ans)
        else:
            S2 = (H-h-1)*W//2 
            S3 = (H-h+1)*W//2
            a = max([abs(S2-S1), abs(S1-S3), abs(S3-S2)])
            S4 = (H-h)*(W+1)//2
            S5 = (H-h)*(W-1)//2
            b = max([abs(S1-S4), abs(S4-S5), abs(S5-S1)])
            ans = min([ans, a, b])
    wp = [W//3, W//3+1]
    for w in wp:
        S1 = H*w
        if ((W-w)*H) % 2 == 0:
            ans = min(abs((W-w)*H//2 - S1), ans)
        else:
            S2 = (W-w-1)*H//2 
            S3 = (W-w+1)*H//2
            a = max([abs(S2-S1), abs(S1-S3), abs(S3-S2)])
            S4 = (W-w)*(H+1)//2
            S5 = (W-w)*(H-1)//2
            b = max([abs(S1-S4), abs(S4-S5), abs(S5-S1)])
            ans = min([ans, a, b])
print(ans)

