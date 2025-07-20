#Zoe Defeo
#Programming Exercise 12
#This program takes the 'grades.csv' file and turns it into an array to be used for calculating various statistics
#using numpy functions. The mean, median, standard deviation, minimum, and maximum of the data is found and displayed.


import numpy as np
import csv

#Function that takes the exam data and calculates multiple statistics of it.
def calc(exams):

    #Numpy functions are used to find each statistic for the exam data
    mean = np.mean(exams)
    median = np.median(exams)
    deviation = np.std(exams)
    minimum = np.min(exams)
    maximum = np.max(exams)

    #Returns the variables for each found statistic
    return mean, median, deviation, minimum, maximum

#Main function
def main():

    #Opens the grades CSV file to be read
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    #Prints a few rows from the CSV file
    data_array = np.array(data)
    print(data_array[0:6], '\n')

    #Slices the exam 1 scores to be analyzed for each statistic, then prints this information
    exam_1 = (np.array(data_array[1:, 2:3], dtype=int))
    mean_1, median_1, deviation_1, min_1, max_1 = calc(exam_1)
    print(f'The mean for Exam 1 grades is {mean_1}, the median is {median_1}, the standard deviation is '
          f'{deviation_1}, the minimum is {min_1}, the maximum is {max_1}')

    #Slices the exam 2 scores to be analyzed for each statistic, then prints this information
    exam_2 = (np.array(data_array[1:, 3:4], dtype=int))
    mean_2, median_2, deviation_2, min_2, max_2 = calc(exam_2)
    print(f'The mean for Exam 2 grades is {mean_2}, the median is {median_2}, the standard deviation is '
          f'{deviation_2}, the minimum is {min_2}, the maximum is {max_2}')

    #Slices the exam 3 scores to be analyzed for each statistic, then prints this information
    exam_3 = (np.array(data_array[1:, 4:6], dtype=int))
    mean_3, median_3, deviation_3, min_3, max_3 = calc(exam_3)
    print(f'The mean for Exam 3 grades is {mean_3}, the median is {median_3}, the standard deviation is '
          f'{deviation_3}, the minimum is {min_3}, the maximum is {max_3}')

    #Slices every exam score to be analyzed for each statistic, then prints this information
    all_exams = (np.array(data_array[1:, 2:6], dtype=int))
    mean_all, median_all, deviation_all, min_all, max_all = calc(all_exams)
    print(f'The mean for all exam grades is {mean_all}, the median is {median_all}, the standard deviation is '
          f'{deviation_all}, the minimum is {min_all}, the maximum is {max_all}', '\n')

    #Tracks and prints the number of exam scores above 60 for each exam
    print(f'{len(exam_1[exam_1 >= 60])} students passed Exam 1')
    print(f'{len(exam_2[exam_2 >= 60])} students passed Exam 2')
    print(f'{len(exam_3[exam_3 >= 60])} students passed Exam 3')
    print(f'The overall pass percentage across all exams is '
          f'{((len(exam_1[exam_1 >= 60]) + len(exam_2[exam_2 >= 60]) + len(exam_3[exam_3 >= 60])) / len(all_exams[all_exams>=0])) * 100}%')


main()