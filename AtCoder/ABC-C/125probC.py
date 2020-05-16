N = int(input())
A = list(map(int, input().split()))


def Gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def gcd_list(num_list):
    for i, num in enumerate(num_list):
        if i == 0:
            g = num
        else:
            g = Gcd(num, g)
    return g

GCD = 0
for i in range(N):
    others = A[:]
    others.pop(i)
    gcd = gcd_list(others)
    if gcd > GCD:
        GCD = gcd
print(GCD)