students_number = int(raw_input("Enter the number of students: "))

scores_per_students = int(raw_input("Enter the amount of scores per students: "))

for students in range(students_number):
    total = 0
    print "Students Number", students + 1
    print '------------------'
    for scores in range(scores_per_students):
        score = int(raw_input(': '))
        total += score
    average = total / scores_per_students
    print "The average for that student is:", average