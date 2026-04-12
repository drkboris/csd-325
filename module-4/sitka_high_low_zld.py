"""
============================================
 Title: sitka_highs
 Author: Unknown
 Date: 10 April 2026
 Modified By: Zach Donohue
 Description: Reads daily weather data from sitka_weather_2018_simple.csv and plots
    either the high or low temperatures for the year, based on user input.
    The program loops until the user chooses to exit.
 Changes from sitka_highs.py:
    - Added a menu at startup with instructions (Highs, Lows, Exit).
    - Added input loop so the user can view multiple graphs before exiting.
    - Added 'lows' option that plots low temperatures in blue (column index 6).
    - Highs graph retained in red (column index 5).
    - Added exit message and sys.exit() for clean program termination.
    - Moved data-reading and plotting logic into support functions to reduce
      repeated code (Topics from this weeks lessons).
    - Added input validation so unrecognized entries prompt the user again.
===========================================
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt
 
 
# --------------------------------------------------------------------------
# Support functions
# --------------------------------------------------------------------------
 
def read_weather_data(filename, col_index):
    """
    Read dates and a temperature column from the CSV file.
 
    Parameters:
        filename  (str): Path to the CSV file.
        col_index (int): Column index for the temperature values.
 
    Returns:
        tuple: (list of datetime objects, list of int temperatures)
    """
    dates, temps = [], []
 
    with open(filename) as f:
        reader = csv.reader(f)
        # skip header row
        next(reader)
 
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            temps.append(int(row[col_index]))
 
    return dates, temps
 
 
def plot_temperatures(dates, temps, color, title, ylabel):
    """
    Plot a temperature series and display the chart.
 
    Parameters:
        dates  (list): List of datetime objects for the x-axis.
        temps  (list): List of temperature values for the y-axis.
        color  (str):  Line color ('red' for highs, 'blue' for lows).
        title  (str):  Chart title.
        ylabel (str):  Y-axis label.
    """
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
 
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(ylabel, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
 
    plt.show()
 
 
# --------------------------------------------------------------------------
# Main program
# --------------------------------------------------------------------------
 
def main():
    filename = 'sitka_weather_2018_simple.csv'
 
    # Open the program with instructions on how to use the menu; Highs, Lows, or Exit.
    print("\n" + "=" * 45)
    print("  Sitka, AK 2018 Weather Viewer")
    print("=" * 45)
    print("  Menu options:")
    print("    highs  - View daily high temperatures")
    print("    lows   - View daily low temperatures")
    print("    exit   - Quit the program")
    print("=" * 45 + "\n")
 
    # Allow the program to loop until the user selects exit.
    while True:
        choice = input("Enter your choice (highs / lows / exit): ").strip().lower()
 
        # When the user selects 'highs', they should see a graph, in red, that reflects the highs for those dates.
        if choice == 'highs':
            dates, temps = read_weather_data(filename, col_index=5)
            plot_temperatures(
                dates, temps,
                color='red',
                title='Daily High Temperatures - Sitka, AK 2018',
                ylabel='Temperature (F)'
            )
 
        # When the user selects 'lows', they should see a graph, in blue, that reflects the lows for those dates.
        elif choice == 'lows':
            dates, temps = read_weather_data(filename, col_index=6)
            plot_temperatures(
                dates, temps,
                color='blue',
                title='Daily Low Temperatures - Sitka, AK 2018',
                ylabel='Temperature (F)'
            )
 
        # When the user exits, provide an exit message.
        elif choice == 'exit':
            print("\nThanks for using the Sitka Weather Viewer. Goodbye!\n")
            # Use what elements you can from previous programs, perhaps including sys to help the exit proces
            sys.exit(0)
 
        else:
            print(f"  '{choice}' is not a valid option. Please enter highs, lows, or exit.\n")
 
 
if __name__ == '__main__':
    main()
 