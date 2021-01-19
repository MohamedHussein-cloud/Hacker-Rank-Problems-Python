if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    s = x + 1
    f = y + 1
    w = z + 1
    print("[", end="")
    for i in range(s):
        for j in range(f):
            for k in range(w):
                if (i + j + k) != n:
                    print("[", i, ", ", j, ", ", k, "]", sep='', end="")
                    if i != x or j != y or k != z:
                        print(", ", end="")
    print("]", end="")
