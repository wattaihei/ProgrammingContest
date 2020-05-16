import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
state = [list(map(int, input().split())) for _ in range(N)]

ans = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if state[i][j] == 1:
            ans[i][j] = min(A[j], B[i])

for i in range(N):
    for j in range(M):
        print(ans[i][j], end=' ')
    print()