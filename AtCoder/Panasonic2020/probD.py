import sys
input = sys.stdin.readline

N = int(input())
Alp = [chr(i) for i in range(97, 97+26)]

ans = []
def dfs(d, maxi, T):
    if d == N-1:
        ans.append(T)
        return
    for i in range(maxi+2):
        dfs(d+1, max(maxi, i), T + Alp[i])

dfs(0, 0, "a")
print(*ans, sep='\n')