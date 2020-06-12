import sys
input = sys.stdin.readline
import math

mod = 10**9+7

N = int(input())
AB = []
Empty = 0
for _ in range(N):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        Empty += 1
    elif y < 0 or (y==0 and x < 0):
        AB.append((math.atan2(-y, -x), -x, -y))
    else:
        AB.append((math.atan2(y, x), x, y))

M = N-Empty
AB.sort()
ind1 = 0
ind2 = 0
ans = 1
while ind1 < M and AB[ind1][1] > 0:
    ind1 += 1
Checked = [False]*M
for i, (t, x, y) in enumerate(AB):
    if x <= 0: break
    if Checked[i]: continue
    just = False
    while ind1 < M:
        update = False
        t1, x1, y1 = AB[ind1]
        ind2 = ind1+1
        while ind2 < M and AB[ind2][1]*y1 == AB[ind2][2]*x1:
            ind2 += 1
        
        if x1*x + y1*y > 0:
            ans = (ans * pow(2, ind2-ind1, mod)) % mod
            ind1 = ind2
        else:
            just = (x1*x + y1*y == 0)
            break
        
    tmp = i
    while tmp < M and not Checked[tmp] and AB[tmp][1]*y == AB[tmp][2]*x:
        Checked[tmp] = True
        tmp += 1
    if just:
        ans = (ans * (pow(2, ind2-ind1, mod) + pow(2, tmp-i, mod) - 1)) % mod
        ind1 = ind2
    else:
        ans = (ans * (pow(2, tmp-i, mod))) % mod

print((ans-1)%mod)