N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

i = 0
c = 0
for i in range(N):
    a, b = AB.pop()
    a += c
    if a % b != 0:
        c += b - a % b
print(c)