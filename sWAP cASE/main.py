def swap_case(s):
    lst = list()
    for i in s:
        if bool(i.isupper()):
            i = i.lower()
        else:
            i = i.upper()
        lst.append(i)
    line = "".join(lst)
    return line


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)