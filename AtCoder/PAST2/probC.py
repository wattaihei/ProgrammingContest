import sys
input = sys.stdin.readline

N = int(input())
state = [list(input().rstrip()) for _ in range(N)]

for h in reversed(range(N-1)):
    for w in range(1, 2*N-2):
        if state[h][w] == "#":
            if state[h+1][w-1] == "X" or state[h+1][w] == "X" or state[h+1][w+1] == "X":
                state[h][w] = "X"

for h in range(N):
    print("".join(state[h]))