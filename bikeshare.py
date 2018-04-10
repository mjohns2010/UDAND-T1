import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWe currently have data for Chicago, New York City, and Washington. Which city would you like to see?\n')
        if city.lower() in ('new york'):
            city = 'new york city'
            break
        elif city.lower() not in ('chicago', 'new york city', 'washington'):
            print ('\nThat input isn\'t valid. Please try again.\n')
            continue
        else:
            break       
    
    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('\nName of the month to filter by, or "all" to apply no month filter?\n')
        if month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print ('\nThat input isn\'t valid. Please try again.\n')
            continue
        else:
            break    

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\nName of the day to filter by, or "all" to apply no day filter?\n')
        if day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print ('\nThat input isn\'t valid. Please try again.\n')
            continue
        else:
            break    
    #print(city, month, day)
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    #print(df.head())

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #print(df.head())


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    #df = pd.read_csv(CITY_DATA)
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    com_month = df['month'].mode()[0]
    print("The most popular month for bikesharing is: ", com_month)

    # display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    com_day = df['day'].mode()[0]
    print("The most popular day of the week for bikesharing is: ", com_day)

    # display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    com_hour = df['hour'].mode()[0]
    print("The most popular time for bikesharing is: ", com_hour)
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df


def main():
    while True:
        city, month, day = get_filters('chicago', 'june', 'wednesday')
        #print(city, month, day)
        load_data(city, month, day)

        time_stats(df, month, day)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()


