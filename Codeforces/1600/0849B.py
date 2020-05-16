import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    x0, y0 = 0, A[0]

    ans = 'No'
    for j in range(1, N):
        x1, y1 = j, A[j]
        dx, dy = x1-x0, y1-y0
        px, py = -1, -1
        ok = False
        for i in range(1, N):
            if i == j:
                continue
            x2, y2 = i, A[i]
            if (x2-x0)*dy != (y2-y0)*dx:
                ok = True
                if px == -1:
                    px, py = x2, y2
                elif (x2-px)*dy != (y2-py)*dx:
                    ok = False
                    break
        if ok:
            ans = 'Yes'

    x3, y3 = 1, A[1]
    x4, y4 = 2, A[2]
    ok = True
    for j in range(2, N):
        if (x4-x3)*(A[j]-y3) != (y4-y3)*(j-x3):
            ok = False
    if (x3-x0)*(y4-y0) != (y3-y0)*(x4-x0) and ok:
        ans = 'Yes'

    print(ans)


if __name__ == "__main__":
    main()