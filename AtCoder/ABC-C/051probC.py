sx, sy, tx, ty = map(int, input().split())

gx, gy = tx-sx, ty-sy

r1 = 'U'*gy + 'R'*gx
r2 = 'D'*gy + 'L'*gx
r3 = 'L' + 'U'*(gy+1) + 'R'*(gx+1) + 'D'
r4 = 'R' + 'D'*(gy+1) + 'L'*(gx+1) + 'U'
print(r1 + r2 + r3 + r4)
