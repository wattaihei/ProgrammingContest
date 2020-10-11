a, b,c = map(int, input().split())
K = int(input())

count = 0
while a >= b:
    b *= 2
    count += 1
while b >= c:
    c *= 2
    count += 1
print("Yes" if count <= K else "No")