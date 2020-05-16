A, B, C, D = map(int, input().split())

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(x, y):
    return (x * y) // gcd(x, y)

A_C = A // C
A_D = A // D
A_CD = A // lcm(C, D)

B_C = B // C
B_D = B // D
B_CD = B // lcm(C, D)

A_e = A - (A_C + A_D - A_CD)
B_e = B - (B_C + B_D - B_CD)

if A % C == 0 or A % D == 0:
    ans = B_e - A_e
else:
    ans = B_e - A_e + 1
print(ans)