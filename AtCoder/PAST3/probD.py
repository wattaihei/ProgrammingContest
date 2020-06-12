import sys
input = sys.stdin.readline

N = int(input())
state = [list(input().rstrip()) for _ in range(5)]

ans = ""
for n in range(N):
    now = -1
    l, m, r = 4*n+1, 4*n+2, 4*n+3
    if state[3][m] == "#":
        now = 1
    elif state[4][m] == ".":
        if state[0][m] == "#":
            now = 7
        else:
            now = 4
    elif state[2][m] == ".":
        now = 0
    elif state[1][l] == "#":
        # 5, 6, 8, 9
        if state[1][r] == "#":
            if state[3][l] == "#":
                now = 8
            else:
                now = 9
        else:
            if state[3][l] == "#":
                now = 6
            else:
                now = 5
    else:
        # 0, 2, 3
        if state[3][l] == "#":
            now = 2
        else:
            now = 3
    ans += str(now)

print(ans)