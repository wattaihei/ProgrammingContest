N, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

def dfs(n, s, L, dic):
    if n == len(L):
        if not s in dic.keys():
            dic[s] = 1
        else:
            dic[s] += 1
        return dic
    dic = dfs(n+1, s, L, dic)
    dic = dfs(n+1, s+L[n], L, dic)
    return dic

def main():
    dic1 = dfs(0, 0, A[:N//2], {})
    dic2 = dfs(0, 0, A[N//2:], {})
    ans = 0
    for num, v in dic1.items():
        if num > X: continue
        pair = X - num
        if pair in dic2.keys():
            ans += v*dic2[pair]
    print(ans)

if __name__ == "__main__":
    main()