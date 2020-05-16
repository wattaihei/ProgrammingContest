N = int(input())
A = list(map(int, input().split()))

B = [None]*N
for i, a in enumerate(A):
    B[a-1] = i+1

print(' '.join([str(b) for b in B]))