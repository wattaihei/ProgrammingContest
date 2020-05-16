import sys

def inout(n):
    print("?", n)
    sys.stdout.flush()
    S = input()
    return S == "Y"

def main():
    Length = -1
    for l in range(11):
        if not inout(10**l):
            Length = l
            break
    if Length == -1:
        for l in range(11):
            if inout(2*10**l):
                print("!", 10**l)
                return
    tmp = ""
    for _ in range(Length):
        l = 0
        r = 10
        while r - l > 1:
            m = (r+l)//2
            if inout(int(tmp + str(m) + "0"*(Length - len(tmp)))):
                r = m
            else:
                l = m
        if len(tmp) == Length-1:
            if l == 0 and inout(int(tmp + "0"*2)):
                tmp += str(l)
            else:
                tmp += str(l+1)
        elif len(tmp) == 0 and l == 0:
            tmp += str(1)
        else:
            tmp += str(l)
    print("!", tmp)
    return


if __name__ == "__main__":
    main()