N = int(input())
A = list(map(int, input().split()))

odd = False
even = False
for a in A:
    if a%2==0:
        even = True
    else:
        odd = True

if odd and even:
    A.sort()
for a in A:
    print(a, end=' ')
print()