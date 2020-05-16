N = int(input())
state = [list(input()) for _ in range(N)]

ans = 0
for k in range(9):
    con = False
    for i in range(N):
        if state[i][k] == "o":
            con = True
        else:
            if con:
                ans += 1
            con = False
        if state[i][k] == "x":
            ans += 1
    if con:
        ans += 1

print(ans)     