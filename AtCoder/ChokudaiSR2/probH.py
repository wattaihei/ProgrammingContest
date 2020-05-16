N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for a, b in AB:
    if a > b:
        print(a-b)
    elif b > a:
        print(b-a)
    else:
        print(-1)