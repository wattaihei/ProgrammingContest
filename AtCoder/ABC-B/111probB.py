N = input()

top = N[0]
little = True
for n in N:
    if int(n) > int(top):
        little = False
        break

if little:
    print(top*len(N))
else:
    print(str(int(top)+1)*len(N))
