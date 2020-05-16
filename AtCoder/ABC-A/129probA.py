a, b, c = map(int, input().split())

a1 = a+b
a2 = a+c
a3 = b+c
x = [a1, a2, a3]
print(min(x))