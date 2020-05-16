N = int(input())
d = list(map(int, input().split()))

d = sorted(d)

m = d[N // 2 - 1]
l = d[N // 2]

print(l-m)