a = 0
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        a += n
print(a)