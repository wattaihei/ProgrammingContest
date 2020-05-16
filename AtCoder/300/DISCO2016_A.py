R, C = map(int, input().split())

a = 0
for x in range(1, R+1):
    for y in range(1, R+1):
        if x%C == 0 and y%C == 0 and x**2+y**2 <= R**2:
            a += 1
print(a*4)