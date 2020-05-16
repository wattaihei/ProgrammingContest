import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    T = [0]*101
    s = 0

    ans = []
    for a in A:
        s += a
        ss = max(s - M, 0)
        count = 0
        for t in range(100, 0, -1):
            c = T[t]
            if ss - t*c > 0:
                count += c
                ss -= t*c
            else:
                count += ss // t
                if ss % t != 0:
                    count += 1
                break
        T[a] += 1
        ans.append(count)

    for a in ans:
        print(a, end=' ')
    print()

if __name__ == "__main__":
    main()