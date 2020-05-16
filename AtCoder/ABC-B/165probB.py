N = int(input())

K = 100
year = 0
while K < N:
    K = K*101//100
    year += 1
print(year)