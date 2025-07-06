#Zoe Defeo
#Programming Exercise CSV
#This program will create a CSV file named 'grades.csv' and prompt the user to record data for the file.
#The program will then display the created file in tabular format.


import csv

#Function that creates the CSV file
def record():

    #Opens the file to be written.
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        #Header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        #Prompts the user for number of times data entry will need to be looped.
        students = int(input("How many students? "))

        #Prompts the user for each data field and adds it as a row to the file.
        for i in range(students):
            first_name = input(f"Student #{i + 1} first name: ")
            last_name = input(f"Student #{i + 1} last name: ")
            grade_1 = input(f"Student #{i + 1} exam 1 grade: ")
            grade_2 = input(f"Student #{i + 1} exam 2 grade: ")
            grade_3 = input(f"Student #{i + 1} exam 3 grade: ")
            print('\n')
            writer.writerow([first_name, last_name, grade_1, grade_2, grade_3])


    #Calls the function to read the CSV file after it's created
    read()

#Function that displays the created CSV file
def read():

    #Opens the 'grades.csv' file to be read
    with open('grades.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        #Prints each row of entered data in tabular format
        for row in reader:
            print('{:<14}'.format(row[0]) + '{:<14}'.format(row[1]) + '{:<14}'.format(row[2]) + '{:<14}'.format(row[3]) + '{:<14}'.format(row[4]))


record()