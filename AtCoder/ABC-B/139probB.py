A, B = map(int, input().split())

for i in range(20):
    if (A-1)*i+1 >= B:
        print(i)
        break