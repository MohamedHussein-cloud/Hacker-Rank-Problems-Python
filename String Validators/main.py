if __name__ == '__main__':
    x = 0
    f = 2
    lst1 = list()
    lst2 = list()
    lst3 = list()
    lst4 = list()
    lst5 = list()
    s = input()
    for i in s:
        lst1.append(i.isalnum())
        lst2.append(i.isalpha())
        lst3.append(i.isdigit())
        lst4.append(i.islower())
        lst5.append(i.isupper())
        x += 1
        f += 1
    if True in lst1:
        print("True")
    else:
        print("False")
    if True in lst2:
        print("True")
    else:
        print("False")
    if True in lst3:
        print("True")
    else:
        print("False")
    if True in lst4:
        print("True")
    else:
        print("False")
    if True in lst5:
        print("True")
    else:
        print("False")
