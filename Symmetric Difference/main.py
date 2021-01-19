z = set()
M = int(input())
S = list(map(int, input().strip().split()))[:M]
N = int(input())
S2 = list(map(int, input().strip().split()))[:N]
for x in S:
    if x in S2:
        continue
    else:
        z.add(x)
for x in S2:
    if x in S:
        continue
    else:
        z.add(x)
z = sorted(z)
for i in z:
    print(i)
