N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

c = 0
for a, b in AB:
    c += min(a//2, b)
print(c)