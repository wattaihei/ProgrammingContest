r, D, x0 = map(int, input().split())
x = [x0]
for i in range(10):
    xi = r * x[-1] - D
    print(xi)
    x.append(xi)