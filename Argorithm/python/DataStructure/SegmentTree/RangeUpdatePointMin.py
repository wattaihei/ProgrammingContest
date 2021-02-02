class SegmentTree:
    def __init__(self, N, e=(1<<31)):
        self.N = 2**(N-1).bit_length()
        self.e = e
        self.data = [self.e]*(2*self.N-1)
    
    def op(self, a, b):
        return min(a, b)
    
    # O(N)で初期化
    def compose(self, A):
        for k, a in enumerate(A):
            self.data[k+self.N-1] = a
        first = self.N - 1
        while first > 0:
            first = (first-1)//2
            for k in range(first, 2*first+1):
                self.data[k] = self.op(self.data[2*k+1], self.data[2*k+2])

    # point get
    def get(self, k):
        s = self.data[k+self.N-1]
        k += self.N - 1
        while k > 0:
            k = (k-1)//2
            s = self.op(s, self.data[k])
        return s

    # chmin(seg[[l, r)], a)
    def range_update(self, l, r, a):
        if l+1 == r:
            self.data[l+self.N-1] = self.op(self.data[l+self.N-1], a)
            return
        L = l + self.N
        R = r + self.N
        s = self.e
        while L < R:
            if R & 1:
                R -= 1
                self.data[R-1] = self.op(self.data[R-1], a)
            if L & 1:
                self.data[L-1] = self.op(self.data[L-1], a)
                L += 1
            L >>= 1; R >>= 1