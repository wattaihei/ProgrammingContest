import heapq as hp
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    q = []
    s = 0
    ans = []
    for a in A:
        qq = q[:]
        hp.heappush(q, -a)
        s += a
        c = 0
        ss = s
        while ss > M:
            b = - hp.heappop(qq)
            ss -= b
            c += 1
        ans.append(c)

    for a in ans:
        print(a, end=' ')
    print()

if __name__ == "__main__":
    main()