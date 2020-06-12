import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M, x, y = map(int, input().split())
    state = [list(input().rstrip()) for _ in range(N)]
    Query.append((N, M, x, y, state))

for N, M, x, y, state in Query:
    white = 0
    two = 0
    for r in range(N):
        go = False
        for c in range(M):
            if go:
                go = False
                continue
            if c < M-1 and state[r][c] == "." and state[r][c+1] == ".":
                go = True
                two += 1
            elif state[r][c] == ".":
                white += 1
    print(min(two*y+white*x, (2*two+white)*x))