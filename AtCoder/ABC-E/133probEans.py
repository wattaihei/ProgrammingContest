N,K = map(int,input().split())
AB = [list(map(int,input().split())) for _ in [0]*(N-1)]
mod = 10**9+7

E = [[] for _ in [0]*N]
for a,b in AB:
    E[a-1].append(b-1)
    E[b-1].append(a-1)

print(E)
ans = K
q = [0]
V = [False for _ in [0]*N] # チェックしたかどうかのリスト
V[0] = True
while q: # 次のやつが有る限り回す
    print('q', q)
    qq = [] # 次に進むやつ。これに追加していく
    for i in q:
        l = K-2+(i==0) # i = 0ならK-1, それ以外ならK-2
        for j in E[i]:
            print('j', j)
            if V[j]:continue # もうチェックしてたら通りすギル
            ans = ans * l % mod 
            if ans == 0:break # 0になったら存在しないってことになる
            qq.append(j)
            V[j] = True
            l -= 1 
    q = qq # 進める
print(ans)
