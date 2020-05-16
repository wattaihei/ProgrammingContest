from collections import Counter
from operator import itemgetter

N = int(input())
A = list(map(int, input().split()))

B = list(Counter(A).items())
B.sort(key=itemgetter(0))

c = 0
even = False
for k, v in B:
    if v % 2 == 1:
        c += 1
    else:
        if even == True:
            c += 2
            even = False
        else:
            even = True
print(c)