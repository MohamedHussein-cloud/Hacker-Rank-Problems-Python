if __name__ == '__main__':
    s = None
    z = None
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    if 2 <= n <= 10:
        arr = sorted(arr)
        arr = list(dict.fromkeys(arr))
        ar = len(arr)
        print(arr[ar-2])
