from operator import itemgetter

N = int(input())
A = list(map(int, input().split()))

B = []
for i, a in enumerate(A):
    B.append([i+1, a])

B.sort(key=itemgetter(1), reverse=True)

for k, b in B:
    print(k)