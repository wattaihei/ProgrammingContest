N = int(input())

for i in range(50):
    if 2**i > N:
        break
print(2**(i-1))