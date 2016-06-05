import random

state_capitals={"Washington":"Olympia","Oregon":"Salem",
                    "California":"Sacramento","Ohio":"Columbus",
                    "Nebraska":"Lincoln","Colorado":"Denver",
                    "Michigan":"Lansing","Massachusetts":"Boston",
                    "Florida":"Tallahassee","Texas":"Austin",
                    "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",
                    "Alaska":"Juneau","Utah":"Salt Lake City",
                    "New Mexico":"Santa Fe","North Dakota":"Bismarck",
                    "South Dakota":"Pierre","West Virginia":"Charleston",
                    "Virginia":"Richmond","New Jersey":"Trenton",
                    "Minnesota":"Saint Paul","Illinois":"Springfield",
                    "Indiana":"Indianapolis","Kentucky":"Frankfort",
                    "Tennessee":"Nashville","Georgia":"Atlanta",
                    "Alabama":"Montgomery","Mississippi":"Jackson",
                    "North Carolina":"Raleigh","South Carolina":"Columbia",
                    "Maine":"Augusta","Vermont":"Montpelier",
                    "New Hampshire":"Concord","Connecticut":"Hartford",
                    "Rhode Island":"Providence","Wyoming":"Cheyenne",
                    "Montana":"Helena","Kansas":"Topeka",
                    "Iowa":"Des Moines","Pennsylvania":"Harrisburg",
                    "Maryland":"Annapolis","Missouri":"Jefferson City",
                    "Arizona":"Phoenix","Nevada":"Carson City",
                    "New York":"Albany","Wisconsin":"Madison",
                    "Delaware":"Dover","Idaho":"Boise",
                    "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}
correct = []
incorrect = []
again = 'y'
c_count = 0
i_count = 0
while again.lower() == 'y':
    choice = random.choice(state_capitals.keys())
    capital = raw_input("Enter the capital of " + choice + ": ")
    if capital == state_capitals.get(choice):
        c_count += 1
        correct.append(capital)
    else:
        i_count += 1
        incorrect.append(capital)
    again = raw_input("To keep playing enter 'y' or 'n' to quit : ")

print "Number of correct answers", c_count
print correct
print "Number of incorrect answers", i_count
print incorrect