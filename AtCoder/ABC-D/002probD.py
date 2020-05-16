N, M = map(int, input().split())
friend = [[False]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a-1][b-1] = True
    friend[b-1][a-1] = True


def search(p, L, ans):
    if p == N:
        if len(L) < 2:
            return ans
        for l1 in L:
            for l2 in L:
                if l1 != l2 and not friend[l1][l2]:
                    return ans
        return max(ans, len(L))
    ans = search(p+1, L, ans)
    ans = search(p+1, L+[p], ans)
    return ans

ans = search(0, [], 1)
print(ans)