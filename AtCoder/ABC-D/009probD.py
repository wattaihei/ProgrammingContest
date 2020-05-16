import sys
input = sys.stdin.readline

K, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))


def mat_c(A, B):
    k = len(A)
    ret = [[0]*k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            for l in range(k):
                ret[i][j] ^= A[i][l]&B[l][j]
    return ret

# modを取りながらべき乗する
def power_func(A,n):
    bi=str(format(n,"b"))#2進表現に
    k = len(A)
    res = A
    for i in range(1, len(bi)):
        res = mat_c(res, res)
        if bi[i]=="1":
            res = mat_c(res, A)
    return res

def main():
    if M <= K:
        ans = A[M-1]
    else:
        mat = [[0]*K for _ in range(K)]
        for j in range(K-1):
            mat[j+1][j] = (1<<32)-1
        for j, a in enumerate(C):
            mat[0][j] = a
        retmat = power_func(mat, M-K)
        ans = 0
        for j, a in enumerate(A):
            ans ^= retmat[0][K-1-j]&a

    print(ans)

if __name__ == "__main__":
    main()