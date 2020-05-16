
mod = 10**9+7
# matrix power
def matintersection(matA, matB, mod):
    length = len(matA)
    matR = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                matR[i][j] += matA[i][k]*matB[k][j] % mod
                matR[i][j] %= mod
    return matR

def power_mat(matA, n, mod):
    bi = str(format(n,"b"))#2進表現に
    length = len(matA)
    res = [[1 if i == j else 0 for i in range(length)] for j in range(length)]
    for i in range(len(bi)):
        res = matintersection(res, res, mod)
        if bi[i] == "1":
            res = matintersection(res, matA, mod)
    return res

N, K = map(int, input().split())

D = [[0]*N for _ in range(N)]
for n in range(N):
    for m in range(N):
        D[(m*n)%N][n] += 1
        D[(m+n)%N][n] += 1

A = power_mat(D, K, mod)
print(A[0][0])