N = int(input())
Hol = [list(map(int, input().split('/'))) for _ in range(N)]

m, d = 1, 1
frust = 0
seq = 0
ans = 0

Month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(366):
    if [m, d] in Hol:
        if i%7 in [0, 6]:
            frust += 1
        seq += 1
    else:
        if i%7 in [0, 6]:
            seq += 1
        elif frust > 0:
            seq += 1
            frust -= 1
        else:
            seq = 0
    ans = max(ans, seq)
    d += 1
    if Month[m-1] < d:
        m += 1
        d = 1

print(ans)