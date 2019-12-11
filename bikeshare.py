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
    valid_cities =['chicago','new york city','washington']
    city =input('please choose a city : chicago,new york city,washington\n').strip()
    while city not in  valid_cities:
      print('Invalid City!\n ')
      city =input('please choose a city : chicago,new york city,washington\n').strip()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months =['january','February','March','April','May','June','July','August','September','October','November','December','All']
    month =input ('Please Enter the month or enter All\n').strip().title()
    while month not in valid_months:
      print('invalid month!\n')
      month =input ('Please Enter the month or enter All\n').strip().title() 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    day =input('Please Enter the day or enter All\n').strip().title()
    while day not in valid_days: 
      print('invalid da!\n')
      day =input('Please Enter the day or enter All\n').strip().title()
        
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
    # filtered by the city
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the start and end times from strings to dates, so we can extract the day/month from them
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract the day and month into their separate columns
    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()
    
     # filter by month if applicable
    if month != 'All':
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'All': 
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month_name()
    popular_month = df['month'].mode()[0]
    print("Most common month:\n{}\n".format(popular_month)) 

    # TO DO: display the most common day of week  
    df['day'] = df['Start Time'].dt.day_name()
    popular_day = df['day'].mode()[0]
    print("Most comon day:\n{}\n".format(popular_day)) 

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most comon start hour:\n{}\n".format(popular_hour)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start =df['Start Station'].mode()[0]
    print("Most common start station :\n{}\n".format(popular_start))

    # TO DO: display most commonly used end station
    popular_end =df['End Station'].mode()[0]
    print("Most common end station :\n{}\n".format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] =df['Start Station'].map(str)+df['End Station']
    popular_route=df['route'].mode()[0]
    print("Most common route:\n{}\n".format(popular_route))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total =df['Trip Duration'].sum()
    print("Total travel time:\n{}\n".format(total))

    # TO DO: display mean travel time
    mean =df['Trip Duration'].mean()
    print ("Mean travel time :\n{}\n".format(mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type =df['User Type']
    type_counts =user_type.value_counts()
    print ("Count of user type :\n")
    print(type_counts)

     # TO DO: Display counts of gender
    try:
        gender_count =df.Gender.value_counts()
        print ("Count of user gender :\n")
        print(gender_count)
    except:
        print("There is no gender data in this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest =df['Birth Year'].min()
        print("Earliest birth year is:\n{}\n".format(earliest))

        recent =df['Birth Year'].max()
        print("The most recent birth year is:\n{}\n".format(recent))

        popular_year=df['Birth Year'].mode()[0]
        print("Most common  birth year is:\n{}\n".format(popular_year))

    except:
        print("There is no  birth year data in this city")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    choice =input ('Would you like to read some of the row data? Yes/No')
    print()
    if choice =='yes' or choice=='y':
        choice=True
    elif choice=='no'or choice=='n':
        choice=False
    else:
        print('You did not enter a valid choice.Let\'s try that again.')
        display_data(df)
        return
    
    if choice:
        while 1:
            for i in range (5):
                print(df.iloc[i])
                print()
            choice= input('Another five? Yse/No').lower()
            if choice=='yes'or choice=='y':
                continue
            elif choice=='no'or 'n':
                break
            else:
                    print('You did not enter a valid choice.')
                    return
                
                
def main():
    restart="yes"
    while(restart=="yes"):
       
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()