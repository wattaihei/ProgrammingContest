from collections import Counter

N = int(input())
A = list(map(str, input().split()))

B = Counter(A)
a = len(B)
if a == 4:
    print('Four')
else:
    print('Three')