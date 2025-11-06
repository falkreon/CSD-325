import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

# Shows a plot of dates vs temps, with the provided title and color.
# Pauses exectuion till the plot window is closed.
def showPlot(title, dates, temps, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Read in dates, highs, and lows from the csv, and returns them as a tuple
def readTemps():
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)

        # Discard the header row
        header_row = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
    return (dates, highs, lows)




dates, highs, lows = readTemps()

print("Welcome to Sitka High/Low.")

while(True):
    print( """
Please enter one of the following:
- Highs to list historic high temps
- Lows to list historic low temps
- Exit to quit the program
""")
    selection = input('> ').lower()
    if (selection == 'highs'):
        showPlot("Daily high temperatures - 2018", dates, highs, 'red')
    elif (selection == 'lows'):
        showPlot("Daily low temperatures - 2018", dates, lows, 'blue')
    elif (selection == 'exit'):
        print("Thank you for using Sitka High/Low!")
        sys.exit()
    else:
        print("Couldn't understand that input. Please type 'highs', 'lows', or 'exit'.")
