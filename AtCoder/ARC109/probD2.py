import sys
input = sys.stdin.buffer.readline

def solve(x, y):
    x = x - (x//3) - 1 if x >= 0 else x + (2-x)//3 - 1
    y = y - (y//3) - 1 if y >= 0 else y + (2-y)//3 - 1
    if (x, y) == (0, 0): return 0
    if (x, y) == (1, 1): return 1
    ret = max([x, -x, y, -y])
    if x == y:
        ret += 1
    return ret

Q = int(input())
for _ in range(Q):
    ax, ay, bx, by, cx, cy = list(map(int, input().rstrip().split()))
    print(solve(ax+bx+cx, ay+by+cy))