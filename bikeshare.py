import calendar
import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'bikesharenew_york_city.csv',
             'washington': 'washington.csv'}


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
        user_input_city = input("please select one of cities 'chicago' , 'new york city' , 'washington' as input : \n ").lower()
        check = CITY_DATA.get(user_input_city)
        if check is not None:
            print("you choosed : {}".format(user_input_city))
            city = user_input_city
            break
        else:
            print("please enter a valid city name")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        user_input_month = input("please enter month from jan to june or all for all months : \n ").lower()
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        if user_input_month in months:
            print("you choosed : {}".format(user_input_month))
            month = user_input_month
            break
        else:
            print("please enter a valid month form jan to june or all for all months")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        user_input_day = input("please enter day of week or all for all week : \n ").lower()
        week_days = ['all', 'saturday', 'sunday', 'monday', 'tuseday', 'wednesday', 'thrusday', 'friday']
        if user_input_day in week_days:
            print("you choosed : {}".format(user_input_day))
            day = user_input_day
            break
        else:
            print("please enter a valid week day or all for all week")

    print('-' * 40)
    return city, month, day


# print(get_filters()) # this line for my check that code running as well !!

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
    df['Start Time'] = df['Start Time'].apply(pd.to_datetime)
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    df['Start_hour'] = df['Start Time'].dt.hour

    # write if statement to filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # write an if statement to filter by day

    if day != 'all':
        df = df[df['week_day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month is :{calendar.month_name[common_month]}")

    # TO DO: display the most common day of week
    common_day = df['week_day'].mode()[0]
    print(f"The most common week day : {common_day}")

    # TO DO: display the most common start hour
    common_hour = df['Start_hour'].mode()[0]
    print(f"The most common start hour : {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most common station : {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most common end station : {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['frequant_direction'] = "Start Station : "+df['Start Station'] + " TO " + " End Station : "+ df['End Station']
    count_frequant_direction = df['frequant_direction'].value_counts(sort=True)
    common_direction = max(count_frequant_direction)
    print(f"direction regularet used  : {count_frequant_direction}")
    print(f"The most common direction : {common_direction}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = round(sum(df['Trip Duration']/3600),2)
    print(f"Total travel time : {Total_Travel_Time} Hours")
    # TO DO: display mean travel time
    Avg_Travel_Time = round((df['Trip Duration']/3600).mean(),2)
    print(f"Avraged travel time : {Avg_Travel_Time} Hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    # print(user_types)
    print(f"user types: {user_types}")
    # TO DO: Display counts of gender
    # check for the presence of Gender in Data Frame
    check_gender = df.get('Gender')
    if check_gender is not None :
        print(f"Gender count : {df['Gender'].value_counts()}")
    else :
        print("gender is not present for current city !")
    # TO DO: Display earliest, most recent, and most common year of birth
    check_birth = df.get('Birth Year') # add variable to check the presence of Birth Year in Data
    if check_birth is not None :
        earliest_year = df['Birth Year'].min()
        print(f"earliest year: {earliest_year}")
        most_recent_year = df['Birth Year'].max()
        print(f"most recent year:  {most_recent_year}")
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print(f"most common year:  {most_common_year}")
    else :
        print("data of birth year is not present")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_raw_data(df):
    i = 0 # set iteration variable
    # ask user if he want to review five raws of data
    user_input = input("would you like to review first five raw of data ? Y/N : \n").upper()
    while True :
            if user_input == 'Y':
                print(df[i: i+5])
                user_input = input("would you like to review the next five raws ? Y/N : \n").upper()
                i += 5
            if user_input == 'N':
                break
            else :
                print("please enter valid choice")
                user_input = input("would you like to review the next five raws ? Y/N : \n").upper()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        user_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
