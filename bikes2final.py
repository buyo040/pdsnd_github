import time
import pandas as pd
import numpy as np

cities = ['chicago', 'new york city', 'washington']

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thurstday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ""
    month = ""
    day = ""

    print('Hello! Let\'s explore some US bikeshare data!')
    while city not in cities:
        city = input('For which city would you like to explore data (chicago, new york city or washington): ')
        city = city.lower()
        if city not in cities:
            print('Please type in either chicogo, new york city or washington')
    while month not in months:
        month = input('For which month would you like to explore some date (January until June). If you would like to contunie with all month type all: ')
        month = month.lower()
        if month not in months:
            print('Please type in either all or a single month from january to june')
        if month == 'january':
            month_num = '1'
        elif month == 'february':
            month_num ='2'
        elif month == 'march':
            month_num ='3'
        elif month == 'april':
            month_num ='4'
        elif month == 'may':
            month_num ='5'
        elif month == 'june':
            month_num = '6'

    while day not in days:
        day = input('For which weekday would you like to explore some date or all if you would like to see all weekdays: ')
        day = day.lower()
        if day not in days:
            print('Please type in either all or a single month from january to june')
        if day == 'monday':
            day_num = '0'
        elif day == 'tuesday':
            day_num ='1'
        elif day == 'wednesday':
            day_num ='2'
        elif day == 'thurstday':
            day_num ='3'
        elif day == 'friday':
            day_num ='4'
        elif day == 'saturday':
            day_num = '5'
        elif day == 'sunday':
            day_num = '6'

    month = int(month_num)
    day = int(day_num)
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

    df['Month'] = pd.DatetimeIndex(df['Start Time']).month
    df['Day'] = pd.DatetimeIndex(df['Start Time']).weekday

    if month == "all":
        df = df
    else:
        df = df[df.Month == month]

    if day == "all":
        df = df
    else:
        df = df[df.Day == day]

    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_month = df['Month'].value_counts()
    popular_month = popular_month.sort_values(ascending=False)

    popular_day = df['Day'].value_counts()
    popular_day = popular_day.sort_values(ascending=False)

    popular_hour = df['hour'].value_counts()
    popular_hour = popular_hour.sort_values(ascending=False)
    print('Most popular month:')
    print(popular_month.head(1))
    print('Most popular day:')
    print(popular_day.head(1))
    print('Most popular hour:')
    print(popular_hour.head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start_station = df['Start Station'].value_counts()
    popular_start_station = popular_start_station.sort_values(ascending=False)

    print('Most popular start station:')
    print(popular_start_station.head(1))


    popular_end_station = df['End Station'].value_counts()
    popular_end_station = popular_end_station.sort_values(ascending=False)

    print('Most popular end station:')
    print(popular_end_station.head(1))


    df['Start to End Station'] = df['Start Station'] + df['End Station']
    popular_route = df['Start to End Station'].value_counts()
    popular_route = popular_route.sort_values(ascending=False)

    print('Most popular route:')
    print(popular_route.head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:')
    print(total_travel_time)

    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time:')
    print(average_travel_time)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('User types:')
    print(user_types)

    if city == "washington":
        print('No Gener data')
    else:
        user_gender = df['Gender'].value_counts()
        print('Gender Data of users:')
        print(user_gender)

    if city == "washington":
        print('No birth Year Data')
    else:
        user_birthyear = df['Birth Year']
        olderst_user = user_birthyear.sort_values(ascending=True)
        print('The oldest user was born in:')
        print(olderst_user.head(1))
        youngest_user = user_birthyear.sort_values(ascending=False)
        print(youngest_user.head(1))
        print('The youngest user was born in:')
        popular_birth_year = user_birthyear.value_counts()
        popular_birth_year = popular_birth_year.sort_values(ascending=False)
        print('Most users were born in:')
        print(popular_birth_year.head(1))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def data_view(df):
    show_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?: ")
    show_data = show_data.lower()
    start_loc = 0
    while show_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        show_data = input('Do you wish to continue?: ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        data_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
