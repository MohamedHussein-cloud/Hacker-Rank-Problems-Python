if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 150:
        x = range(n)
        for s in x:
            if s != 0:
                print(s, end="")
    print(n)
