class BankingArray():
    def addCost(self, initialCapacity, numAdds):
        cap = initialCapacity
        cost = 0
        while numAdds > cap:
            cost += cap
            cap *= 2
        cost += numAdds
        return cost