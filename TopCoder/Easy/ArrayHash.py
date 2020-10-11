class ArrayHash():
    def getHash(self, T):
        ret = 0
        for i, t in enumerate(T):
            for j in range(len(t)):
                ret += i + j + ord(t[j]) - ord("A")
        return ret