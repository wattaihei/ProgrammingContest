N, M = map(int, input().split())

even = M//2
odd = (M+1)//2
B = odd*2
K = B+even*2
ans = []
for n in range(1, odd+1):
    print(n, B-n+1)
for n in range(1, even+1):
    print(B+n, K-n+2)