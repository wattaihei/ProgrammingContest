import sys
input = sys.stdin.readline
import heapq as hp
INF = 10**15

N = int(input())
Store = [list(map(int, input().split()))[1:] for _ in range(N)]
M = int(input())
A = list(map(int, input().split()))

q1 = [] # 一番前に入ってる(価値,　棚)
q2 = [] # 2番目

NowOn = [[INF]*2 for k in range(N)] # 棚iで今見せているind
for n in range(N):
    hp.heappush(q1, (-Store[n][0], n, 0))
    hp.heappush(q2, (-Store[n][0], n, 0))
    NowOn[n][0] = 0
    if len(Store[n]) > 1:
        hp.heappush(q2, (-Store[n][1], n, 1))
        NowOn[n][1] = 1

checked = set()
for a in A:
    if a == 1:
        while True:
            costinv, store, order = hp.heappop(q1)
            if not -costinv in checked:
                break
        print(-costinv)
        checked.add(-costinv)
        Second = NowOn[store][1]
        Third = Second + 1
        if len(Store[store]) > Third:
            hp.heappush(q1, (-Store[store][Second], store, Second))
            hp.heappush(q2, (-Store[store][Third], store, Third))
            NowOn[store][0] = Second
            NowOn[store][1] = Third
        elif len(Store[store]) > Second:
            hp.heappush(q1, (-Store[store][Second], store, Second))
            NowOn[store][0] = Second
            NowOn[store][1] = INF
        else:
            NowOn[store][0] = INF
            NowOn[store][1] = INF
    else:
        while True:
            costinv, store, order = hp.heappop(q2)
            if not -costinv in checked:
                break
        print(-costinv)
        checked.add(-costinv)
        if NowOn[store][1] == order: # back
            Third = order + 1
            if len(Store[store]) > Third:
                hp.heappush(q2, (-Store[store][Third], store, Third))
                NowOn[store][1] = Third
            else:
                NowOn[store][1] = INF
        else: # front
            Second = NowOn[store][1]
            Third = Second + 1
            if len(Store[store]) > Third:
                hp.heappush(q1, (-Store[store][Second], store, Second))
                hp.heappush(q2, (-Store[store][Third], store, Third))
                NowOn[store][0] = Second
                NowOn[store][1] = Third
            elif len(Store[store]) > Second:
                hp.heappush(q1, (-Store[store][Second], store, Second))
                NowOn[store][0] = Second
                NowOn[store][1] = INF
            else:
                NowOn[store][0] = INF
                NowOn[store][1] = INF