S = input()
NUM = [str(a) for a in range(10)]
ok = True
for s in S:
    if not s in NUM:
        ok = False
if not ok:
    print("error")
else:
    print(int(S)*2)