import sys
input = sys.stdin.buffer.readline

INF = 10**18

N = int(input())
XY = [list(map(int, input().rstrip().split())) for _ in range(N)]

m1 = INF
m2 = INF
M1 = 0
M2 = 0
Xs = []
for i, (x, y) in enumerate(XY):
    if x > y: y, x = x, y
    Xs.append((x, i))
    Xs.append((y, i))
    M1 = max(M1, x)
    m1 = min(m1, x)
    M2 = max(M2, y)
    m2 = min(m2, y)

ans = (M1-m1)*(M2-m2)
Xs.sort()

in_dic = {}
mind = 0
for ind, (x, k) in enumerate(Xs):
    if k in in_dic:
        in_dic[k] += 1
    else:
        in_dic[k] = 1
    if len(in_dic) == N:
        mind = ind
        break

for lind, (x, k) in enumerate(Xs):
    if in_dic[k] == 1:
        del in_dic[k]
        while mind+1 < 2*N:
            mind += 1
            y, l = Xs[mind]
            if l in in_dic:
                in_dic[l] += 1
            else:
                in_dic[l] = 1
                break
    else:
        in_dic[k] -= 1
    
    if mind >= 2*N or len(in_dic) < N:
        break
    ans = min(ans, (Xs[mind][0] - Xs[lind+1][0])*(M2-m1))

print(ans)