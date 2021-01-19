s = 0
input()
x = list(map(int, input().strip().split()))
a = set(map(int, input().strip().split()))
b = set(map(int, input().strip().split()))
for i in x:
    if i in a:
        s += 1
    if i in b:
        s -= 1
print(s)
