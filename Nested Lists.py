if __name__ == '__main__':
    uniqueList = []
    mark = []
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark.append(score)
        student.append([name, score])
    for firstCounter in range(0, len(mark)):
        flag = 0
        for secondCounter in range(0, len(uniqueList)):
            if mark[firstCounter] == uniqueList[secondCounter]:
                flag = 1
        if flag == 0:
            uniqueList.append(mark[firstCounter])

    uniqueList.sort()
    student = sorted(student, key=lambda student: student[0])
    for counter in range(0, len(student)):
        if student[counter][1] == uniqueList[1]:
            print(student[counter][0])