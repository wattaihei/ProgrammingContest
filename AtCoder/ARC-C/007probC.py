A = [1 if a == 'o' else 0 for a in list(input())]
N = len(A)

def search(d, L, ans):
    if d == N:
        checked = [False]*N
        for l in L:
            for i in range(N):
                if A[i] == 1:
                    checked[(i+l)%N] = True
        ok = True
        for i in range(N):
            if not checked[i]:
                ok = False
        if ok:
            ans = min(ans, len(L))
        return ans
    ans = search(d+1, L, ans)
    ans = search(d+1, L+[d], ans)
    return ans

ans = search(0, [0], N)
print(ans)