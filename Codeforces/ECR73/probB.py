N = int(input())

l1 = ''.join(['W' if i%2 == 0 else 'B' for i in range(N)])
l2 = ''.join(['B' if i%2 == 0 else 'W' for i in range(N)])

for j in range(N):
    if j%2 == 0:
        print(l1)
    else:
        print(l2)