if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = 0
    for i in student_marks:
        if i == query_name:
            for i in student_marks[i]:
                marks = marks+i
    avg = marks/3
    new = "{:.2f}".format(avg)
    print(new)
