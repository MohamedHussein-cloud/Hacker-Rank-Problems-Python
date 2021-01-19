if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        s = len(scores)
        c = sum(scores) 
        f = c/s
        student_marks[name] = f
    query_name = input()
    x = student_marks[query_name]
    z = str(x) + "0"
    h = z.find(".") + 3
    print(z[:h])
