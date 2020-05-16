n = input()
ans = []
for i in n:
    if i == '1':
        ans.append('9')
    elif i == '9':
        ans.append('1')
    else:
        ans.append(i)

print(''.join(ans))