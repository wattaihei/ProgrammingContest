N = int(input())

am = N % 4
if am == 1:
    print(0, 'A')
elif am == 2:
    print(1, 'B')
elif am == 3:
    print(2, 'A')
else:
    print(1, 'A')