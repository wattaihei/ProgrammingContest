# P[i] : iから移動する先の頂点
# 巨大なK進んだのちの頂点をO(N)で求める
class FastTripWithCycle():
    def __init__(self, N, P):
        self.N = N
        self.P = P
        self.belongGroup = [-1]*self.N # 帰着するサイクルグループ
        self.cycleStartInd = [-1]*self.N #最初にサイクルに到達したときのリストind
        self.Cycles = []
        self.compose()
    
    def compose(self):
        seq = [-1]*self.N
        for s in range(self.N):
            t = s
            T = []
            while seq[t] == -1:
                seq[t] = len(T)
                T.append(t)
                t = self.P[t]
            if self.belongGroup[t] == -1: 
                # 新規サイクル
                g = len(self.Cycles)
                for i, c in enumerate(T):
                    self.cycleStartInd[c] = i-seq[t] if i >= seq[t] else 0
                    self.belongGroup[c] = g
                self.Cycles.append(T[seq[t]:])
            else:
                for i in T:
                    self.belongGroup[i] = self.belongGroup[t]
                    self.cycleStartInd[i] = self.cycleStartInd[t]
    
    # startからn進んだあとの頂点
    def query(self, start, n):
        g = self.belongGroup[start]
        v = start
        u = self.Cycles[g][self.cycleStartInd[start]]
        while n > 0 and v != u:
            n -= 1
            v = self.P[v]
        if n == 0: return v

        for _ in range(n%len(self.Cycles[g])):
            v = self.P[v]
        return v
    
    # 各頂点のスコアが決まってるとき、合計の算出(最初を除く)
    def queryScoreSum(self, start, n, Score):
        g = self.belongGroup[start]
        v = start
        u = self.Cycles[g][self.cycleStartInd[start]]
        s = 0
        while n > 0 and v != u:
            n -= 1
            v = self.P[v]
            s += Score[v]
        if n == 0: return s

        wholeCycleScore = 0
        for p in self.Cycles[g]:
            wholeCycleScore += Score[p]

        s += (n//(len(self.Cycles[g])))*wholeCycleScore
        for _ in range(n%len(self.Cycles[g])):
            v = self.P[v]
            s += Score[v]
        return s