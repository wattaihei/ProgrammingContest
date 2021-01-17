import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split())
Ss = [list("." + input().rstrip() + ".") for _ in range(H)]

Ss = [list("."*(W+2))] + Ss + [list("."*(W+2))]

for h in range(1, H+1):
    for w in range(1, W+1):
        cnt = 0
        for dw in range(-1, 2):
            for dh in range(-1, 2):
                if Ss[h+dh][w+dw] == "#": cnt += 1
        print(cnt, end="")
    print()