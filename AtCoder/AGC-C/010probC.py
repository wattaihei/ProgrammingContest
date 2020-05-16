import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def check():
    stack = [0]
    checked = [False]*N
    need = [[] for _ in range(N)]
    Parent = [-1]*N
    while stack:
        p = stack.pop()
        if p >= 0:
            checked[p] = True
            stack.append(~p)
            for np in graph[p]:
                if not checked[np]:
                    Parent[np] = p
                    stack.append(np)
        else:
            p = ~p
            if len(need[p]) == 0:
                need[Parent[p]].append(A[p])
            elif len(need[p]) == 1:
                if need[p][0] != A[p]:
                    return False
                need[Parent[p]].append(A[p])
            else:
                kmax = sum(need[p])
                kmin = max(max(need[p]), (kmax+1)//2)
                if not kmin <= A[p] <= kmax:
                    return False
                if p == 0 and kmax-2*(kmax-A[p]) != 0:
                    return False
                need[Parent[p]].append(kmax-2*(kmax-A[p]))
    return True

print("YES" if check() else "NO")