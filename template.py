A, B = map(int, input().split()) # 横に2個
N = int(input()) # 1個
n_list = list(map(int, input().split())) # １行に別れてるとき
s = [int(input()) for _ in range(N)] # 縦にNこ並んでるとき

XY = [list(map(int, input().split())) for _ in range(M)]  # M行N列

S = [int(i) for i in list(input())] # 000を[0, 0, 0]に

import sys
input = sys.stdin.readline

input = sys.stdin.buffer.readline

L = []
R = []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)


# 最大公約数と最小公倍数
from fractions import gcd
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(x, y):
    return (x * y) // gcd(x, y)


# 素因数分解
def prime(n):
    factor = []
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    if n != 1:
        factor.append(n)
    return factor

# 辞書で返すやつ
def prime2(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor


mod = int(1E9+7)


# １０進数を二進数にする
def trans2(n):
    A = bin(n)
    return int(A[2:])


# sorting array
from operator import itemgetter
job = sorted(job, key=itemgetter(0), reverse=True)
job = sorted(job, key=itemgetter(1))
# lambda関数の使い方
inf.sort(key=lambda s: len(s), reverse=True)

# リストの要素数を辞書で返す
import collections
colA = collections.Counter(sumA)

# アルファベット小文字
[chr(i) for i in range(97, 97+26)]
# 大文字
[chr(i) for i in range(65, 65+26)]

# 双方向キュー
from collections import deque

# キュー(FIFO)
from queue import Queue
q = Queue()
q.put(i)
a = q.get()
L = q.qsize()



# numpy 関連
ABarray = np.zeros((N, M), dtype=int) # N行M列の0行列


ABsum = np.sum(ABarray, axis=0) # 行方向を出力(列方向をたす)
both = np.count_nonzero(np.all(ABarray == 1, axis=1)) # 全部1であるような


# WF
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

# A, B: 頂点ペア
# T : 頂点間の長さ
graph = csr_matrix((T, (A, B)), (N+1, N+1))
dist = floyd_warshall(graph, directed=False)


# 順列
from itertools import permutations
# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
# permutations(range(3)) --> 012 021 102 120 201 210

# n^k
from itertools import product
# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111


# N-1辺表示をグラフ表示に
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


# 再帰限界をあげる。デフォルトは1000
import sys
sys.setrecursionlimit(1000000)

# コドフォの場合これもかく
# targetをmain関数に
import threading
if __name__ == "__main__":
    threading.stack_size(1024 * 100000)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()



# コンビネーション
mod = 10**9+7
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 10**6 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

a = cmb(n,r,mod)

# その2
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

# その3
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]


# modを取りながらべき乗する
def power_func(a,n,mod):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res


#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m=mod):
    x = extgcd(a,m)[0]
    return (m+x%m)%m




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