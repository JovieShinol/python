if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks:
        if i == query_name:
            average = 0.0
            for j in student_marks[i]:
                
                average += j
            
            print('{:.2f}'.format(float(average/len(student_marks[i]))))
       