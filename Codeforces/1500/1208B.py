import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = N
    for l in range(N):
        ok = True
        checked = set()
        for i in range(l):
            if A[i] in checked:
                ok = False
                break
            checked.add(A[i])
        if not ok:
            break
        L = 0
        for r in reversed(range(l, N)):
            if A[r] in checked:
                L = r-l+1
                break
            checked.add(A[r])
        ans = min(ans, L)

    print(ans)

if __name__ == "__main__":
    main()