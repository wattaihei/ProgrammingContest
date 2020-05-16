N = int(input())
H = list(map(int, input().split())) 

c = 0
for i in range(N):
    if i == 0:
        c += 1
        continue
    if max(H[:i+1]) == H[i]:
        c += 1
print(c)
