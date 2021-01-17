K = int(input())

N = 50

b = N-1 + K//N
c = K%N

ans = []
for _ in range(c):
    ans.append(b+N-c+1)

for _ in range(N-c):
    ans.append(b-c)

print(N)
print(*ans)