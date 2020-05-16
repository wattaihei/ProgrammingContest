N = int(input())
K = int(input())

num = 1
for _ in range(N):
    num = min(num*2, num+K)
print(num)