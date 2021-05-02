MAX = 5

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

# Dic = {}
# def subnaive(a, l, N):
#     if l == MAX:
#         return a
#     ret = 0
#     for i in range(N+1):
#         ret = add(ret, subnaive(op(i, a), l+1, N-i))
#     return ret

def subnaive2(N):
    dp = [0]*(N+1)
    dp[0] = 1
    for _ in range(MAX):
        ndp = [0]*(N+1)
        for i in range(N+1):
            for j in range(i+1, N+1):
                ndp[j] = add(ndp[j], op(j-i, dp[i]))
        dp = ndp
    ret = [0]*(N+1)
    for i in range(N+1):
        ret[i] = add(ret[i-1], dp[i])
    return ret

def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 3*10**5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


Dic = subnaive2((3*MAX+1) * (1<<MAX))
def naive(N):
    ret = 0
    for i in range(0, N+1, 2):
        r = cmb(i//2+MAX-1, MAX-1)
        # if not N-i in Dic:
        #     # Dic[N-i] = subnaive(1, 0, N-i)
        #     Dic[N-i] = subnaive2(N)
        ret = add(ret, op(Dic[N-i],r))
    # print(N, ret)
    return ret

dics = [{} for _ in range(1<<MAX)]
for i in range((3*MAX+1) * (1<<MAX)):
    dics[i%(1<<MAX)][i] = naive(i)

Pols = []
for dic in dics:
    Pols.append(PolynomialComplemention(dic))

def solve(n):
    ans = 0
    base = 1
    for p in Pols[n%(1<<MAX)]:
        ans = (ans + base * p) % mod
        base = base * n % mod
    return ans

# for pl in Pols:
#     print(pl)

# for n in range(0, 200):
#     ans1 = solve(n)
#     ans2 = naive(n)
#     print(n, ans1-ans2, ans1, ans2)


import sys
input = sys.stdin.buffer.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    print(solve(N))