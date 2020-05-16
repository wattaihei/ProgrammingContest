N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

Colors = [0]*(1000002)

for a,b in AB:
    Colors[a] += 1
    Colors[b+1] -= 1

Colors2 = []
s = 0
for c in Colors:
    s += c
    Colors2.append(s)

print(max(Colors2))