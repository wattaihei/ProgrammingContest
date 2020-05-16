import sys
input = sys.stdin.readline
import heapq as hp


def main():
    N, M, K = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    Tmp = [i for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Tmp[b-1] = max(Tmp[b-1], a-1)

    Val = [[] for _ in range(N)]
    for i, (_, _, c) in enumerate(ABC):
        Val[Tmp[i]].append(c)

    q = []
    S = K
    for i, (a, b, _) in enumerate(ABC):
        vacant = S-a
        if vacant < 0:
            return -1
        while len(q) > vacant:
            hp.heappop(q)
        S += b
        for p in Val[i]:
            hp.heappush(q, p)
    while len(q) > S:
        hp.heappop(q)
    return sum(q)

if __name__ == "__main__":
    print(main())