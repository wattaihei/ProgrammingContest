import sys
input = sys.stdin.readline
import heapq as hp

def str_to_bit(A):
    bit = 0
    for i, a in enumerate(A):
        if a == "B":
            bit |= (1<<i)
    return bit

def main():
    INF = 10**18

    N, X, Y = map(int, input().split())
    A = list(input().rstrip().split())
    B = list(input().rstrip().split())

    # construct graph
    L = (1<<N)
    graph = [[] for _ in range(L)]
    for bit in range(L):
        # swap
        for i in range(N-1):
            mask = ((1<<N)-1)^(1<<i)^(1<<(i+1))
            l = bit&(1<<i)
            r = bit&(1<<(i+1))
            nbit = (mask&bit) | (l<<1) | (r>>1)
            graph[bit].append((X, nbit))
        # upside down
        for i in range(N):
            nbit = bit ^ (1<<i)
            graph[bit].append((Y, nbit))

    # dijkstra
    Ds = [INF]*L
    sbit = str_to_bit(A)
    ebit = str_to_bit(B)
    q = [(0, sbit)]
    Ds[sbit] = 0
    while q:
        d, p = hp.heappop(q)
        if Ds[p] < d: continue
        for nd, np in graph[p]:
            if Ds[np] > Ds[p] + nd:
                Ds[np] = Ds[p] + nd
                hp.heappush(q, (Ds[np], np))

    print(Ds[ebit])

if __name__ == "__main__":
    main()