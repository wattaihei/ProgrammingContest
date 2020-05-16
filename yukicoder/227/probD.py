mod = 10**9+7

N = int(input()) - 4

a3 = 1 if N%3 == 0 else 0
a2 = N//2 + 1
if a3 == 1:
    a2 -= 1

al = (N+2)*(N+1)//2
part = (a3 + a2*3)
print(al)

a1 = (al - part) // 6
print((a1+a2+a3)%mod)