N, P = map(int, input().split()) # 横に2個
A = [0 if a % 2 == 0 else 1 for a in list(map(int, input().split()))]
odd = A.count(1)
even = A.count(0)

if (P == 1 and odd == 0 ):
    ans = 0
elif odd == 0:
    ans = 2**(len(A))
else:
    ans = 2**(len(A)-1)

print(ans)