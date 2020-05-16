N = int(input())
City = [int(input()) for _ in range(5)]

people = [N] + [0]*5

t = 0
while people[-1] != N:
    people0 = people[:]
    for i, pep in enumerate(people):
        if i == 5:
            break
        if pep != 0:
            trans = City[i] if pep >= City[i] else pep
            people0[i] -= trans
            people0[i+1] += trans
    people = people0
    t += 1

print(t)

# this argo takes too long time