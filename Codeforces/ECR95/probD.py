from bisect import bisect_right, bisect_left
# instead of AVLTree
class BITbisect():
    def __init__(self, InputProbNumbers):
        # 座圧
        self.ind_to_co = [-10**18]
        self.co_to_ind = {}
        for ind, num in enumerate(sorted(list(set(InputProbNumbers)))):
            self.ind_to_co.append(num)
            self.co_to_ind[num] = ind+1
        self.max = len(self.co_to_ind)
        self.data = [0]*(self.max+1)
    
    def __str__(self):
        retList = []
        for i in range(1, self.max+1):
            x = self.ind_to_co[i]
            if self.count(x):
                c = self.count(x)
                for _ in range(c):
                    retList.append(x)
        return "[" + ", ".join([str(a) for a in retList]) + "]"
    
    def __getitem__(self, key):
        key += 1
        s = 0
        ind = 0
        l = self.max.bit_length()
        for i in reversed(range(l)):
            if ind + (1<<i) <= self.max:
                if s + self.data[ind+(1<<i)] < key:
                    s += self.data[ind+(1<<i)]
                    ind += (1<<i)
        if ind == self.max or key < 0:
            raise IndexError("BIT index out of range")
        return self.ind_to_co[ind+1]
    
    def __len__(self):
        return self._query_sum(self.max)
    
    def __contains__(self, num):
        if not num in self.co_to_ind:
            return False
        return self.count(num) > 0
    
    # 0からiまでの区間和
    # 左に進んでいく
    def _query_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    # i番目の要素にxを足す
    # 上に登っていく
    def _add(self, i, x):
        while i <= self.max:
            self.data[i] += x
            i += i & -i
    
    # 値xを挿入
    def push(self, x):
        if not x in self.co_to_ind:
            raise KeyError("The pushing number didnt initialized")
        self._add(self.co_to_ind[x], 1)
            
    # 値xを削除
    def delete(self, x):
        if not x in self.co_to_ind:
            raise KeyError("The deleting number didnt initialized")
        if self.count(x) <= 0:
            raise ValueError("The deleting number doesnt exist")
        self._add(self.co_to_ind[x], -1)

    # 要素xの個数
    def count(self, x):
        return self._query_sum(self.co_to_ind[x]) - self._query_sum(self.co_to_ind[x]-1)
    
    # 値xを超える最低ind
    def bisect_right(self, x):
        if x in self.co_to_ind:
            i = self.co_to_ind[x]
        else:
            i = bisect_right(self.ind_to_co, x) - 1
        return self._query_sum(i)

    # 値xを下回る最低ind
    def bisect_left(self, x):
        if x in self.co_to_ind:
            i = self.co_to_ind[x]
        else:
            i = bisect_left(self.ind_to_co, x)
        if i == 1:
            return 0
        return self._query_sum(i-1)


def main():
    import sys
    input = sys.stdin.buffer.readline
    import heapq as hp

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    InputNum = A[:]
    Query = []
    for _ in range(Q):
        a, b = map(int, input().split())
        InputNum.append(b)
        Query.append((a, b))

    q = []
    for i in range(N-1):
        hp.heappush(q, (-A[i+1]+A[i], A[i], A[i+1]))
    
    bit = BITbisect(InputNum)
    for a in A:
        bit.push(a)
    if q:
        print(A[-1]-A[0]+q[0][0])
    else:
        print(0)
    l = N
    for a, b in Query:
        ind = bit.bisect_left(b)
        
        m2 = bit[ind-1] if 0 <= ind-1 < l else -1
        if a == 1:
            m1 = bit[ind] if 0 <= ind < l else -1
            if m1 != -1:
                hp.heappush(q, (-m1+b, b, m1))
            if m2 != -1:
                hp.heappush(q, (-b+m2, m2, b))
            bit.push(b)
            l += 1
        else:
            m0 = bit[ind+1] if 0 <= ind+1 < l else -1
            if m0 != -1 and m2 != -1:
                hp.heappush(q, (-m0+m2, m2, m0))
            bit.delete(b)
            l -= 1
        
        while q:
            d, s, t = q[0]
            if not s in bit or not t in bit or bit.bisect_left(t) - bit.bisect_left(s) != 1:
                hp.heappop(q)
            else:
                break
        if l <= 2:
            ans = 0
        else:
            ans = bit[l-1] - bit[0] + d
        print(ans)




if __name__ == "__main__":
    main()