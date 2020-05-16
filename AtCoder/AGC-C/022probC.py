import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def main():
    border = 12

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

    mustconsider = [True]*N
    basebit = 0
    for i, (a, b) in enumerate(zip(A, B)):
        if b >= border:
            mustconsider[i] = False
            if a >= 2*b+1:
                basebit |= 1<<(a-b)
            elif a != b:
                return -1
    
    # 立ってるbitのcostを使う
    ans = 10**60
    for bit in range(1<<(border-1)):
        bit <<= 1
        ok = True
        using = [0 for _ in range(N)]
        lowest = []
        for i, (a, b) in enumerate(zip(A, B)):
            if mustconsider[i]:
                canreach = False
                q = [b]
                checked = [False]*51
                checked[b] = True
                while q:
                    qq = []
                    for p in q:
                        if p == a:
                            canreach = True
                            break
                        if 2*p+1 <= a:
                            n = 1
                            while (a-p)//n > p:
                                if (a-p)%n == 0:
                                    using[i] |= 1<<((a-p)//n)
                                n += 1
                        for cost, np in graph[p]:
                            if (1<<cost)&bit and not checked[np]:
                                checked[np] = True
                                qq.append(np)
                    if canreach: break
                    q = qq
                if not canreach:
                    if using[i] == 0:
                        ok = False
                        break
                    l = using[i] & -using[i]
                    lowest.append((l, i))
        if ok:
            now = bit|basebit
            lowest.sort(reverse=True)
            for l, i in lowest:
                if using[i]&now: continue
                now |= l
            ans = min(ans, now)

    if ans == 10**60:
        return -1
    return ans



if __name__ == "__main__":
    print(main())