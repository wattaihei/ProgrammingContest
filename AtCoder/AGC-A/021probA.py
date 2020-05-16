Nin = input()
l = len(Nin)
fow = int(Nin[0])

all9 = True
for n in Nin[1:]:
    if n != '9':
        all9 = False
if all9:
    ans = fow+(l-1)*9
else:
    ans = fow-1+(l-1)*9
print(ans)