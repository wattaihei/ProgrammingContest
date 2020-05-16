import sys
input = sys.stdin.readline

N = int(input())
state = [list(input().rstrip()) for _ in range(N)]

c = 0
for h in range(N):
    for w in reversed(range(N)):
        if state[h][w] == ".":
            c += 1
            for nw in range(w+1):
                state[h][nw] = "o"
            if h == N-1:
                break
            for nw in range(w, N):
                state[h+1][nw] = "o"
print(c)