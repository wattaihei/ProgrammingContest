T = int(input())
nx = [list(map(int, input().split())) for _ in range(T)]

for n, x in nx:
    print(2*x)