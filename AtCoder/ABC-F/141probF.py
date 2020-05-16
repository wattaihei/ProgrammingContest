N = int(input())
A = list(map(int, input().split()))

def trans2(n):
    A = bin(n)
    return A[2:]

A.sort(reverse=True)

max_l = len(trans2(A[0]))
C = [0 for _ in range(max_l)]
L = [0 for _ in range(max_l+1)]
B = []
for a in A:
    b = trans2(a)
    L[len(b)] += 1
    b = '0'*(max_l - len(b)) + b
    for l in range(max_l):
        if b[max_l-1-l] == '1':
            C[l] += 1
#print(C)
ans = 0
for i, c in enumerate(C):
    if c == 0:
        continue
    elif c%2 == 0:
        ans += 2**(i+1)
    else:
        ans += 2**i
if C[0] == 2:
    ans -= 2
print(ans)