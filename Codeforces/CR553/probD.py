N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: x[1]-x[0])

ans = 0
for i in range(N):
    a, b = AB[i]
    ans += a*i + b*(N-i-1)
print(ans)