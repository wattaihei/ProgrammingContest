import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N)]
for _  in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

checked = [False]*N
L = [-1]*N
R = [-1]*N

# def dfs(p, last_end):
#     checked[p] = True
#     nowright = len(graph[p])+last_end
#     R[p] = nowright
#     nowleft = nowright
#     for np in graph[p]:
#         if not checked[np]:
#             nowright -= 1
#             L[np] = nowright
#             nowleft = dfs(np, nowleft)
#     return nowleft

right = [-1]*N
left = [-1]*N

def dfs2(p):
    stack = [p]
    checked[p] = True
    left[p] = R[p] = right[p] = len(graph[p]) + 2
    L[p] = 1
    while stack:
        p = stack.pop()
        update = False
        for np in graph[p]:
            if not checked[np]:
                stack.append(p)
                stack.append(np)
                right[p] -= 1
                L[np] = right[p]
                left[np] = R[np] = right[np] = len(graph[np]) + left[p]
                checked[np] = True
                update = True
                break
        if not update and stack:
            pp = stack[-1]
            left[pp] = left[p]



def main():
    dfs2(0)
    print("\n".join([str(l) + " " + str(r) for l, r in zip(L,R)]))


if __name__ == "__main__":
    main()