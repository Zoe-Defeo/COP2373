#Zoe Defeo
#Programming Exercise 13
#This program creates a database and table for the population of 10 Florida cities in 2023. It then simulates
#population growth and decline over 20 years, adding the new data to the table. Lastly, the program prompts the user
#to select an available city to see a visual representation it's simulated growth.


from random import randint
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

#Function that creates the population database and table
def database():

    #Connect to database
    conn = sqlite3.connect('population_ZD.db')
    c = conn.cursor()

    #Drops table if it already exists
    c.execute("DROP TABLE IF EXISTS population")

    #Creates population table
    c.execute("""CREATE TABLE population (
        CITY VARCHAR(255), YEAR INT, POPULATION INT)""")

    #Inserting initial data for 10 Florida cities into table
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Cape Coral', 2023, 224455)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Miami', 2023, 455924)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Tampa', 2023, 403364)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Orlando', 2023, 320742)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Venice', 2023, 28150)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Bradenton', 2023, 57076)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('North Port', 2023, 88934)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Port Charlotte', 2023, 57602)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Tamiami', 2023, 52649)")
    c.execute("INSERT INTO population (CITY, YEAR, POPULATION) VALUES ('Punta Gorda', 2023, 20227)")

    # Commit changes
    conn.commit()

    #Run population growth simulation using created table
    simulate(c)


#Function that simulates population growth and decline, adds new data to table
def simulate(c):

    year = 2023

    #Repeats simulation process for 20 years
    for i in range(20):
        c.execute('SELECT * FROM population WHERE YEAR = ?',(year,))

        #Determines growth rate for the simulated year
        rate = randint(-1, 4) / 100

        #Retrieves data from each row
        for row in c.fetchall():

            #Determines which city will be used for calculations
            c.execute('SELECT CITY FROM population')
            name = row[0]

            #Determines what year is being simulated, increments with each loop
            c.execute('SELECT YEAR FROM population WHERE CITY = ?', (name,))
            year = int(row[1]) + 1

            #Calculates new population with predetermined growth rate
            c.execute('SELECT POPULATION FROM population WHERE CITY = ?', (name,))
            population = (int(row[2]) * rate) + int(row[2])

            #Creates a new row of data after calculations
            insert = [name, year, population]
            c.executemany("INSERT INTO population (CITY, YEAR, POPULATION) VALUES (?,?,?)", (insert,))

    #Runs function to display graph with newly added data
    display(c)


#Function that creates and displays a graph of a selected city's population growth
def display(c):

    #List of cities to choose from
    cities = ['Cape Coral', 'Miami', 'Tampa', 'Orlando', 'Venice', 'Bradenton', 'North Port', 'Port Charlotte',
              'Tamiami', 'Punta Gorda']

    #Displays what cities can be chosen
    print(f"Cities: {cities}")

    #If selected city is valid, begins graphing process
    while True:

        #Prompts user to select a city
        city = input("Select a city to see it's population growth: ")

        #Checks to see if city is in data
        if city.title() in cities:

            #Takes each year from selected city for plotting
            c.execute('SELECT YEAR FROM population WHERE CITY = ?', (city.title(),))
            year = c.fetchall()

            #Takes populations from selected city for plotting
            c.execute('SELECT POPULATION FROM population WHERE CITY = ?', (city.title(),))
            population = c.fetchall()

            #Plots the selected cities population at each year
            plt.plot(year, population)

            #Adjust visuals of graph
            plt.xticks(np.arange(2020, 2050, 5), ('2020', '2025', '2030', '2035', '2040', '2045'))
            plt.title(f'Population Growth of {city.title()}')
            plt.xlabel('Year')
            plt.ylabel('Population')

            #Displays the final graph of selected city
            plt.show()
            break

        #Loop repeats if city input is invalid
        else:
            print('Invalid Input')



database()