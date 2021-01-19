def count_substring(string, sub_string):
    f = 0
    s = len(sub_string)
    for i in range(len(string)):
        if sub_string == string[i:s]:
            f += 1
        s += 1
    return f


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
