import sys
input = sys.stdin.buffer.readline

def main():
    mod = 10**9+7

    H, W = map(int, input().split())
    state = [list(input().rstrip()) for _ in range(H)]

    Nums = [[1]*W for _ in range(H)]
    Ps = [1]
    for h in range(H):
        s = 0
        for w in range(W):
            Nums[h][w] += s
            if state[h][w] == ord("#"):
                s = 0
            else:
                Ps.append(Ps[-1]*2 % mod)
                s += 1

    for h in range(H):
        s = 0
        for w in reversed(range(W)):
            Nums[h][w] += s
            if state[h][w] == ord("#"):
                s = 0
            else:
                s += 1

    for w in range(W):
        s = 0
        for h in range(H):
            Nums[h][w] += s
            if state[h][w] == ord("#"):
                s = 0
            else:
                s += 1

    for w in range(W):
        s = 0
        for h in reversed(range(H)):
            Nums[h][w] += s
            if state[h][w] == ord("#"):
                s = 0
            else:
                s += 1

    r = len(Ps)-1
    ans = 0
    for h in range(H):
        for w in range(W):
            if state[h][w] == ord("."):
                c = Nums[h][w]
                ans = (ans + Ps[r] - Ps[r-c]) % mod
    print(ans) 

if __name__ == "__main__":
    main()