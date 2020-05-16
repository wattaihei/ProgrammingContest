from operator import itemgetter

N = int(input())
job = [list(map(int, input().split())) for i in range(N)]

job = sorted(job, key=itemgetter(0), reverse=True)
job = sorted(job, key=itemgetter(1))

now = 0
des = True
for i, j in enumerate(job):
    j_time = j[0]
    j_dead = j[1]
    now += j_time
    if now > j_dead:
        des = False

if des:
    print('Yes')
else:
    print('No')