import sys
input = sys.stdin.buffer.readline

def inout(x, y):
    print("? {} {}".format(x+1, y+1))
    sys.stdout.flush()
    return int(input())

def main():
    N = int(input())
    larger = 0
    ans = [-1]*N
    for i in range(1, N):
        r1 = inout(larger, i)
        r2 = inout(i, larger)
        if r1 > r2:
            ans[larger] = str(r1)
            larger = i
        else:
            ans[i] = str(r2)
    ans[larger] = str(N)
    
    print("! " + " ".join(ans))

if __name__ == "__main__":
    main()