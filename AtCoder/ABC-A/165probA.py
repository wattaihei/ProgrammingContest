K = int(input())
A, B = map(int, input().split())
ok = False
for n in range(A, B+1):
    if n % K == 0:
        ok = True
print("OK" if ok else "NG")