import time
import pandas as pd
import numpy as np
import calendar
import datetime

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
   
    print("Hello! Let's explore some U.S. bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWe currently have data for Chicago, New York City, and Washington. Which city would you like to see?\n")
        if city.lower() in ('new york'):
            city = 'new york city'
            break
        elif city.lower() not in ('chicago', 'new york city', 'washington'):
            print ("\nThat input isn't valid. Please try again.\n")
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    com_month1 = df['month'].mode()[0]
    com_month2 = calendar.month_name[com_month1]
    print("The most popular month for bikesharing in {} is: {} ".format(city.title(), com_month2))

    # display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    com_day = df['day'].mode()[0]
    print("The most popular day of the week for bikesharing in {} is: {} ".format(city.title(), com_day))
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hour = df['hour'].mode()[0]
    print("The most popular hour to start bikesharing in {} is: {} ".format(city.title(), com_hour))
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("The most popular Start Station for bikesharing in {} is: {} ".format(city.title(), start_station))
   
    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("The most popular End Station for bikesharing in {} is: {} ".format(city.title(), end_station))

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " / " + df['End Station']
    common_trip = df['Trip'].value_counts().idxmax()
    print("The most common trip for bikesharing in {} is: {} ".format(city.title(), common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""
    def time_convert(time_sec):
            time = time_sec
            time = total_duration
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            #return ("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
            return (days, hours, minutes, seconds)
        
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    #total_duration = (df['Trip Duration'].sum().item())
    total_duration = (int(df['Trip Duration'].sum()))
    print(type(total_duration))
    days, hours, minutes, seconds = time_convert(total_duration)
    print ("The total travel duration was {} days, {} hours, {} minutes, {} seconds.".format(days, hours, minutes, seconds))

    # display mean travel time
    mean_travel = (int(df['Trip Duration'].mean()))
    print(type(mean_travel))
    days2, hours2, minutes2, seconds2 = time_convert(mean_travel)
    print ("The mean travel duration was {} days, {} hours, {} minutes, {} seconds.".format(days2, hours2, minutes2, seconds2))
    #print("the mean duration for {} in {} on {} is {} minutes.".format(city.title(), month.title(), day.title(), mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_values = df['User Type'].value_counts()
    
    #dataframe[column].value_counts().index.tolist()
    print("There were {} riders who were subscribers.".format(user_values[0]))
    print("There were {} riders who were customers.".format(user_values[1]))

    # Display counts of gender
    while True:
        #Error handler for Washington not having user data.
        if city == 'washington':
            print('\nThere is no further user data for Washington.')
            break
        else:
            gender_counts = df['Gender'].value_counts()
            
            print("\nThere were {} male riders.".format(gender_counts[0]))
            print("There were {} female riders.".format(gender_counts[1]))
            
            # Display earliest, most recent, and most common year of birth
            earliest_year = int(df['Birth Year'].min())
            recent_year = int(df['Birth Year'].max())
            common_year = int(df['Birth Year'].value_counts().idxmax())
            
            print("\nThe oldest rider was born in {}.".format(earliest_year))
            print("The youngest rider was born in {}.".format(recent_year))
            print("Most riders were born in {}.".format(common_year))
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters('chicago', 'june', 'wednesday')
        load_data(city, month, day)
        df = load_data(city, month, day)
        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()



