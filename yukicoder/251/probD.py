mod = 10**9+7

# matrix power
def matintersection(matA, matB, mod=mod):
    length = len(matA)
    matR = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                matR[i][j] += matA[i][k]*matB[k][j] % mod
                matR[i][j] %= mod
    return matR

def power_mat(matA, n, mod=mod):
    bi = str(format(n,"b"))#2進表現に
    length = len(matA)
    res = [[1 if i == j else 0 for i in range(length)] for j in range(length)]
    for i in range(len(bi)):
        res = matintersection(res, res, mod)
        if bi[i] == "1":
            res = matintersection(res, matA, mod)
    return res

N = int(input())

inv6 = pow(6, mod-2, mod)
vec = [1]
for _ in range(5):
    c = 0
    for v in vec:
        c += v
    vec.append(c*inv6%mod)

if N <= 5:
    ans = vec[N]
else:
    vec = vec[::-1]
    mat = [[inv6, inv6, inv6, inv6, inv6, inv6],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0]
    ]
    ret_mat = power_mat(mat, N-5, mod)
    tmp = 0
    for i in range(6):
        tmp = (tmp + ret_mat[0][i]*vec[i]) % mod
    ans = tmp % mod
print(ans)