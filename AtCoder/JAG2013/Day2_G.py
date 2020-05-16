import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N_, Q = map(int, input().split())
P = list(map(lambda x:int(x)-1, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]
mod = 10**9+7

now = [i for i in range(N_)]
Ps = [now]
for i in range(41):
    next = [None]*N_
    ok = True
    for j in range(N_):
        next[j] = P[now[j]]
        if next[j] != j:
            ok = False
    if ok:
        cycle = i+1
        break
    Ps.append(next)
    now = next

# 累積わ
Qs = []
for i in range(cycle):
    q = [0]
    pre = 0
    for p in Ps[i]:
        pre += p+1
        q.append(pre)
    Qs.append(q)

# SegTree
N = 1
while N < N_: N *= 2

SEG = []
for i in range(cycle):
    seg = [None]*(2*N-1)
    for j in range(N):
        if j >= N_:
            seg[j+N-1] = False
        elif Ps[i][j] == j:
            seg[j+N-1] = True
        else:
            seg[j+N-1] = False
    k = N - 1
    while k > 0:
        for i in range((k-1)//2, k):
            seg[i] = seg[2*i+1] and seg[2*i+2]
        k = (k-1)//2
    SEG.append(seg)

def query(i, l, r, k=0, a=0, b=N):
    if b <= l or r <= a:
        return True
    if l <= a and b <= r:
        return SEG[i][k]
    else:
        vl = query(i, l, r, k*2+1, a, (a+b)//2)
        vr = query(i, l, r, k*2+2, (a+b)//2, b)
        return vl and vr

def main():
    for l, r in Query:
        todo = cycle
        for i in range(1, cycle):
            if query(i, l-1, r):
                todo = i
                break
        ret = 0
        for i in range(todo):
            ret = (ret + Qs[i][r] - Qs[i][l-1]) % mod
        print(ret)

if __name__ == "__main__":
    main()