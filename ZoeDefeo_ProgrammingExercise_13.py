#Zoe Defeo
#Programming Exercise 13
#This program creates a database and table for the population of 10 Florida cities in 2023. It then simulates
#population growth and decline over 20 years, adding the new data to the table. Lastly, the program prompts the user
#to select an available city to see a visual representation it's simulated growth.


from random import randint
import numpy as np
import matplotlib.pyplot as plt
import sqlite3


def database():

    conn = sqlite3.connect('population_ZD.db')
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS population")

    c.execute("""CREATE TABLE population (
        CITY VARCHAR(255), YEAR INT, POPULATION INT)""")

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

    simulate(c)



def simulate(c):

    year = 2023
    for i in range(20):
        c.execute('SELECT * FROM population WHERE YEAR = ?',(year,))
        rate = randint(-1, 4) / 100

        for row in c.fetchall():
            c.execute('SELECT CITY FROM population')
            name = row[0]
            c.execute('SELECT YEAR FROM population WHERE CITY = ?', (name,))
            year = int(row[1]) + 1
            c.execute('SELECT POPULATION FROM population WHERE CITY = ?', (name,))
            population = (int(row[2]) * rate) + int(row[2])
            insert = [name, year, population]
            c.executemany("INSERT INTO population (CITY, YEAR, POPULATION) VALUES (?,?,?)", (insert,))


    display(c)


def display(c):

    cities = ['Cape Coral', 'Miami', 'Tampa', 'Orlando', 'Venice', 'Bradenton', 'North Port', 'Port Charlotte',
              'Tamiami', 'Punta Gorda']

    print(f"Cities: {cities}")
    while True:
        city = input("Select a city to see it's population growth: ")
        if city.title() in cities:

            c.execute('SELECT YEAR FROM population WHERE CITY = ?', (city.title(),))
            year = c.fetchall()

            c.execute('SELECT POPULATION FROM population WHERE CITY = ?', (city.title(),))
            population = c.fetchall()

            plt.plot(year, population)
            plt.xticks(np.arange(2020, 2050, 5), ('2020', '2025', '2030', '2035', '2040', '2045'))
            plt.title(f'Population Growth of {city.title()}')
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.show()
            break
        else:
            print('Invalid Input')



database()