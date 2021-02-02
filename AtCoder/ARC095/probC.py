
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    from itertools import permutations

    H, W = map(int, input().rstrip().split())
    Ss = [list(input().rstrip()) for _ in range(H)]

    ok = False
    for P in permutations(range(H), (H+1)//2):
        selected = [False]*H
        A = []
        for p in P:
            selected[p] = True
            A.append(p)
        for i in range(H):
            if not selected[i]: A.append(i)
        
        T = {}
        for w in range(W):
            s = ""
            for h in A:
                s = s + Ss[h][w]
            r = s[::-1]
            if T.get(s, 0) > 0:
                T[s] -= 1
            else:
                T[r] = T.get(r, 0) + 1
        
        if sum(T.values()) < 2:
            ok = True
            break

    print("YES" if ok else "NO")