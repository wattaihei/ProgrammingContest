A, B = map(int, input().split())

Primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def dfs(p, L, now, ans):
    if p == len(L):
        ans.append(now)
        return ans
    ans = dfs(p+1, L, now+[L[p]], ans)
    ans = dfs(p+1, L, now, ans)
    return ans

def main():
    O = []
    E = []
    for a in range(A, B+1):
        if a%2 == 0:
            E.append(a)
        else:
            O.append(a)
    E.append(None)

    ans = 0
    Ls = dfs(0, O, [], [])
    for e in E:
        K = [e]
        if e is None:
            K = []
        for L in Ls:
            nL = L + K
            ok = True
            for p in Primes:
                c = 0
                for l in nL:
                    if l%p == 0:
                        c += 1
                if c > 1:
                    ok = False
                    break
            if ok:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()