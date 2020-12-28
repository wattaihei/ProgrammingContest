import sys
input = sys.stdin.buffer.readline


def sim(ax, ay, bx, by, cx, cy):
    points = [(ax, ay), (bx, by), (cx, cy)]
    if not (0, 0) in points:
        return 0
    if not (0, 1) in points:
        return 1
    if not (1, 0) in points:
        return 2
    return 3

def is_near(ax, ay, bx, by, cx, cy):
    mx = min([ax, bx, cx])
    my = min([ay, by, cy])
    return -1 <= mx <= 1 and -1 <= my <= 1

def solve_near(ax, ay, bx, by, cx, cy):
    mx = min([ax, bx, cx])
    my = min([ay, by, cy])
    D = {
        1 : {
            -1 : [3, 2, 3, 2],
            0: [3, 2, 3, 2],
            1: [4, 3, 3, 3]
        },
        0: {
            -1: [1, 1, 2, 2],
            0: [1, 1, 1, 0],
            1 : [3, 3, 2, 2]
        },
        -1 : {
            -1 : [2, 2, 2, 3],
            0 : [1, 2, 1, 2],
            1 : [3, 3, 2, 2]
        }
    }
    return D[my][mx][sim(ax-mx, ay-my, bx-mx, by-my, cx-mx, cy-my)]

# 余ってる時
def line_solve(ax, ay, bx, by, cx, cy):
    if is_near(ax, ay, bx, by, cx, cy):
        return solve_near(ax, ay, bx, by, cx, cy)
    d = min([ax, bx, cx])
    return 2*(d-2) + 1  + solve_near(-ay+1, ax-d+1, -by+1, bx-d+1, -cy+1, cx-d+1)


def solve_p(ax, ay, bx, by, cx, cy):
    ret = 0
    dx = min([ax, bx, cx])
    dy = min([ay, by, cy])
    if dx < dy:
        ax, ay, bx, by, cx, cy = ay, ax, by, bx, cy, cx
        dx, dy = dy, dx
    if dy > 0:
        dy -= 1
    return 1 + 2*dy + line_solve(ax-dy, ay-dy, bx-dy, by-dy, cx-dy, cy-dy)


def solve(ax, ay, bx, by, cx, cy):
    if is_near(ax, ay, bx, by, cx, cy):
        return solve_near(ax, ay, bx, by, cx, cy)
    mx = min([ax, bx, cx])
    my = min([ay, by, cy])
    if mx >= 0:
        if my >= 0:
            return solve_p(ax, ay, bx, by, cx, cy)
        else:
            return solve_p()

    

Q = int(input())
for _ in range(Q):
    A = list(map(int, input().rstrip().split()))
    print(solve(*A))