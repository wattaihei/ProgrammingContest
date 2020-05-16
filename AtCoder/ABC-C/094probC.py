N = int(input())
X = list(map(int, input().split()))

Y = sorted(X)
l = Y[N//2-1]
r = Y[N//2]

for x in X:
    if x <= l:
        print(r)
    else:
        print(l)