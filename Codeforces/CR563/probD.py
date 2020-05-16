

def main():
    N, X = map(int, input().split())
    L = 2**N-1

    if X <= L:
        P = [0]
        checked = [False]*(L+1)
        checked[0] = True
        for n in range(1, L+1):
            inv = n ^ X
            if not checked[inv]:
                P.append(n)
            checked[n] = True
            checked[inv] = True
    else:
        P = [0]
        for n in range(1, L+1):
            P.append(n)

    ans = []
    for i in range(len(P)-1):
        ans.append(P[i+1]^P[i])

    if not ans:
        print(0)
    else:
        print(len(ans))
        print(' '.join([str(a) for a in ans]))

if __name__ == "__main__":
    main()