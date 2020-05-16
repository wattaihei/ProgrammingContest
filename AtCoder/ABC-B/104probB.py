S = input()
L = len(S)

A = [chr(i) for i in range(97, 97+26)]
A.append('C')
ans = 'AC'
c = 0
for i in range(L):

    if i == 0:
        if S[i] != 'A':
            ans = 'WA'
            break
        continue
    if  2 <= i <= L-2:
        if S[i] == 'C':
            c += 1
    if not S[i] in A:
        ans = 'WA'
        break

if c != 1:
    ans = 'WA'
print(ans)

