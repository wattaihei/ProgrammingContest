A, B, K = map(int, input().split()) # 横に2個

from fractions import gcd

Gcd = gcd(A, B)

c = 0
for i in range(1, Gcd+1):
	if Gcd % i == 0:
		c += 1
	if c == K:
		print(Gcd//i)
		break