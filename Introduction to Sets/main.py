def average(array):
    array = set(array)
    array = sum(array) / len(array)
    return array


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
