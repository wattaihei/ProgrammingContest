x, y, z = map(int, input().split())
print("Yes" if x*y*z %3 == 0 else "No")