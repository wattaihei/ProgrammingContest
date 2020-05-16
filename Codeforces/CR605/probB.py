import sys
input = sys.stdin.readline

Q = int(input())
Ss = [list(input().rstrip()) for _ in range(Q)]

for S in Ss:
    dic = {"L": 0, "R": 0, "U": 0, "D": 0}
    for s in S:
        dic[s] += 1
    
    LR = min(dic["L"], dic["R"])
    UD = min(dic["U"], dic["D"])
    if LR == 0:
        print(min(UD, 1)*2)
        print("UD"*min(UD, 1))
    elif UD == 0:
        print(min(LR, 1)*2)
        print("LR"*min(LR, 1))
    else:
        print((LR+UD)*2)
        print("L"*LR + "U"*UD + "R"*LR + "D"*UD)