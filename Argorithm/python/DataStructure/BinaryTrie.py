class BinaryTrie():
    def __init__(self, max_value=(1<<32)):
        self.N = max_value.bit_length()
        self.root = self.node()

    class node():
        def __init__(self):
            self.count = 0
            self.left = None
            self.right = None
    
    def __str__(self):
        arr = []
        for i in range(self.__len__()):
            arr.append(self.__getitem__(i))
        return "[" + ", ".join([str(a) for a in arr]) + "]"

    def __len__(self):
        return self.root.count

    def __getitem__(self, k):
        if not 0 <= k < self.__len__():
            raise IndexError("Array Index Out of Range")
        ind = 0
        tmpnode = self.root
        for height in reversed(range(self.N)):
            m = tmpnode.left.count if not tmpnode.left is None else 0
            if k < m:
                tmpnode = tmpnode.left
            else:
                k -= m
                ind |= (1<<height)
                tmpnode = tmpnode.right
        return ind
    
    @property
    def max(self):
        return self.__getitem__(self.__len__()-1)

    @property
    def min(self):
        return self.__getitem__(0)
    
    def add(self, val):
        tmpnode = self.root
        tmpnode.count += 1
        for height in reversed(range(self.N)):
            if (1<<height)&val:
                if tmpnode.right is None:
                    tmpnode.right = self.node()
                tmpnode = tmpnode.right
            else:
                if tmpnode.left is None:
                    tmpnode.left = self.node()
                tmpnode = tmpnode.left
            tmpnode.count += 1

    def delete(self, val):
        tmpnode = self.root
        tmpnode.count -= 1
        for height in reversed(range(self.N)):
            if (1<<height)&val:
                if tmpnode.right.count <= 1:
                    tmpnode.right = None
                    break
                tmpnode = tmpnode.right
            else:
                if tmpnode.left.count <= 1:
                    tmpnode.left = None
                    break
                tmpnode = tmpnode.left
            tmpnode.count -= 1

    def bisect_left(self, val):
        tmpnode = self.root
        ret = 0
        for height in reversed(range(self.N)):
            if tmpnode is None:
                break
            if (1<<height)&val:
                if not tmpnode.left is None:
                    ret += tmpnode.left.count
                tmpnode = tmpnode.right
            else:
                tmpnode = tmpnode.left
        return ret

    def bisect_right(self, val):
        return self.bisect_left(val+1)



# if __name__ == "__main__":
#     import sys
#     input = sys.stdin.buffer.readline

#     M = 2*10**5+1
#     N, Q = map(int, input().split())
#     Rate = []
#     Mem = []
    

#     for _ in range(N):
#         a, b = map(int, input().split())
#         Rate.append(a)
#         Mem.append(b)
        
#     ind_to_co = sorted(list(set(Rate)))
#     co_to_ind = {a:i for i, a in enumerate(ind_to_co)}

#     Grands = [BinaryTrie(len(ind_to_co)) for _ in range(M+1)]
#     for a, b in zip(Rate, Mem):
#         Grands[b].add(co_to_ind[a])
    
    
#     Strong = BinaryTrie(len(ind_to_co))
#     for bt in Grands:
#         if len(bt) > 0:
#             Strong.add(bt.max)

#     Query = [list(map(int, input().split())) for _ in range(Q)]

#     for c, after in Query:
#         c -= 1
#         rate = co_to_ind[Rate[c]]
#         before = Mem[c]
#         if Grands[before].max == rate:
#             Grands[before].delete(rate)
#             Strong.delete(rate)
#             if len(Grands[before]) > 0:
#                 newmax = Grands[before].max
#                 Strong.add(newmax)
#         else:
#             Grands[before].delete(rate)
        
#         if len(Grands[after]) == 0:
#             Grands[after].add(rate)
#             Strong.add(rate)
#         else:
#             premax = Grands[after].max
#             if premax < rate:
#                 Strong.delete(premax)
#                 Strong.add(rate)
#             Grands[after].add(rate)
        
#         print(ind_to_co[Strong.min])
#         Mem[c] = after
