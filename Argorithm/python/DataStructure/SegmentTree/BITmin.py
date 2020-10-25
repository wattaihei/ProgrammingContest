INF = 10**18

class BITmin():
    def __init__(self, max):
        self.max = max
        self.data = [INF]*(self.max+1)
    
    # 上に登ってく
    def query_min(self, i):
        s = INF
        while i > 0:
            if s > self.data[i]:
                s = self.data[i]
            i -= i & -i
        return s

    # iまで全ての要素をxで更新
    def update(self, i, x):
        while i <= self.max:
            if x < self.data[i]:
                self.data[i] = x
            i += i & -i