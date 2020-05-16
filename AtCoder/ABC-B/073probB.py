N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for l, r in LR:
    ans += r-l+1
print(ans)