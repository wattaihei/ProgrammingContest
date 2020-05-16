import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


checked = [False]*N
checked[0] = True

def dfs(stack):
    while True:
        p = stack[-1]
        update = False
        for np in graph[p]:
            if not checked[np]:
                update = True
                stack.append(np)
                checked[np] = True
                break
        if not update:
            break
    return stack

stack1 = dfs([0])
stack2 = dfs([0])
ans = stack1[::-1] + stack2[1:]

print(len(ans))
print(" ".join([str(a+1) for a in ans]))