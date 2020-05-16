def main():
    N = int(input())
    n = 0
    for h in range(1, 3501):
        for w in range(1, 3501):
            a = 4*h*w-N*h-N*w
            if a <= 0:
                continue
            b = N*w*h
            if b%a == 0:
                n = b//a
                break
        if n > 0:
            break
    print(h, w, n)

if __name__ == "__main__":
    main()