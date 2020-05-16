N = int(input())

a = N//100
b = N%100
if a >= 20 or b <= 5*a:
    print(1)
else:
    print(0)