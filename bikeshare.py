import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def Display_Common(df, name):
    """Returns the most common value in a specified column of a DataFrame."""
    return df[name].mode()[0]

def validation(text, valid_list):
    """Prompts the user for input and validates it against a list of valid options."""
    while True:
        valid = input(text).lower()
        if valid in valid_list:
            return valid
        else:
            print("It seems your input is invalid, please try again.")

def display_rows(df):
    """To show rows"""
    n = 0
    while True:
        x = input("Do you want to view individual trip data? Type yes or no: ")
        if x.lower() == 'yes':
            n += 5
            print(df.head(n))
        else:
            break

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    valid_cities = ["chicago", "new york", "washington"]
    city = validation("Would you like to see data for Chicago, New York, or Washington? ", valid_cities)

    valid_months = ["all", "january", "february", "march", "april", "may", "june"]
    month = validation("Which month - January, February, March, April, May, or June? ", valid_months)

    valid_days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = validation("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ", valid_days)

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    Common_Month = Display_Common(df, 'Month')
    print(f'Most common month is: {Common_Month}')

    Common_Day = Display_Common(df, 'Day')
    print(f'Most common day is: {Common_Day}')

    df['Hour'] = df['Start Time'].dt.hour
    Common_Hour = Display_Common(df, 'Hour')
    print(f'Most common hour is: {Common_Hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    Common_Start_Station = Display_Common(df, 'Start Station')
    print(f'Most used start station is: {Common_Start_Station}')

    Common_End_Station = Display_Common(df, 'End Station')
    print(f'Most used end station is: {Common_End_Station}')

    df['Start-End Combination'] = df['Start Station'] + " to " + df['End Station']
    Most_Frequent_Combination = Display_Common(df, 'Start-End Combination')
    print(f'Most frequent combination of start station and end station trip is: {Most_Frequent_Combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    Total_Travel_Time = df['Trip Duration'].sum()
    print(f'Total travel time is: {Total_Travel_Time}')

    Mean_Travel_Time = df['Trip Duration'].mean()
    print(f'Mean travel time is: {Mean_Travel_Time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(f'The count of user types is: {user_types}')

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('The count of genders: ')
        print(gender)
    else:
        print(f'Sorry, no gender data available for {city.title()} City')

    if 'Birth Year' in df.columns:
        min_Birth = df['Birth Year'].min()
        print(f'Earliest year of birth is: {min_Birth}') 
        max_Birth = df['Birth Year'].max()
        print(f'Most recent year of birth is: {max_Birth}')
        Common_Birth = Display_Common(df, 'Birth Year')
        print(f'Most common year of birth is: {Common_Birth}')
    else:
        print(f'Sorry, no birth year data available for {city.title()} City')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
