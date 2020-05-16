S = list(input())

a = S.count('0')
b = S.count('1')
m = min(a, b)

print(2 * m)