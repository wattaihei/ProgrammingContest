import threading
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter

N = int(input())
state = list(map(int, input().split()))
F = list(map(int, input().split()))
INF = 10**13

graph = [[] for _ in range(N)]
for i, f in enumerate(F):
    graph[f-1].append(i+1)

def dfs(p):
    leaf = True
    if state[p] == 0:
        score = 0
        for lp in graph[p]:
            score += dfs(lp)
            leaf = False
    else:
        score = INF
        for lp in graph[p]:
            score = min(score, dfs(lp))
            leaf = False
    if leaf:
        return 1
    else:
        return score

def main():
    ans = N-len(Counter(F)) - dfs(0) + 1
    print(ans)

if __name__ == "__main__":
    threading.stack_size(128*1024*1024)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()