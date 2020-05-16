x = list(input())
y = list(input())

x.sort()
y.sort(reverse=True)

s = ''.join(x)
t = ''.join(y)
if s < t:
    print('Yes')
else:
    print('No')
