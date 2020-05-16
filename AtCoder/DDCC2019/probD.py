import sys
input = sys.stdin.readline


def main():
    M = int(input())
    DC = [list(map(int, input().split())) for _ in range(M)]

    ans = 0
    n = 0
    for d, c in DC:
        t = n
        checked = [False]*10
        T = []
        S = []
        for _ in range(10):
            t += d
            r = 1
            if t > 9:
                t -= 9
                r = 2
            if checked[t]:
                S[0] = r
                break
            checked[t] = True
            T.append(t)
            S.append(r)

        loop = c//len(T)
        rem = c%len(T)
        ans += loop*sum(S)
        for r in range(rem):
            ans += S[r]
        n = T[rem-1]
    
    print(ans)

if __name__ == "__main__":
    main()