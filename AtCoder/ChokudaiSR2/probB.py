N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for a, b in AB:
    print(a%b)