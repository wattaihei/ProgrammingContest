from operator import itemgetter

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    AB[i].sort()

AB.sort(key=itemgetter(0))

c = 0
pa, pb = 0, 0
for a, b in AB:
    if (a, b) != (pa, pb):
        c += 1
    pa, pb = a, b

print(c)