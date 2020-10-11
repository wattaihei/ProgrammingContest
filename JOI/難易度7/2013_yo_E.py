import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Points = [list(map(int, input().split())) for _ in range(N)]

# 座標圧縮
Xs = set()
Ys = set()
Zs = set()
for x0, y0, z0, x1, y1, z1 in Points:
    Xs.add(x0)
    Xs.add(x1)
    Ys.add(y0)
    Ys.add(y1)
    Zs.add(z0)
    Zs.add(z1)

ind_to_co_X = sorted(list(Xs))
ind_to_co_Y = sorted(list(Ys))
ind_to_co_Z = sorted(list(Zs))

co_to_ind_X = {}
co_to_ind_Y = {}
co_to_ind_Z = {}
for i, x in enumerate(ind_to_co_X):
    co_to_ind_X[x] = i
for i, y in enumerate(ind_to_co_Y):
    co_to_ind_Y[y] = i
for i, z in enumerate(ind_to_co_Z):
    co_to_ind_Z[z] = i

lx = len(ind_to_co_X)
ly = len(ind_to_co_Y)
lz = len(ind_to_co_Z)

grid = [[[0]*lz for _ in range(ly)] for _ in range(lx)]

# フラグ立て
for x0, y0, z0, x1, y1, z1 in Points:
    ix0 = co_to_ind_X[x0]
    ix1 = co_to_ind_X[x1]
    iy0 = co_to_ind_Y[y0]
    iy1 = co_to_ind_Y[y1]
    iz0 = co_to_ind_Z[z0]
    iz1 = co_to_ind_Z[z1]

    grid[ix0][iy0][iz0] += 1
    grid[ix0][iy0][iz1] -= 1
    grid[ix0][iy1][iz0] -= 1
    grid[ix1][iy0][iz0] -= 1
    grid[ix0][iy1][iz1] += 1
    grid[ix1][iy0][iz1] += 1
    grid[ix1][iy1][iz0] += 1
    grid[ix1][iy1][iz1] -= 1


ans = 0
for ix, x in enumerate(ind_to_co_X):
    for iy, y in enumerate(ind_to_co_Y):
        for iz, z in enumerate(ind_to_co_Z):
            # imos
            if iz > 0:
                grid[ix][iy][iz] += grid[ix][iy][iz-1]
            if iy > 0:
                grid[ix][iy][iz] += grid[ix][iy-1][iz]
            if ix > 0:
                grid[ix][iy][iz] += grid[ix-1][iy][iz]
            if ix > 0 and iy > 0:
                grid[ix][iy][iz] -= grid[ix-1][iy-1][iz]
            if iy > 0 and iz > 0:
                grid[ix][iy][iz] -= grid[ix][iy-1][iz-1]
            if iz > 0 and ix > 0:
                grid[ix][iy][iz] -= grid[ix-1][iy][iz-1]
            if ix > 0 and iy > 0 and iz > 0:
                grid[ix][iy][iz] += grid[ix-1][iy-1][iz-1]

            if grid[ix][iy][iz] >= K:
                ans += (ind_to_co_X[ix+1]-x) * (ind_to_co_Y[iy+1]-y) * (ind_to_co_Z[iz+1]-z)

print(ans)