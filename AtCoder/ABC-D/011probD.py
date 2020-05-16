import sys
input = sys.stdin.readline

def main():
    N, D = map(int, input().split())
    X, Y = map(int, input().split())
    if X%D != 0 or Y%D != 0:
        return 0
    x = abs(X//D)
    y = abs(Y//D)
    if (N-x-y)%2 != 0:
        return 0
    r = (N-x-y)//2
    ans = 0
    for a in range(r+1):
        b = r-a
        n = 1
        p = 1
        for q in range(1, y+a+1):
            p *= n/q/4
            n += 1
        for q in range(1, a+1):
            p *= n/q/4
            n += 1
        for q in range(1, x+b+1):
            p *= n/q/4
            n += 1
        for q in range(1, b+1):
            p *= n/q/4
            n += 1
        ans += p
    return ans

if __name__ == "__main__":
    print(main())