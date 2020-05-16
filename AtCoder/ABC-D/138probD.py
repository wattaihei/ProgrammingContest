import sys
input = sys.stdin.readline
sys.setrecursionlimit(900000)


N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
PX = [list(map(int, input().split())) for _ in range(Q)]

def dfs(p, s, checked, score):
    #print(p, s, score)
    ns = s + score[p]
    score[p] += s
    for q in graph[p]:
        if not checked[q]:
            checked[q] = True
            score = dfs(q, ns, checked, score)
    return score


def main():


    score = [0 for _ in range(N)]
    for p, x in PX:
        score[p-1] += x

    checked = [False for _ in range(N)]
    checked[0] = True
    
    ans = dfs(0, 0, checked, score)
    print(' '.join([str(a) for a in ans]))


if __name__ == "__main__":
    main()