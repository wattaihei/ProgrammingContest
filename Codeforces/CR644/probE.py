import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    state = [list(input().rstrip()) for _ in range(N)]
    Query.append((N, state))

for N, state in Query:
    ok = True
    for h in range(N-1):
        for w in range(N-1):
            if state[h][w] == "1" and state[h+1][w] == "0" and state[h][w+1] == "0":
                ok = False
    print("YES" if ok else "NO")