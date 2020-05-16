B = [list(map(int, input().split())) for _ in range(2)]
C = [list(map(int, input().split())) for _ in range(3)]

def dfs(d, checked):
    if d == 9:
        score = 0
        for i in range(3):
            for j in range(2):
                if checked[i][j] == checked[i][j+1]:
                    score += B[j][i]
                if checked[j][i] == checked[j+1][i]:
                    score += C[i][j]
        return score
    S = []
    for i in range(3):
        for j in range(3):
            if checked[i][j] == 0:
                if d%2 == 0:
                    checked[i][j] = 1
                    s = dfs(d+1, checked) 
                else:
                    checked[i][j] = -1
                    s = dfs(d+1, checked)
                S.append(s)
                checked[i][j] = 0
    if d%2 == 0:
        return max(S)
    else:
        return min(S)
    
checked = [[0 for _ in range(3)] for _ in range(3)]
s1 = dfs(0, checked)

T = 0
for i in range(3):
    for j in range(2):
        T += B[j][i]
        T += C[i][j]
print(s1)
print(T-s1)