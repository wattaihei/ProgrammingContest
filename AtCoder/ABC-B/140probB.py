N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

s = 0
pa = -100
for a in A:
    s += B[a-1]
    if a == pa + 1:
        s += C[pa-1]
    pa = a
print(s)