
day = 1
ans = 0
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for year in range(1901, 2001):
    for month in range(1, 13):
        if day%7 == 1:
            ans += 1
        if month == 2 and year%4 == 0:
            day += 29
        else:
            day += days[month]
    
print(ans)