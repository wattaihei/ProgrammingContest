N = int(input())
A = list(map(int, input().split()))

c = 0
up = '?'
pre = A[0]
for a in A:
    if a > pre:
        if up is False:
            c += 1
            up = '?'
        else:
            up = True
    elif a < pre:
        if up is True:
            c += 1
            up = '?'
        else:
            up = False
    pre = a

c += 1

print(c)