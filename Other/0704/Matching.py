import random
import time
import math

N = 9
G = 20
S = 100

Penalty = -4

# make input
def random_generator():
    Ss = [[random.randint(0, 1) for _ in range(N)] for _ in range(S)]
    Gs = [[0]*N for _ in range(G)]
    for i in range(G):
        L = random.sample(range(N), k=3)
        for j, l in enumerate(L):
            Gs[i][l] = j+1
    return Gs, Ss

# read input
def read_from_file():
    Ss = []
    with open("shain.txt", "r") as f:
        for row in f:
            Ss.append(list(map(int, row.rstrip().split())))
    Gs = []
    with open("gakusei.txt", "r") as f:
        for row in f:
            Gs.append(list(map(int, row.rstrip().split())))
    return Gs, Ss


def score_1to1(g, s):
    ret = 0
    for i in range(N):
        ret += g[i]*s[i]
    if ret == 0:
        return Penalty
    return ret

def make_table(Gs, Ss):
    return [[score_1to1(g, s) for i, g in enumerate(Gs)] for j, s in enumerate(Ss)]




Gs, Ss = random_generator()
# Gs, Ss = read_from_file()
Table = make_table(Gs, Ss)

# number of groups
Groups = 10

# group
def score_group(Group):
    ret = 0
    for group in Group:
        for g_ind in group["g"]:
            for s_ind in group["s"]:
                ret += Table[s_ind][g_ind]
    return ret



def make_random_solution():
    Group = []
    Remain_g = set(range(G))
    Remain_s = set(range(S))
    Where_g = [-1]*G
    Where_s = [-1]*S
    for group_ind in range(Groups):
        g_inds = set()
        s_inds = set()
        for _ in range(2):
            g_ind = random.choice(list(Remain_g))
            g_inds.add(g_ind)
            Remain_g.remove(g_ind)
            Where_g[g_ind] = group_ind
        for _ in range(4):
            s_ind = random.choice(list(Remain_s))
            s_inds.add(s_ind)
            Remain_s.remove(s_ind)
            Where_s[s_ind] = group_ind
        Group.append({"s": s_inds, "g": g_inds})
    return Group, Where_g, Where_s



# delta score if swap g_ind1 and g_ind2
def score_increase_swap_g(g_ind1, g_ind2, Group, Where_g):
    group_1 = Where_g[g_ind1]
    group_2 = Where_g[g_ind2]
    if group_1 == group_2:
        return 0
    
    # score before and after swapping
    score_before = 0
    score_after = 0
    for s_ind in Group[group_1]["s"]:
        score_before += Table[s_ind][g_ind1]
        score_after += Table[s_ind][g_ind2]
    for s_ind in Group[group_2]["s"]:
        score_before += Table[s_ind][g_ind2]
        score_after += Table[s_ind][g_ind1]
    
    return score_after - score_before

def swap_g(g_ind1, g_ind2, Group, Where_g):
    group_1 = Where_g[g_ind1]
    group_2 = Where_g[g_ind2]
    Where_g[g_ind1] = group_2
    Where_g[g_ind2] = group_1

    Group[group_1]["g"].remove(g_ind1)
    Group[group_2]["g"].remove(g_ind2)

    Group[group_1]["g"].add(g_ind2)
    Group[group_2]["g"].add(g_ind1)
    return Group, Where_g




# delta score if swap g_ind1 and g_ind2
def score_increase_swap_s(s_ind1, s_ind2, Group, Where_s):
    group_1 = Where_s[s_ind1]
    group_2 = Where_s[s_ind2]
    if group_1 == group_2:
        return 0
    
    # score before and after swapping
    score_before = 0
    score_after = 0
    if group_1 != -1:
        for g_ind in Group[group_1]["g"]:
            score_before += Table[s_ind1][g_ind]
            score_after += Table[s_ind2][g_ind]
    if group_2 != -1:
        for g_ind in Group[group_2]["g"]:
            score_before += Table[s_ind2][g_ind]
            score_after += Table[s_ind1][g_ind]
    
    return score_after - score_before

def swap_s(s_ind1, s_ind2, Group, Where_s):
    group_1 = Where_s[s_ind1]
    group_2 = Where_s[s_ind2]
    if group_1 == group_2:
        return Group, Where_s
    Where_s[s_ind1] = group_2
    Where_s[s_ind2] = group_1

    if group_1 != -1:
        Group[group_1]["s"].remove(s_ind1)
        Group[group_1]["s"].add(s_ind2)
    
    if group_2 != -1:
        Group[group_2]["s"].remove(s_ind2)
        Group[group_2]["s"].add(s_ind1)
    
    return Group, Where_s




def print_result(Score, Group):
    print("Whole Score: {}".format(Score))
    Gakusei = [0]*G
    print("----------------group--------------------")
    for group in Group:
        print(group)
        for g_ind in group["g"]:
            for s_ind in group["s"]:
                Gakusei[g_ind] += Table[s_ind][g_ind]
    print("-------------------score for each gakusei-----------------------")
    for i, g in enumerate(Gakusei):
        print("No.{}: {}".format(i, g))

# simple search
def main():
    Group, Where_g, Where_s = make_random_solution()
    Score = score_group(Group)

    START = time.time()
    LIMIT = 2 #s
    while time.time() - START < LIMIT:
        g_ind1, g_ind2 = random.sample(range(G), 2)
        score_delta = score_increase_swap_g(g_ind1, g_ind2, Group, Where_g)
        if score_delta > 0:
            Group, Where_g = swap_g(g_ind1, g_ind2, Group, Where_g)
            Score += score_delta
        
        s_ind1, s_ind2 = random.sample(range(S), 2)
        score_delta = score_increase_swap_s(s_ind1, s_ind2, Group, Where_s)
        if score_delta > 0:
            Group, Where_s = swap_s(s_ind1, s_ind2, Group, Where_s)
            Score += score_delta
    print(Score)
    
# burning search
def main_burning():
    Group, Where_g, Where_s = make_random_solution()
    Score = score_group(Group)

    START = time.time()
    LIMIT = 10 #s
    TMAX = 1
    TMIN = 0.01
    print("wait for {} sec...".format(LIMIT))
    while time.time() - START < LIMIT:
        t = (time.time() - START) / LIMIT
        Temp = TMAX**(1-t) * TMIN**t
        g_ind1, g_ind2 = random.sample(range(G), 2)
        score_delta = score_increase_swap_g(g_ind1, g_ind2, Group, Where_g)
        if score_delta > 0 or math.exp(score_delta/Temp) > random.random():
            Group, Where_g = swap_g(g_ind1, g_ind2, Group, Where_g)
            Score += score_delta
        
        s_ind1, s_ind2 = random.sample(range(S), 2)
        score_delta = score_increase_swap_s(s_ind1, s_ind2, Group, Where_s)
        if score_delta > 0 or math.exp(score_delta/Temp) > random.random():
            Group, Where_s = swap_s(s_ind1, s_ind2, Group, Where_s)
            Score += score_delta
    print_result(Score, Group)

    


if __name__ == "__main__":
    #main()
    main_burning()