import sys
input = sys.stdin.readline


S = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

for b in B:
    for i in range(3):
        for j in range(3):
            if S[i][j] == b:
                S[i][j] = -1

ok = False
for i in range(3):
    bi = True
    for j in range(3):
        if S[i][j] != -1:
            bi = False
    if bi: ok = True

for j in range(3):
    bi = True
    for i in range(3):
        if S[i][j] != -1:
            bi = False
    if bi: ok = True

if S[0][0] == -1 and S[1][1] == -1 and S[2][2] == -1:
    ok = True
if S[0][2] == -1 and S[1][1] == -1 and S[2][0] == -1:
    ok = True

print("Yes" if ok else "No")