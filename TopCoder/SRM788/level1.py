class NextOlympics():
    def datetoday(self, year, month, day):
        Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d1 = 0
        if year == 2021: d1 += 365
        for m in range(1, month):
            d1 += Days[m-1]
        d1 += day
        return d1

    def countDays(self, today):
        
        year, month, day = map(int, today.split("."))
        d1 = self.datetoday(year, month, day)
        d2 = self.datetoday(2021, 7, 23)
        return d2-d1