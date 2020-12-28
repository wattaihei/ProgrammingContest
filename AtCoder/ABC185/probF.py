# 足す時はi番目に足し、返すのは累積和
class sumBIT():
    def __init__(self, N):
        self.N = N
        self.bit = [0 for _ in range(self.N+2)]
    
    def __str__(self):
        ret = []
        for i in range(1, self.N+1):
            ret.append(self.__getitem__(i))
        return "[" + ", ".join([str(a) for a in ret]) + "]"

    def __getitem__(self, i):
        i += 1
        s = 0
        while i > 0:
            s ^= self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.N:
            self.bit[i] ^= x
            i += i & -i


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline

    N, Q = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))

    bit = sumBIT(N)
    for i, a in enumerate(A):
        bit.add(i, a)
    
    for _ in range(Q):
        t, x, y = map(int, input().rstrip().split())
        x -= 1
        if t == 1:
            bit.add(x, y)
        else:
            ans = bit[y-1] ^ bit[x-1]
            print(ans)