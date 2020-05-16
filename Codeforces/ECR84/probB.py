import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    graph = [[]]
    for i in range(N):
        A = list(map(int, input().split()))
        graph.append(A[1:])
    Query.append((N, graph))

for N, graph in Query:
    Man = set([i+1 for i in range(N)])
    Woman = set()
    for woman in range(1, N+1):
        decided = False
        for pair in graph[woman]:
            if pair in Man:
                Man.remove(pair)
                decided = True
                break
        if not decided:
            Woman.add(woman)
    
    if not Man:
        print("OPTIMAL")
    else:
        print("IMPROVE")
        a1 = min(Man)
        a2 = min(Woman)
        print(a2, a1)