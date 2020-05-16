N = int(input())

max = 0
for i in range(1,10):
    for j in range(1, 10):
        max += i*j

for i in range(1, 10):
    for j in range(1, 10):
        if i*j+N == max:
            print(i, 'x', j)