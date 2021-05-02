import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]


def solve(N):
    if N == 1: return [(1, 1)]
    elif N == 2: return [(1, 1), (2, 1)]
    elif N == 3: return [(1, 1), (2, 1), (3, 1)]
    r = 2; s = 1
    ans = [(1, 1), (2, 1)]
    S = 2
    while True:
        if S + r > N:
            break
        S += r
        r += 1
        ans.append((r, 2))
    
    for i in range(N-S):
        ans.append((r+i, 1))
    
    return ans


for qnum, N in enumerate(Query):
    print("Case #{}:".format(qnum+1))
    ans = solve(N)
    for a, b in ans:
        print(a, b)