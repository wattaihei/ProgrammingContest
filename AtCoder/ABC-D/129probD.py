import copy
import numpy as np
import time

H, W = map(int, input().split())
state = np.array([list(input()) for _ in range(H)])

t0 = time.time()

def light(row, col, state):
    lighted_count = 0
    col1 = copy.copy(col)
    next = '.'
    while next == '.':
        lighted_count += 1
        col1 += 1
        if col1 >= W:
            break
        next = state[row, col1]
    
    col2 = copy.copy(col)
    next = '.'
    while next == '.':
        lighted_count += 1
        col2 -= 1
        if col2 < 0:
            break
        next = state[row, col2]

    row1 = copy.copy(row)
    next = '.'
    while next == '.':
        lighted_count += 1
        row1 += 1
        if row1 >= H:
            break
        next = state[row1, col]

    row2 = copy.copy(row)
    next = '.'
    while next == '.':
        lighted_count += 1
        row2 -= 1
        if row2 < 0:
            break
        next = state[row2, col]

    lighted_count -= 3
    return lighted_count



def blank_fun(state):
    blank_list = []
    for i, item in np.ndenumerate(state):
        if item == '.':
            blank_list.append(i)
    return blank_list


blank_list = blank_fun(state)

t1 = time.time()
print('make blank', t1 - t0)

blank_count = 0
for blank in blank_list:
    row = blank[0]
    col = blank[1]
    blank_count_now = light(row, col, state)
    if blank_count_now > blank_count:
        blank_count = blank_count_now

t2 = time.time()
print('solve', t2 - t1)

print(blank_count)




