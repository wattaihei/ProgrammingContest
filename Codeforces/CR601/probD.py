import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    R, C, K = map(int, input().split())
    state = [list(input().rstrip()) for _ in range(R)]
    Query.append((R, C, K, state))

Alp = [chr(i) for i in range(97, 97+26)] + [chr(i) for i in range(65, 65+26)] + [str(i) for i in range(10)]

for R, C, K, state in Query:
    count = 0
    for r in range(R):
        for c in range(C):
            if state[r][c] == "R":
                count += 1
    ans = [[None]*C for _ in range(R)]
    Limit = [count//K+1 if i<(count%K) else count//K  for i in range(K)]
    ind = 0
    now = 0
    for r in range(R):
        if r%2 == 0:
            seq = list(range(C))
        else:
            seq = list(reversed(range(C)))
        for c in seq:
            ans[r][c] = Alp[ind]
            if state[r][c] == "R":
                now += 1
            if now == Limit[ind] and ind != K-1:
                ind += 1
                now = 0
    for s in ans:
        print("".join(s))