n = int(input())
s = set()
for i in range(n):
    s.add(input().strip())
s = set(dict.fromkeys(s))
print(len(s))
