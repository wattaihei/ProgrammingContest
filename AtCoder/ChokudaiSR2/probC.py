N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b in AB:
    c = a+b
    ans = max(ans, c)
print(ans)