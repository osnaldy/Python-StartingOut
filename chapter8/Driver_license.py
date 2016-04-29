def main():
    #Here are the correct answers of the test!
    right_answers = ["B", "D", "A", "A", "C", "A",
               "B", "A", "C", "D", "B", "C",
               "D", "A", "D", "C", "C", "B",
               "D", "A"]
    #The students will enter the answer for each question from 1 - 20 and add it to an array
    students_answers = []
    for i in range(20):
        ans = raw_input("Enter the later letter answer for question #" + str(i+1)+' ')
        students_answers.append(ans)

    new_list = []

    correct = 0
    incorrect = 0
    #here we will compare the answers entered by the students with the correct answers
    #and the whether is correct or incorrect we will append it to a new list
    for i in range(20):
        if right_answers[i] == students_answers[i]:
            new_list.append('Correct')
            correct += 1
        else:
            new_list.append('Incorrect')
            incorrect += 1
    print
    print "Question#\tCorrect Answer\tYour Answer\tStatus"
    print "------------------------------------------------"
    index = 0
    count = 0
    #This is just the printing function to make a nice output
    while index < 20:
        count +=1
        print ' ', count, '\t          ', \
            right_answers[index], \
            '\t       ', students_answers[index], '\t   ', new_list[index]
        index += 1
    grade = (correct/20.0)*100
    print "Your Final Grade is:", grade

    if grade >= 70:
        print "Congrats you passed the test!!!"
    else:
        print "Sorry you failed the test :-("
main()