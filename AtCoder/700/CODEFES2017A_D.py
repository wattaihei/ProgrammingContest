import sys
input = sys.stdin.buffer.readline

H, W, d = map(int, input().rstrip().split())

RYGB = "RYGB"

if d%2 == 0:
    ans = [["."]*W for _ in range(H)]
    b = d//2
    for sh in range(-1, H+d, d):
        for sw in range(-1, W+d, d):
            color = RYGB[(sh//d + sw//d)%2]
            for dh in range(-b+1, b):
                r = b-abs(dh)-1
                for dw in range(-r, r+2):
                    h = sh + dh; w = sw + dw
                    if 0 <= h < H and 0 <= w < W:
                        ans[h][w] = color
    for sh in range(b-1, H+d, d):
        for sw in range(b-1, W+d, d):
            color = RYGB[(sh//d + sw//d)%2 + 2]
            for dh in range(-b+1, b):
                r = b-abs(dh)-1
                for dw in range(-r, r+2):
                    h = sh + dh; w = sw + dw
                    if 0 <= h < H and 0 <= w < W:
                        ans[h][w] = color
else:
    ans = [["."]*W for _ in range(H)]
    b = d//2
    hsize = (H+W)//d
    Offsets = [
        (0, 0),
        (b+1, b),
        (-b, b+1),
        (1, d)
    ]
    for color_ind, (offset_h, offset_w) in enumerate(Offsets):
        for s in range(-2, 2*hsize+4):
            for t in range(-hsize-3, hsize+4):
                sh = (d+1)*s + (d-1)*t + offset_h
                sw = (d-1)*s - (d+1)*t + offset_w
                if -b <= sh <= H+b and -b <= sw <= W+b:
                    for dh in range(-b, b+1):
                        r = b-abs(dh)
                        for dw in range(-r, r+1):
                            h = sh + dh
                            w = sw + dw
                            if 0 <= h < H and 0 <= w < W:
                                ans[h][w] = RYGB[color_ind]


for row in ans:
    print("".join(row))