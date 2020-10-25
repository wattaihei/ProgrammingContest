# 足す時は0~iまで一律に足し、返すのはi番目の値
class imosBIT():
    def __init__(self, N):
        self.N = N
        self.bit = [0 for _ in range(self.N+1)]
    
    def __str__(self):
        ret = []
        for i in range(1, self.N+1):
            ret.append(self.__getitem__(i))
        return "[" + ", ".join([str(a) for a in ret]) + "]"

    def __getitem__(self, i):
        s = 0
        while i <= self.N:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, i, x):
        while i > 0:
            self.bit[i] += x
            i -= i & -i
