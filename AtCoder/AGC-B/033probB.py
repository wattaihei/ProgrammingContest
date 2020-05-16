import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
sr, sc = map(int, input().split())
S = input().rstrip()
T = input().rstrip()

ok = True

now_r = sc
for i in range(N):
    if S[i] == 'R':
        if now_r == W:
            ok = False
            break
        now_r += 1
    if T[i] == 'L':
        now_r = max(now_r-1, 1)

now_l = sc
for i in range(N):
    if S[i] == 'L':
        if now_l == 1:
            ok = False
            break
        now_l -= 1
    if T[i] == 'R':
        now_l = min(now_l+1, W)

now_u = sr
for i in range(N):
    if S[i] == 'U':
        if now_u == 1:
            ok = False
            break
        now_u -= 1
    if T[i] == 'D':
        now_u = min(now_u+1, H)

now_d = sr
for i in range(N):
    if S[i] == 'D':
        if now_d == H:
            ok = False
            break
        now_d += 1
    if T[i] == 'U':
        now_d = max(now_d-1, 1)

if ok:
    print("YES")
else:
    print("NO")
