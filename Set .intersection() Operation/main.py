input()
n = set(map(int, input().strip().split()))
input()
b = set(map(int, input().strip().split()))
x = n.intersection(b)
print(len(x))
