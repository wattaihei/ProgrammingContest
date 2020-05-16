N = int(input())

a = N
b = 0
B = []
if a == 0:
    B = [0]
while a:
    if a % 2 == 0:
        a, b = a//(-2) , 0
    else:
        a, b = a//(-2)+1, 1
    B.append(b)

B = B[::-1]
print(''.join([str(b) for b in B]))