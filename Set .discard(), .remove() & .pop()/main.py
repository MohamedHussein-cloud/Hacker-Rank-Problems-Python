o = int(input())
s = set(map(int, input().strip().split()))
n = int(input())
for i in range(n):
    x = list(input().strip().split())
    if x[0] == "remove":
        try:
            s.remove(int(x[1]))
        except:
            continue
    elif x[0] == "discard":
        s.discard(int(x[1]))
    else:
        s.pop()
print(sum(s))
