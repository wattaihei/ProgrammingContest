N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

for a in A:
    b = sum(a)
    print(b//2)