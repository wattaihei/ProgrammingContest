N = int(input())

if N % 2 == 0:
    print(N//2)
    for _ in range(N//2):
        print(2)
else:
    print(N//2+1)
    for _ in range(N//2):
        print(2)
    print(1)