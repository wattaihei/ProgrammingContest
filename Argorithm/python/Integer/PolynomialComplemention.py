mod = 10**9+7

def op(a, b):
    return a*b % mod

def add(a, b):
    return (a+b) % mod

def inv(a):
    return pow(a, mod-2, mod)

def inverseMatrix(Mat):
    d = len(Mat)
    iMat = [[1 if i==j else 0 for i in range(d)] for j in range(d)]
    for x in range(d):
        # set Mat[x][x] != 0
        y = x
        for i in range(x, d):
            if Mat[i][x] != 0:
                y = i
                break
        Mat[y], Mat[x] = Mat[x], Mat[y]
        iMat[y], iMat[x] = iMat[x], iMat[y]

        # set Mat[x][x] = 1
        inva = inv(Mat[x][x])
        for j in range(d):
            Mat[x][j] = op(Mat[x][j], inva)
            iMat[x][j] = op(iMat[x][j], inva)
        
        # set Mat[i][x] = 0 for i != x
        for i in range(d):
            if i == x: continue
            a = Mat[i][x]
            for j in range(d):
                Mat[i][j] = add(Mat[i][j], -op(Mat[x][j], a))
                iMat[i][j] = add(iMat[i][j], - op(iMat[x][j], a))
    return iMat


def PolynomialComplemention(dic):
    d = len(dic)
    Mat = []
    Arr = []
    for b, c in dic.items():
        Mr = []
        p = 1
        for _ in range(d):
            Mr.append(p)
            p = op(p, b)
        Mat.append(Mr)
        Arr.append(c)
    
    iMat = inverseMatrix(Mat)
    ret = []
    for i in range(d):
        a = 0
        for j in range(d):
            a = add(a, op(iMat[i][j], Arr[j]))
        ret.append(a)
    return ret