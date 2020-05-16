for a in range(1, 1001):
    for b in range(1, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a, b, c)
            print(a*b*c)
            break

print(375**2+200**2)
print(425**2)
print(375*200*425)