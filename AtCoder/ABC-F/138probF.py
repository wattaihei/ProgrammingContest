L, R = map(int, input().split())

def main():
    la, lb = L, 0
    while la > 1:
        la //= 2
        lb += 1

    ra, rb = R, 0
    while ra > 1:
        ra //= 2
        rb += 1
    print(lb, rb)
    ans = 0
    for b in range(lb, rb):
        ans += 3**b
    
    print(ans)

if __name__ == "__main__":
    main()