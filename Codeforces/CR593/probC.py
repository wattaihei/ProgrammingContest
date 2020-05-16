N = int(input())

ans = [[] for _ in range(N)]
for i in range(N):
    for j in range(1, N+1):
        if i%2 == 0:
            ans[j-1].append(N*i+j)
        else:
            ans[N-j].append(N*i+j)

for i in range(N):
    for j in range(N):
        print(ans[i][j], end=' ')
    print()