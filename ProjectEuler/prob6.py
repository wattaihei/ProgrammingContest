S = 0
T = 0
for i in range(1, 101):
    S += i
    T += i**2
print(S**2-T)