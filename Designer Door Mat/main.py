x = 1
n, m = map(int, input().strip().split())
for i in range(int(n / 2)):
    print((".|." * x).center(m, '-'))
    x += 2
print("WELCOME".center(m, '-'))
for i in range(int(n / 2)):
    x -= 2
    print((".|." * x).center(m, '-'))
