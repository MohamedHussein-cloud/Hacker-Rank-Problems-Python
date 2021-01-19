if __name__ == '__main__':
    n = int(input())
    s = tuple(map(int, input().split()))[:n]
    print(hash(s))
