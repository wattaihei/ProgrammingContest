x, y, z = map(int, input().split())
if x > y+z:
    print("+")
elif y > x+z:
    print("-")
elif z == 0 and x == y:
    print("0")
else:
    print("?")