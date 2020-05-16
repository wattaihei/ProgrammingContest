import sys
input = sys.stdin.readline

def main():
    N, C = map(int, input().split())
    XV = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    R = [0]
    x0, v0 = 0, 0
    for i in range(N):
        x, v = XV[i]
        v0 += v-(x-x0)
        x0 = x
        R.append(max(v0, R[-1]))
        ans = max(ans, v0)

    L = [0]
    x0, v0 = C, 0
    for i in reversed(range(N)):
        x, v = XV[i]
        v0 += v-(x0-x)
        x0 = x
        L.append(max(v0, L[-1]))
        ans = max(ans, v0)

    x0, v0 = 0, 0
    for r in range(N):
        x, v = XV[r]
        v0 += v-2*(x-x0)
        x0 = x
        ans = max(ans, v0+L[N-1-r])

    x0, v0 = C, 0
    for l in reversed(range(N)):
        x, v = XV[l]
        v0 += v-2*(x0-x)
        x0 = x
        ans = max(ans, v0+R[l])

    print(ans)


if __name__ == "__main__":
    main()