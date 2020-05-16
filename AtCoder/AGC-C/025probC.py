import sys
input = sys.stdin.readline

N = int(input())
Ls = []
Rs = []
l0 = 0
r0 = 0
for i in range(N):
    l, r = map(int, input().split())
    Ls.append((l, i))
    Rs.append((r, i))
    if l > 0:
        l0 += 1
    if r < 0:
        r0 += 1

Ls.sort(reverse=True)
Rs.sort()

used = [False]*N
if l0 > r0:
    toright = True
else:
    toright = False 

l = 0
r = 0
ans = 0
now = 0
for _ in range(N):
    if toright:
        while True:
            nl, ind = Ls[l]
            if used[ind]:
                l += 1
            else:
                used[ind] = True
                break
        if nl-now > 0:
            ans += nl - now
            now = nl
        toright = False
    else:
        while True:
            nr, ind = Rs[r]
            if used[ind]:
                r += 1
            else:
                used[ind] = True
                break
        if now-nr > 0:
            ans += now-nr
            now = nr
        toright = True

ans += abs(now)

print(ans)