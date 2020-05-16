a, b = map(int, input().split())
if a < b:
    b, a = a, b
print(str(b)*a)