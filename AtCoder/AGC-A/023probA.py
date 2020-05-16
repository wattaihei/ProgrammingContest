import collections

N = int(input())
A = list(map(int, input().split()))

sum = 0
sumA = []
for a in A:
    sum += a
    sumA.append(sum)

colA = collections.Counter(sumA)

ans = 0
for key, val in colA.items():
    if key == 0:
        ans += val*(val+1)//2
    else:
        ans += (val-1)*val//2

print(ans)
