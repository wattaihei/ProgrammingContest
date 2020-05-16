N, K = map(int, input().split())

c = 0
while True:
    c += 1
    if N//(K**c) == 0:
        break
print(c)