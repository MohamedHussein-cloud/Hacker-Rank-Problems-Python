input()
n = set(map(int, input().strip().split()))
input()
b = set(map(int, input().strip().split()))
x = n.union(b)
print(len(x))
