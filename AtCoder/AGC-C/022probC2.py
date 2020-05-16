import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def main():

    graph = [[] for _ in range(51)]
    for start in range(51):
        for cost in range(1,51):
            if start%cost == 0:
                graph[0].append((cost, start))
    for end in range(1, 51):
        for cost in range(end+1, 51):
            start = end + cost
            while start <= 50:
                graph[end].append((cost, start))
                start += cost

    use = 0
    for l in reversed(range(1, 52)):
        for a, b in zip(A, B):
            ok = False
            q = [b]
            checked = [False]*51
            checked[b] = True
            while q:
                qq = []
                for p in q:
                    if p == a:
                        ok = True
                        break
                    for cost, np in graph[p]:
                        if not checked[np] and (cost < l or use&(1<<cost)):
                            checked[np] = True
                            qq.append(np)
                if ok: break
                q = qq
            if not ok:
                if l == 51:
                    return -1
                use |= (1<<l)
                break
    return use

if __name__ == "__main__":
    print(main())