N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


ok = True
ans1 = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    r = 0
    for j in range(M):
        if A[i][j] == 1:
            if j == M-1:
                if r == 0:
                    ok = False
            elif i < N-1 and A[i][j+1] == 1:
                ans1[i][j] = True
            r += 1
        else:
            if r == 1:
                ok = False
            r = 0
ans2 = [[False for _ in range(M)] for _ in range(N)]
for j in range(M):
    r = 0
    for i in range(N):
        if A[i][j] == 1:
            if i == N-1:
                if r == 0:
                    ok = False
            elif i < N-1 and A[i+1][j] == 1:
                ans2[i][j] = True
            r += 1
        else:
            if r == 1:
                ok = False
            r = 0

if not ok:
    print(-1)
else:
    ans = []
    for i in range(N-1):
        for j in range(M-1):
            if ans1[i][j] and ans2[i][j] and A[i+1][j+1] == 1:
                ans.append([i+1, j+1])
    print(len(ans))
    for x, y in ans:
        print(x, y)
