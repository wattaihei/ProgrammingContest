X = int(input())

A = [0]
c = 0
while True:
    c += 1
    k = A[-1] + c
    if k >= X:
        break
    A.append(k)

print(c)