xa, ya, xb, yb, T, V = map(int, input().split())
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

D = T*V
ans = 'NO'
for x, y in XY:
    da2 = (x-xa)**2+(y-ya)**2
    db2 = (x-xb)**2+(y-yb)**2
    #print(da2, db2, D**2)
    if 4*da2*db2 <= (D**2-da2-db2)**2:
        ans = 'YES'
        break
print(ans)