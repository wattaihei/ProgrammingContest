N = int(input())
p = list(map(int, input().split()))


c = 0
for i in range(1, N-1):
    com = sorted([p[i-1], p[i], p[i+1]])
    if com[1] == p[i]:
        c += 1

print(c)