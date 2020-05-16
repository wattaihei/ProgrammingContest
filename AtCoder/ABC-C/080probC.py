N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

def dfs(i, A, ans):
    if i == 10:
        ans.append(A)
        return ans
    B = A[:]
    B.append(0)
    ans = dfs(i+1, B, ans)
    C = A[:]
    C.append(1)
    ans = dfs(i+1, C, ans)
    return ans

def main():
    D = dfs(0, [], [])
    for ind, A in enumerate(D):
        if ind == 0:
            continue
        gain = 0
        for i in range(N):
            c = 0
            for day in range(10):
                c += F[i][day]*A[day]
            gain += P[i][c]
        if ind == 1:
            ans = gain
            continue
        ans = max(ans, gain)

    print(ans)

if __name__ == "__main__":
    main()