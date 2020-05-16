from copy import deepcopy

B = [list(map(int, input().split())) for _ in range(2)]
C = [list(map(int, input().split())) for _ in range(3)]

bat = [[0 for _ in range(3)] for _ in range(3)]
point = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
def game(bat, point, turn):
    print(turn, len(point))
    if turn == 9:
        score = 0
        for i in range(2):
            for j in range(3):
                if bat[i][j] == bat[i+1][j]:
                    score += B[i][j]
                if bat[j][i] == bat[j][i+1]:
                    score += C[j][i]
        return score
    
    k = len(point)
    sc = []
    for i in range(k):
        newp = point[:]
        bat1 = deepcopy(bat)
        bat2 = deepcopy(bat)
        x, y = newp.pop(i)
        bat1[x][y] = 0
        bat2[x][y] = 1
        s1 = game(bat1, newp, turn+1)
        s2 = game(bat2, newp, turn+1)
        sc.append(s1)
        sc.append(s2)
    if turn % 2 == 1:
        return min(sc)
    else:
        return max(sc)
print(game(bat, point, 0))