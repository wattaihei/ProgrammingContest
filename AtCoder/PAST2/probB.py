from collections import Counter
from operator import itemgetter

S = list(input())
C = sorted(list(Counter(S).items()), key=itemgetter(1), reverse=True)
print(C[0][0])
