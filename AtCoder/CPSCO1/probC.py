import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

Bits = []

def dfs(d, c, bit):
    if d == K:
        Bits.append(bit+"0"*(N-c))
        return
    for n in range(c, N):
        dfs(d+1, n+1, bit+"1")
        bit += "0"

dfs(0, 0, "")

def main():
    ans = 10**14
    for bit in Bits:
        p = 0
        for i, a in enumerate(A):
            if bit[i] == "1":
                p += a
        s = 0
        for a_str in str(p):
            a = int(a_str)
            s += a//5 + a%5
        if s < ans:
            ans = s

    print(ans)

if __name__ == "__main__":
    main()