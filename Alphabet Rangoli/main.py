import string
lst = list(string.ascii_lowercase)


def return_func(_x, a):
    f = a * 4 - 3
    for o in range(_x):
        s = ""
        size = a - 1
        if o != 0:
            for z in range(o):
                s = s + lst[size] + "-"
                size -= 1
            size += 1
            for z in range(1, o):
                size += 1
                if z == (o - 1):
                    s = s + lst[size]
                else:
                    s = s + lst[size] + "-"
        else:
            continue
    if a == 1:
        print("a")
    else:
        print(s.center(f, '-'))


def print_rangoli(_n):
    a = _n
    _n -= 1
    for x in range(2, a + 2):
        return_func(x, a)
    while x > 2:
        x -= 1
        return_func(x, a)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
