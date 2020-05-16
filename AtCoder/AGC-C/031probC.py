import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())

remain = []
must_change = []
for n in range(N):
    if (A^B)&(1<<n):
        must_change.append(n)
    else:
        remain.append(n)

ans = []
def dfs(ind, bit, end):
    if ind == 0:
        n = must_change[0]
        bit = dfs(ind+1, bit, False)
        bit = dfs(ind+1, bit^(1<<n), True)
    elif ind < len(must_change):
        n1, n2 = must_change[ind], must_change[ind+1]
        if end:
            bit = dfs(ind+2, bit, False)
            bit = dfs(ind+2, bit^(1<<n2), False)
            bit = dfs(ind+2, bit^(1<<n1), False)
            bit = dfs(ind+2, bit^(1<<n2), True)
        else:
            bit = dfs(ind+2, bit, False)
            bit = dfs(ind+2, bit^(1<<n1), False)
            bit = dfs(ind+2, bit^(1<<n2), False)
            bit = dfs(ind+2, bit^(1<<n1), False)
    elif ind < N:
        n = remain[ind-len(must_change)]
        bit = dfs(ind+1, bit, end)
        bit = dfs(ind+1, bit^(1<<n), end)
    else:
        ans.append(bit)
    
    return bit


if len(must_change)%2 == 0:
    print("NO")
else:
    dfs(0, A, False)
    print("YES")
    print(*ans)