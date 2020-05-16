import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    if M%2 == 1:
        print(-1)
        return

    q = [0]
    checked = [False]*N
    checked[0] = True
    search_seq = [0]
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if not checked[np]:
                    checked[np] = True
                    qq.append(np)
                    search_seq.append(np)
        q = qq
    
    evenOrOdd = []
    for n in range(N):
        evenOrOdd.append(len(graph[n])%2)
    
    searched = [False]*N
    ans = []
    for p in reversed(search_seq):
        evens = []
        odds = []
        for np in graph[p]:
            if not searched[np]:
                if evenOrOdd[np]:
                    odds.append(np)
                else:
                    evens.append(np)
        if not odds and not evens:
            break

        if evenOrOdd[p] == 1:
            if odds:
                np = odds.pop()
                ans.append((np, p))
            else:
                np = evens.pop()
                ans.append((np, p))
        for np in odds:
            ans.append((p, np))
            evenOrOdd[np] = 0
        for np in evens:
            ans.append((p, np))
            evenOrOdd[np] = 1
            
        searched[p] = True
    
    for a1, a2 in ans:
        print(a1+1, a2+1)

    return            

        

if __name__ == "__main__":
    main()