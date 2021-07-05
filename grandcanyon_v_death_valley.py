import csv
import matplotlib.pyplot as plt
from datetime import datetime


def store_data(filename):
    """Retrieves relevant data from CSV file for plotting"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        indexes = {}

        # Create a dictionary for the indexes of each column_header
        for index, column_header in enumerate(header_row):
            indexes[column_header] = index

        # Temporarily store each date, high and low temp in a variable
        # Then permanently store it in its' corresponding list
        for row in reader:
            date = datetime.strptime(row[indexes['DATE']], '%Y-%m-%d')
            try:
                high = int(row[indexes['TMAX']])
                low = int(row[indexes['TMIN']])
            except ValueError:
                print(f"Missing data for: {date} for the following file:"
                      f" \n{filename}")
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)


# Initiate plot
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Plot Grand Canyon NP - 2018
dates, highs, lows = [], [], []
store_data('/Users/larrysaavedra/Desktop/PCC_projects/chapter_16/data/grand_canyon_np_2018_full.csv')

ax.plot(dates, highs, c='red', linewidth=0.9, alpha=0.8)
ax.plot(dates, lows, c='blue', linewidth=0.9, alpha=0.8)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# Plot Death Valley NP - 2018
dates, highs, lows = [], [], []
store_data('/Users/larrysaavedra/Desktop/PCC_projects/chapter_16/data/death_valley_2018_simple.csv')

ax.plot(dates, highs, c='red', linewidth=0.9, alpha=0.4)
ax.plot(dates, lows, c='blue', linewidth=0.9, alpha=0.4)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatting overall plot
ax.set_title("Daily High & Low Temperatures \n"
             "Grand Canyon NP & Death Valley NP - 2018", fontsize=18)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F°)', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)


plt.show()
