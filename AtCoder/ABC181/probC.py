import sys
input = sys.stdin.buffer.readline


N = int(input())
XY = [list(map(int, input().rstrip().split())) for _ in range(N)]

ok = False
for i in range(N-2):
    x1, y1 = XY[i]
    for j in range(i+1, N-1):
        x2, y2 = XY[j]
        for k in range(j+1, N):
            x3, y3 = XY[k]
            if (x3-x1)*(y2-y1) == (x2-x1)*(y3-y1):
                ok = True
                break
    if ok:
        break

print("Yes" if ok else "No")