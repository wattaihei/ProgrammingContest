import sys
input = sys.stdin.readline


def main():
    N = int(input())
    As = []
    B = []
    C = []
    for i in range(N):
        a, b, c = map(int, input().split())
        As.append((a, i))
        B.append(b)
        C.append(c)
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    Graph = [[] for _ in range(N)]
    checked = [False]*N
    checked[0] = True
    q = [0]
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if not checked[np]:
                    checked[np] = True
                    qq.append(np)
                    Graph[p].append(np)
        q = qq

    As.sort()
    already = [False]*N
    remain = [0]*N
    ans = 0
    for a, node in As:
        if already[node]: continue
        q = [node]
        already[node] = True
        Balance = [0, 0, 0]
        Balance[C[node]-B[node]] += 1
        while q:
            qq = []
            for p in q:
                for np in Graph[p]:
                    if already[np]:
                        if remain[np] > 0:
                            Balance[1] += remain[np]
                        elif remain[np] < 0:
                            Balance[-1] += -remain[np]
                    else:
                        qq.append(np)
                        already[np] = True
                        Balance[C[np]-B[np]] += 1
            q = qq
        if Balance[1] >= Balance[-1]:
            ans += 2*a*(Balance[-1])
            remain[node] = Balance[1] - Balance[-1]
        else:
            ans += 2*a*(Balance[1])
            remain[node] = - Balance[-1] + Balance[1]

    if remain[0] != 0:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()