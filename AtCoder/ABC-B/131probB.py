N, L = map(int, input().split())

aji = []
aji_abs = []
for i in range(1, N+1):
    aji.append(L+i-1)
    aji_abs.append(abs(L+i-1))
eaten = min(aji_abs)
if eaten*(-1) in aji:
    eaten = - eaten

all = sum(aji) - eaten
print(all)