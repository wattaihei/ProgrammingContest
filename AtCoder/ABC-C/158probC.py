A, B = map(int, input().split())

m = -1
for n in range(100001):
    if A*100 <= 8*n < (A+1)*100 and B*100 <= 10*n < (B+1)*100:
        m = n
        break
print(m)