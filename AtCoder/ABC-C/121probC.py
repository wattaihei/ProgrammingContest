from operator import itemgetter
import numpy as np

N, M = map(int, input().split()) # 横に2個
stores = [list(map(int, input().split())) for _ in range(N)]

astores = np.array(sorted(stores, key=itemgetter(0)))

stock = 0
price = 0
for i in range(N):
    if stock + astores[i, 1] > M:
        price += astores[i, 0] * (M - stock)
        break
    else:
        price += astores[i, 0] * astores[i, 1]
        stock += astores[i, 1]

print(price)
