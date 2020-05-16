import heapq as hp

mod = 10**9+7

# modを取りながらべき乗する
def power_func(a,n,mod=mod):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res


def main():
    N, A, B = map(int, input().split())
    P = list(map(int, input().split()))

    if A == 1:
        P.sort()
        for p in P:
            print(p)
        return
    
    maxP = max(P)
    q = []
    for i, p in enumerate(P):
        hp.heappush(q, p)

    c = 0
    while True:
        p = hp.heappop(q)
        if p*A >= maxP:
            hp.heappush(q, p)
            break
        c += 1
        hp.heappush(q, p*A)
        if c == B:
            for _ in range(N):
                print(hp.heappop(q))
            return

    rem = (B-c)%N
    loop = (B-c)//N
    Bigger = []
    for _ in range(rem):
        p = hp.heappop(q)
        Bigger.append(p*A%mod)
    
    const = power_func(A, loop)
    while q:
        p = hp.heappop(q)
        print(p*const%mod)
    
    for p in Bigger:
        print(p*const%mod)



if __name__ == "__main__":
    main()