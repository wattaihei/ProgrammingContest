A = int(input())
B = int(input())

for n in range(A+1):
    if n%B == 0:
        ans = n
print(ans)