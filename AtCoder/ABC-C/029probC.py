N = int(input())

A = []
def make(s):
    if len(s) == N:
        A.append(s)
        return
    make(s+'a')
    make(s+'b')
    make(s+'c')
    return

make('')
for a in A:
    print(a)