import sys
input = sys.stdin.readline


def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]

    A = [None]*(2*N+1)
    for i, (l, r) in enumerate(LR):
        A[l] = i
        A[r] = i

    graph = [[] for _ in range(N)]

    num_of_edge = 0
    q = []
    for n in range(1, 2*N+1):
        p = A[n]
        if LR[p][0] == n:
            q.append(p)
        else:
            tmp = []
            while True:
                np = q.pop()
                if np == p:
                    break
                else:
                    tmp.append(np)
            while tmp:
                np = tmp.pop()
                q.append(np)
                num_of_edge += 1
                graph[np].append(p)
                graph[p].append(np)
            if num_of_edge > N:
                return False
    if num_of_edge != N-1:
        return False
    q = [0]
    checked = [False]*N
    checked[0] = True
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if not checked[np]:
                    checked[np] = True
                    qq.append(np)
        q = qq
    
    for p in range(N):
        if not checked[p]:
            return False
    return True



if __name__ == "__main__":
    print("YES" if main() else "NO")