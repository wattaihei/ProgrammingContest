N = int(input())

update = False
for X in range(N+1):
    if X*108//100 == N:
        update = True
        print(X)
        break
if not update:
    print(':(')