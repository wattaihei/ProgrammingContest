C = [list(map(int, input().split())) for _ in range(3)]

ans = 'Yes'
for i in range(1, 3):
    if C[0][i] - C[1][i] != C[0][0] - C[1][0]:
        ans = 'No'
        break
    if C[0][i] - C[2][i] != C[0][0] - C[2][0]:
        ans = 'No'
        break
    if C[i][0] - C[i][1] != C[0][0] - C[0][1]:
        ans = 'No'
        break
    if C[i][0] - C[i][2] != C[0][0] - C[0][2]:
        ans = 'No'
        break
print(ans)