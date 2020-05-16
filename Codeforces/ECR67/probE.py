import sys
import threading
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dp = [1]*N
checked1 = [False]*N
checked = [False]*N
ans = 0

def dfs(p):
    checked1[p] = True
    for np in graph[p]:
        if not checked1[np]:
            dfs(np)
            dp[p] += dp[np]

def reroot(p, score):
    global ans
    ans = max(ans, score)
    checked[p] = True
    for np in graph[p]:
        if not checked[np]:
            root = dp[p]
            goto = dp[np]
            dp[np] = root
            dp[p] = root - goto
            reroot(np, score + root - 2*goto)
            dp[np] = goto
            dp[p] = root

def main():
    dfs(0)
    reroot(0, sum(dp))
    print(ans)

if __name__ == "__main__":
    threading.stack_size(1024 * 100000)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
