
def solve():
    import sys
    input = sys.stdin.buffer.readline

    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().rstrip().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    Centers = set()
    for i in range(N):
        if len(graph[i]) > 1:
            Centers.add(i)

    if N == 2:
        return [1, 2]
    
    if len(Centers) == 1:
        # star
        ans = [1]
        for i in range(3, N):
            ans.append(i)
        ans.append(2)
        ans.append(N)
        return ans
    
    graph2 = {}
    
    edge = []
    for i in Centers:
        graph2[i] = []
        for j in graph[i]:
            if j in Centers:
                graph2[i].append(j)
        if len(graph2[i]) > 2:
            return []
        if len(graph2[i]) == 1:
            edge.append(i)
    
    e = edge[0]
    q = [e]
    checked = {a:False for a in Centers}
    checked[e] = True
    seq = [e]
    while q:
        qq = []
        for p in q:
            for np in graph2[p]:
                if not checked[np]:
                    checked[np] = True
                    seq.append(np)
                    qq.append(np)
        q = qq

    t = 2
    ans1 = [1]
    for i, p in enumerate(seq):
        w = len(graph[p]) - len(graph2[p])
        if i == 0 or i == len(seq)-1:
            w -= 1
        for s in range(t+1, t+w+1):
            ans1.append(s)
        ans1.append(t)
        t += w+1
    ans1.append(N)
    
    t = 2
    ans2 = [1]
    for i, p in enumerate(seq[::-1]):
        w = len(graph[p]) - len(graph2[p])
        if i == 0 or i == len(seq)-1:
            w -= 1
        for s in range(t+1, t+w+1):
            ans2.append(s)
        ans2.append(t)
        t += w+1
    ans2.append(N)

    for a1, a2 in zip(ans1, ans2):
        if a1 > a2:
            return ans2
        if a1 < a2:
            return ans1

    return ans1

if __name__ == "__main__":
    ans = solve()
    if ans:
        print(*ans)
    else:
        print(-1)