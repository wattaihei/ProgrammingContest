a, b = map(int, input().split())
n = b - a
h = 0
for i in range(1, n+1):
    h += i
print(h-b)