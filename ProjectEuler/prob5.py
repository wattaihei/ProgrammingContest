from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)

n = 1
for i in range(1, 21):
    n = lcm(n, i)
print(n)