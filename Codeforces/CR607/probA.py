import sys
input = sys.stdin.readline

N = int(input())
Ss = [input().rstrip() for _ in range(N)]

for S in Ss:
    L = len(S)
    if L >= 5:
        if S[-5:] == "mnida":
            print("KOREAN")
        elif S[-4:] == "desu" or S[-4:] == "masu":
            print("JAPANESE")
        elif S[-2:] == "po":
            print("FILIPINO")
    elif L >= 4:
        if S[-4:] == "desu" or S[-4:] == "masu":
            print("JAPANESE")
        elif S[-2:] == "po":
            print("FILIPINO")    
    elif L >= 2:
        if S[-2:] == "po":
            print("FILIPINO")    