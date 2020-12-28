import sys
input = sys.stdin.readline

N = int(input())


def main():

    graph = [[] for _ in range(N)]
    for i in range(N):
        S = input().rstrip()
        for j in range(N):
            if S[j] == "1":
                graph[i].append(j)

    state = []
    for i in range(N):
        cango = [False]*N
        cango[i] = True
        q = [i]
        while q:
            qq = []
            for p in q:
                for np in graph[p]:
                    if not cango[np]:
                        cango[np] = True
                        qq.append(np)
            q = qq
        
        state.append(cango)

    ans = 0
    for i in range(N):
        c = 0
        for j in range(N):
            if state[j][i]:
                c += 1
        ans += 1/c
    
    print(ans)

if __name__ == "__main__":
    main()