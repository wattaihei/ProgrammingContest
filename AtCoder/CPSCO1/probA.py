N, A = map(int, input().split())
a = min(N//3, A)
b = A//3
if A%3 > 0: b += 1
print(b, a)
