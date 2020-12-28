import sys
input = sys.stdin.buffer.readline

mod = 10**9+7

N, X, Y = map(int, input().rstrip().split())
Ps = [[] for _ in range(N)]
for _ in range(N):
    c, w = map(int, input().rstrip().split())
    Ps[c-1].append(w)

NN = 3*10**5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

D = []
for P in Ps:
    if not P: continue
    D.append(sorted(P))

if len(D) < 2:
    ans = 1
else:
    D.sort(key=lambda x:x[0])
    m = D[0][0]
    T = []
    for P in D[1:]:
        l = P[0]
        if l+m > Y: continue
        c = 1
        for p in P[1:]:
            if l+p <= X or m+p <= Y:
                c += 1
        T.append(c)
    
    if m + D[1][0] <= Y:
        c = 1
        for p in D[0][1:]:
            if m+p <= X or D[1][0]+p <= Y:
                c += 1
        T.append(c)
    
    ans = g1[sum(T)]
    for t in T:
        ans = ans * g2[t] % mod

print(ans)