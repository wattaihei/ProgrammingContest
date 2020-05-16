import sys
input = sys.stdin.readline

N = int(input())
remain = 0
A = []
L = []
for _ in range(N):
    a, l = map(int, input().split())
    A.append(a)
    L.append(l)
    remain += l*len(str(a))
B = int(input())

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


# modを取りながらべき乗する
def power_func(a,n,mod):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res

ans = 0
for a, l in zip(A, L):
    k = len(str(a))
    remain -= k*l
    matrix = power_mat([[10**k%B, 1], [0, 1]], l-1, B)
    ans += (matrix[0][0] + matrix[0][1]) % B * a % B * power_func(10, remain, B) % B
    ans %= B
print(ans)