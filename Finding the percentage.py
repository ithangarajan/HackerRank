if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    markList=student_marks[query_name]
    total=0.0
    for counter in range (0,len(markList)):
        total=total+markList[counter]
    print ("%.2f" % (total/len(markList)))