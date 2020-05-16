N, M = map(int, input().split())

mod = 998244353
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 4*10**6 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


A = []
tmp = 0
for i in range(2*M+N+2):
    tmp = (tmp + cmb(N-2+i, N-2)) % mod
    A.append(tmp)

ans = 0
for k in range(min(N, M)+1):
    if (M-k) % 2 != 0: continue
    l = (3*M-k)//2
    a = cmb(N-1+l, N-1) * cmb(N, k)
    b = N * (cmb(N-1, k-1)*A[l-M])
    if l >= M+1:
        b += N * cmb(N-1, k)*A[l-M-1]
    #print(k,a-b)
    ans = (ans + a - b) % mod 
print(ans)

# C = set()
# def calc(d, A):
#     if d == M:
#         t = ""
#         for a in A:
#             t += str(a)
#         C.add(t)
#         return
#     for i in range(N):
#         for j in range(N):
#             if i == j: continue
#             B = A[:]
#             B[i] += 2
#             B[j] += 1
#             calc(d+1, B)
#     return

#calc(0, [0]*N)
#print(len(C))
#print(C)
