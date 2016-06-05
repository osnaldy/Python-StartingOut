def main():

    course = {'CS101':['3004', 'Haynes', '8:30 a.m.'],
          'CS102':['4501', 'Alvarado', '9:00 a.m.'],
          'CS103':['6755', 'Rich', '10:00 a.m.'],
          'NT110':['1244', 'Burke', '11:00 a.m.'],
          'CM241':['1411', 'Lee', '1:00pm']}

    string = raw_input("Enter the key to retrieve its values: ")

    value  = course.get(string, 'Not Found!')
    print 'Room Number:', value[0]
    print '''Instructor's Names:''', value[1]
    print 'Meeting Time:', value[2]

main()
