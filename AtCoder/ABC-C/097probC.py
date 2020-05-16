def main():
    S = input()
    N = len(S)
    K = int(input())

    S1 = {}
    for i, s in enumerate(S):
        if not s in S1.keys():
            S1[s] = [i]
        else:
            S1[s].append(i)
    alp = sorted(list(S1.keys()))

    c = 0
    for a in alp:
        aset = set()
        inds = S1[a]
        for d in inds:
            up = min(N-d+1, K+1)
            for i in range(up):
                aset.add(S[d:d+i])
        L = len(aset)-1
        if L >= K-c:
            break
        c += L

    for _ in range(10):
        M = '何だこれはもうやめてくれよ'
        for a in aset:
            if a < M:
                M = a
        aset.discard(M)
        if M == '':
            continue
        c += 1
        if c >= K:
            ans = M
            break

    print(ans)



if __name__=='__main__':
    main()