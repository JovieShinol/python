"https://www.hackerrank.com/challenges/nested-list/problem"


def second_grade():
    n = int(input())
    student_mark = []
    mark_percent = []
    for i in range(n):
        name = input()
        mark = float(input())
        student_mark.append([name,mark])
        mark_percent.append(mark)
    
    mark_percent.sort()
    a = mark_percent[1]
    

    sort_name=[]
    for i in range(n):
        if a == student_mark[i][1]:
            sort_name.append(student_mark[i][0])
    sort_name.sort()
    for i in sort_name:
        print(i)
            


second_grade()