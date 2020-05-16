import sys
input = sys.stdin.readline

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i, (a, b) in enumerate(AB):
    if a*b >= s:
        mi, ma, mb = i, a, b
        s = a*b

ans = mi+1
#print(ans)
for i, (a, b) in enumerate(AB):
    if i == mi:
        continue
    z1 = ma//b + 1 if ma%b!=0 else ma//b
    z2 = a//mb + 1 if a%mb!=0 else a//mb
    #print(i, z1, z2)
    if z1 <= z2:
        ans = -1
        break
print(ans)