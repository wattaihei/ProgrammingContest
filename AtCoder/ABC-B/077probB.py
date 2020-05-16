import math

N = int(input())

for n in range(int(math.sqrt(N))+1):
    a = n**2
    if a > N:
        break
print(a)