import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter the first letter of the city you would like to see data for: Chicago, New York City, or Washington?\n').lower()
        if city in CITY_DATA:
            break
        for key in CITY_DATA:
            if city == key[0]:
                city = key
                break
        if city in CITY_DATA:
            break
        else:
            print('The entry for city is not recognized. Please re-enter the name or first letter of the city of choice.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter 'all' for annual data, or the month of interest.\n").lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', \
                     'october', 'november', 'december'):
            break
        else:
            print("The entry for month is not recognized. Please re-enter the month by 3-letter abbreviation or 'all'.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter 'all' for weekly data, or the day of interest.\n").lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print("The entry for day is not recognized. Please re-enter the day by 3-letter abbreviation or 'all'.\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october'\
                 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Month: {}".format(df['month'].mode().loc[0]))

    # TO DO: display the most common day of week
    print("Day: {}".format(df['day_of_week'].mode().loc[0]))
    
    # TO DO: display the most common start hour
    print("Hour: {}".format(df['Start Time'].dt.hour.mode().loc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Starting Station: {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("Ending Station: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " - " + df['End Station']
    print("Start-End Station Combo: {}".format(df['Trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: {}".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("Average travel time: {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("Earliest birth year: {}".format(df['Birth Year'].min()))
    print("Most recent birth year: {}".format(df['Birth Year'].max()))
    print("Most common birth year: {}".format(df['Birth Year'].mode().loc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' or restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
