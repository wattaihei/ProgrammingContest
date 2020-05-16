a, b = map(int, input().split())

if a == b:
    print(10*a, 10*a+1)
elif a + 1 == b:
    print(10*a+9, 10*b)
elif a == 9 and b == 1:
    print(9, 10)
else:
    print(-1)